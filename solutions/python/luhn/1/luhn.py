class Luhn(object):
    def __init__(self, card_num: str):
        self.card_num = card_num

    def is_valid(self):
        return self.valid

    @property
    def valid(self):
        card: str = self.card_num.replace(' ', '')
        if len(card) <= 1 or not card.isdigit():
            return False
        else:
            odds = [int(card[i]) for i in range(1, len(card), 2)]
            evens = [int(card[i]) for i in range(0, len(card), 2)]

            def double_number(n):
                x = 2 * n
                return x if x < 10 else x - 9
            valid_1 = (sum(odds) + sum(map(double_number, evens))) % 10 == 0
            valid_2 = (sum(evens) + sum(map(double_number, odds))) % 10 == 0
            return valid_1 if valid_1 else valid_2
