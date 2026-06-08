from string import ascii_uppercase, digits
from random import sample


class Robot(object):
    names = ''

    def __init__(self):
        while True:
            self.name = ''.join(sample(ascii_uppercase, 2) + sample(digits, 3))
            if self.name not in Robot.names:
                break
        Robot.names += self.name

    def reset(self):
        self.__init__()


