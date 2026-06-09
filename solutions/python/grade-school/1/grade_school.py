class School(object):
    def __init__(self):
        self.grades_kids = {}

    def add_student(self, name, grade):
        if grade not in self.grades_kids:
            self.grades_kids[grade] = ''
        if name not in self.grades_kids[grade]:
            self.grades_kids[grade] += f'{name} '

    def roster(self):
        roster = self.grades_kids
        sorted_grade = sorted(self.grades_kids.keys())
        roster = {grade: ' '.join(sorted(roster[grade].split())) for grade in sorted_grade}
        names = [roster[g] for g in sorted_grade]
        return ' '.join(names).split()

    def grade(self, grade_number):
        try:
            return sorted(self.grades_kids[grade_number].split())
        except KeyError:
            return []


