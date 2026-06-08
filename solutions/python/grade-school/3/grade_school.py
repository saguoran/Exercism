from collections import defaultdict
from functools import reduce


class School(object):

    def __init__(self):
        self.kids = defaultdict(set)

    def add_student(self, name, grade):
        self.kids[grade].add(name)

    def roster(self):
        sorted_grades = sorted(self.kids.keys())
        all_names = [self.grade(grade) for grade in sorted_grades]
        try:
            return reduce(list.__add__,all_names)
        except TypeError as e:
            print(f"{e}, don't have any student or grade in school")
            return list()

    def grade(self, grade_number):
        return sorted(self.kids[grade_number])

