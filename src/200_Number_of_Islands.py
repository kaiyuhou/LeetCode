from typing import  *

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        N = len(grid)
        M = len(grid[0])

        visited = [[False for _ in range(M)] for _ in range(N)]

        def dfs(x, y):
            if grid[x][y] == "0" or visited[x][y] is True:
                return
            visited[x][y] = True
            for step_x, step_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_x = x + step_x
                next_y = y + step_y
                if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                    continue
                dfs(next_x, next_y)

        ans = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == "1" and visited[i][j] is False:
                    ans += 1
                    dfs(i, j)

        return ans

s = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(s.numIslands(grid))
