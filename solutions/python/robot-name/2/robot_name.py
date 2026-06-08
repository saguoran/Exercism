from itertools import product
from string import ascii_uppercase, digits

'''Generate all names and assign them into a set, which I learned in tcarobruce's solution thanks'''
names = {''.join(name) for name in product(ascii_uppercase, ascii_uppercase, digits, digits, digits)}

'''because the elements in set are already random so all I need to do is pop them all'''


class Robot(object):
    def __init__(self):
        self.name = names.pop()

    def reset(self):
        self.name = names.pop()
