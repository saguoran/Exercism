from collections import Counter


def boxes_score(dices: list, dice):
    return dice * dices.count(dice)


def four_times_same_dices(dices):
    four_dices = [dice for dice in set(dices) if dices.count(dice) > 3]
    return 4 * four_dices[0] if four_dices else 0


YACHT = (lambda dices: 50 if len(set(dices)) == 1 else 0)
ONES = (lambda dices: boxes_score(dices, 1))
TWOS = (lambda dices: boxes_score(dices, 2))
THREES = (lambda dices: boxes_score(dices, 3))
FOURS = (lambda dices: boxes_score(dices, 4))
FIVES = (lambda dices: boxes_score(dices, 5))
SIXES = (lambda dices: boxes_score(dices, 6))
FULL_HOUSE = (lambda dices: sum(dices) if sorted(Counter(dices).values()) == [2, 3] else 0)
FOUR_OF_A_KIND = four_times_same_dices
LITTLE_STRAIGHT = (lambda dices: 30 if sorted(dices) == [1, 2, 3, 4, 5] else 0)
BIG_STRAIGHT = (lambda dices: 30 if sorted(dices) == [2, 3, 4, 5, 6] else 0)
CHOICE = sum


def score(dice, category):
    return category(dice)


