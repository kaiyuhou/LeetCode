# class DoubleLetterCount:
#     def count(self, s):
#         ans = 0
#         for a, b in zip(s, s[1:]):
#             if a == b:
#                 ans += 1
#         return ans

# import itertools
#
# class TriangleCounting:
#     def count(self, x, y):
#         n = len(x)
#         if n < 3:
#             return 0
#
#         ans = 0
#         L = list(range(n))
#         for a, b, c in itertools.combinations(L, 3):
#             if (x[a] - x[b]) * (y[a] - y[c]) != (x[a] - x[c]) * (y[a] - y[b]):
#                 ans += 1
#         return ans
#
# s = TriangleCounting()
# x = [ 0, 2, 4, 6, 8 ]
# y = [ 0, 5, 3, 15, 6 ]
# print(s.count(x, y))

class ChamberCount:
    def count(self, map):
        n = len(map)
        m = len(map[0])
        ans = 0

        A = [list(a) for a in map]


        def dfs(i, j):
            for nx, ny in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x = i + nx
                y = j + ny
                if 0 <= x < n and 0 <= y < m and A[x][y] == '.':
                    A[x][y] = '1'
                    dfs(x, y)

        for i in range(n):
            for j in range(m):
                if A[i][j] == '.':
                    A[i][j] = '1'
                    ans += 1
                    dfs(i, j)

        return ans


s = ChamberCount()
map = ["...", "...", "..."]
print(s.count(map))




