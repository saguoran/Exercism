from itertools import groupby
# Score categories
# Change the values as you see fit
YACHT = 'YACHT'
ONES = 'ONES'
TWOS = 'TWOS'
THREES = 'THREES'
FOURS = 'FOURS'
FIVES = 'FIVES'
SIXES = 'SIXES'
BOXES = {'ONES': 1, 'TWOS': 2, 'THREES': 3, 'FOURS': 4, 'FIVES': 5, 'SIXES': 6}
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 5
BIG_STRAIGHT = 6
CHOICE = None


def upper_section_score_calculate(dices, category):
    same_dices = [dice for dice in dices if dice == BOXES[category]]
    return sum(same_dices)


def house(dices, category):
    houses = [list(dice) for key, dice in groupby(sorted(dices))]
    same_dices = max(houses, key=lambda x: len(x))
    if category == FULL_HOUSE:
        return sum(dices) if len(same_dices) == 3 else 0
    elif category == FOUR_OF_A_KIND:
        return same_dices.pop() * 4 if len(same_dices) > 3 else 0
    else:
        return 50 if len(same_dices) == 5 else 0


def straight(dices, category):
    dices = sorted(dices)
    max_dice = int(max(dices))
    comparison = list(range(max_dice+1-5, max_dice+1))
    is_straight = dices == comparison
    if is_straight and category == max_dice:
        return 30
    else:
        return 0


def score(dice, category):
    if category in BOXES:
        return upper_section_score_calculate(dice, category)
    elif category in (FULL_HOUSE, FOUR_OF_A_KIND, YACHT):
        return house(dice, category)
    elif category in (LITTLE_STRAIGHT, BIG_STRAIGHT):
        return straight(dice, category)
    else:
        return sum(dice)


