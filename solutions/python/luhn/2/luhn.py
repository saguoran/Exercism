class Luhn(object):
    def __init__(self, card_num: str):
        self.card_num = card_num

    def is_valid(self):
        card: str = self.card_num.replace(' ', '')[:: -1]
        if len(card) <= 1 or not card.isdigit():
            return False
        else:
            numbers = [int(card[i]) if i % 2 == 0 else int(card[i]) * 2 if int(card[i]) < 5 else int(card[i]) * 2 - 9 for i in range(0, len(card))]
            return sum(numbers) % 10 == 0

