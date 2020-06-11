import numpy as np


class Matrix:
    def __init__(self, s):
        self.matrix = np.array([col for col in [list(map(int, row.split())) for row in s.split("\n")]])

    def row(self, index):
        return self.matrix[index-1, :]

    def column(self, index):
        return self.matrix[:, index-1]


m = Matrix("1 2 3\n5 56 7\n9 2 6")
print(m.column(0))

#[print(col) for col in [row.split() for row in s.split("\n")]]