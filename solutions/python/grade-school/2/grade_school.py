class School(object):

    def __init__(self):
        self.kids = {}

    def add_student(self, name, grade):
        if grade in self.kids:
            self.kids[grade] += [name]
        else:
            self.kids[grade] = [name]
        self.kids[grade].sort()

    def roster(self):
        grades = sorted(self.kids.keys())
        roster = []
        for grade in grades:
            for name in self.kids[grade]:
                roster.append(name)
        return roster

    def grade(self, grade_number):
        try:
            return self.kids[grade_number]
        except KeyError:
            return []
