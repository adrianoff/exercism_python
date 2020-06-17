import numpy as np


class Matrix:
    def __init__(self, s):
        self.matrix = np.array([col for col in [list(map(int, row.split())) for row in s.split("\n")]])

    def row(self, index):
        return list(self.matrix[index-1, :])

    def column(self, index):
        return list(self.matrix[:, index-1])