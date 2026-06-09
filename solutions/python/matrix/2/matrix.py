class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_str = matrix_string.splitlines()
        self.rows =[]
        for i in range(len(self.matrix_str)):
            self.rows.append([int(x) for x in self.matrix_str[i].split()])
        self.columns=[]
        for i in range(len(self.rows[0])):
            c = []
            for j in range(len(self.rows)):
                c.append(self.rows[j][i])
            self.columns.append(c)

    def row(self, index):
        return self.rows[index]

    def column(self, index):
        return self.columns[index]

