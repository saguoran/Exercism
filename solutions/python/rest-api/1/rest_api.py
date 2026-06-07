import json

class RestAPI:
    def __init__(self, database=None):
        # Initialize database, tracking our users as a list
        self.database = database if database else {"users": []}

    def _get_user(self, name):
        """Helper to fetch a user dict from our list by name."""
        for user in self.database["users"]:
            if user["name"] == name:
                return user
        return None

    def get(self, url, payload=None):
        if url == "/users":
            if payload:
                # Filter down to specific requested usernames
                target_names = json.loads(payload).get("users", [])
                filtered_users = [
                    user for user in self.database["users"] 
                    if user["name"] in target_names
                ]
                return json.dumps({"users": filtered_users})
            
            # If no payload, return everyone in the current state
            return json.dumps({"users": self.database["users"]})

    def post(self, url, payload=None):
        data = json.loads(payload) if payload else {}

        if url == "/add":
            username = data.get("user")
            new_user = {
                "name": username,
                "owes": {},
                "owed_by": {},
                "balance": 0.0
            }
            self.database["users"].append(new_user)
            # Sorting alphabetically keeping structural predictability
            self.database["users"].sort(key=lambda u: u["name"])
            return json.dumps(new_user)

        if url == "/iou":
            lender_name = data.get("lender")
            borrower_name = data.get("borrower")
            amount = data.get("amount", 0.0)

            lender = self._get_user(lender_name)
            borrower = self._get_user(borrower_name)

            # 🧮 DEBT CANCELLATION ENGINE:
            # Check if the lender already owed the borrower anything
            if borrower_name in lender["owes"]:
                existing_debt = lender["owes"][borrower_name]
                if amount > existing_debt:
                    # Lender lends more than they owed. Debt is cleared, 
                    # and borrower now owes the remainder to the lender!
                    amount -= existing_debt
                    del lender["owes"][borrower_name]
                    del borrower["owed_by"][lender_name]
                    
                    lender["owed_by"][borrower_name] = lender["owed_by"].get(borrower_name, 0.0) + amount
                    borrower["owes"][lender_name] = borrower["owes"].get(lender_name, 0.0) + amount
                elif amount == existing_debt:
                    # Perfect clean slate split!
                    del lender["owes"][borrower_name]
                    del borrower["owed_by"][lender_name]
                else:
                    # Lender still owes borrower, but the debt is reduced
                    lender["owes"][borrower_name] -= amount
                    borrower["owed_by"][lender_name] -= amount
            else:
                # Pure new loan logic (No pre-existing opposing debts)
                lender["owed_by"][borrower_name] = lender["owed_by"].get(borrower_name, 0.0) + amount
                borrower["owes"][lender_name] = borrower["owes"].get(lender_name, 0.0) + amount

            # 📊 Recalculate balances after modifications
            lender["balance"] = sum(lender["owed_by"].values()) - sum(lender["owes"].values())
            borrower["balance"] = sum(borrower["owed_by"].values()) - sum(borrower["owes"].values())

            # Return only the modified users participating in the transaction, sorted alphabetically!
            affected_users = [lender, borrower]
            affected_users.sort(key=lambda u: u["name"])
            return json.dumps({"users": affected_users})