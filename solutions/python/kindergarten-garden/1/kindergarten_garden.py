class Garden(object):

    def __init__(self, diagram, students = ['Alice', 'Bob', 'Charlie', 'David',
                'Eve', 'Fred', 'Ginny', 'Harriet',
                'Ileana', 'Joseph', 'Kincaid', 'Larry']):
        self.students = students
        import re
        pattern = re.compile(r'([GRVC]{2})?')
        keys2 = [c for c in re.findall(pattern, diagram) if c]
        number_stu = int(len(keys2) / 2)
        self.keys4 = [list(keys2[i] + keys2[i + number_stu]) for i in range(number_stu)]

    def plants(self,name):
        plants = {'G': 'Grass', 'R': 'Radishes', 'V': 'Violets', 'C': 'Clover'}

        def convert_to_value(keys):
            return [plants[key] for key in keys]
        plants_li = [convert_to_value(keys) for keys in self.keys4[self.students.index(name)]]
        from functools import reduce
        student_plants = reduce(list.__add__,plants_li)
        return student_plants
