from typing import *

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.s = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.s[i + 1][j + 1] = self.s[i + 1][j] + self.s[i][j + 1] - self.s[i][j] + matrix[i][j]

    def sumRegion(self, x1: int, y1: int, x2: int, y2: int) -> int:
        return self.s[x2 + 1][y2 + 1] + self.s[x1][y1] - self.s[x2 + 1][y1] - self.s[x1][y2 + 1]




# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(obj.sumRegion(2, 1, 4, 3))
print(obj.sumRegion(1, 1, 2, 2))
print(obj.sumRegion(1, 2, 2, 4))