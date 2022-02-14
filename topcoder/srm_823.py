
# class OxToTiger:
#     def rewrite(self, message):
#         ms = message.split(' ')
#         for i, m in enumerate(ms):
#             if m == 'ox':
#                 ms[i] = 'tiger'
#         return ' '.join(ms)
#
#
# ox = OxToTiger()
# message = 'ox'
# message = '"the ox the ox the ox and the fox in the box"'
# print(ox.rewrite(message))

# class TigerRiverCrossing:
#     def addRocks(self, river, maxL):
#         n = len(river)
#         m = len(river[0])
#         if maxL > n:
#             return river
#
#         ans = {}
#         for i in range(n):
#             if i >= maxL:
#                 break
#             for j in range(m):
#                 for k in range(1, maxL + 1):
#                     cur_pos = i
#                     cur_ans = 0
#
#                     while cur_pos < n:
#                         if river[cur_pos][j] == '=':
#                             cur_ans += 1
#                         cur_pos += k
#                     ans[i, j, k] = cur_ans
#
#         best_ans = min(ans.values())
#         river = [list(r) for r in river]
#         for key, value in ans.items():
#             if value == best_ans:
#                 i, j, k = key
#                 while i < n:
#                     river[i][j] = 'O'
#                     i += k
#                 return tuple([''.join(r) for r in river])
#
# s = TigerRiverCrossing()
# river = ("===============", "========O======", "===============", "========O======", "=O=============", "========O======", "===============", "========O======", "===============", "========O======")
# maxL = 2
# print(s.addRocks(river, maxL))

class JumpingTiger:
    def travel(self, plan):
        n = len(plan)
        m = len(plan[0])
        v = {}
        for i in range(n):
            for j in range(m):
                v[i, j] = (False, 0)
                if plan[i][j] == 'T':
                    sx, sy = i, j
                if plan[i][j] == 'L':
                    ex, ey = i, j

        ans = [50 * 50 * 50]
        mv = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(x, y, last_mv, last_d, steps):
            # print(x, y, last_mv, last_d, steps)
            if steps > ans[0]:
                return
            if last_mv == 1 and (x, y) == (ex, ey):
                if steps < ans[0]:
                    ans[0] = steps
                return
            if last_mv == 1:
                v[x, y] = (True, steps)
                for d, (mx, my) in enumerate(mv):
                    for k in range(max(n, m)):
                        nx, ny = x + mx * k, y + my * k
                        if 0 <= nx < n and 0 <= ny < m:
                            if (v[nx, ny][0] == False or v[nx, ny][1] >= steps) and plan[nx][ny] != '#':
                                dfs(nx, ny, k, d, steps + 1)
                        else:
                            break
            else:
                for k in range(1, last_mv):
                    mx, my = mv[last_d]
                    nx, ny = x + mx * k, y + my * k
                    if 0 <= nx < n and 0 <= ny < m:
                        if (v[nx, ny][0] == False or v[nx, ny][1] >= steps) and plan[nx][ny] != '#':
                            dfs(nx, ny, k, last_d, steps + 1)
                    else:
                        break


        dfs(sx, sy, 1, 0, 0)
        return ans[0] if ans[0] < 50 * 50 * 50 else -1

s = JumpingTiger()
p = ("T.######", "#..#####", "##..####", "###..###", "####..##", "#####..#", "######..", "#######L")
p = ("T.######", "#..#####", "##..####", "###..###", "####..##", "#####..#", "######..", ".######L")
p = ("T.######",
     "#..#####",
     "##..####",
     "###..###",
     "####..##",
     "#####..#",
     ".#####..",
     ".######L")
p = ['T' + '.' * 49, '.' * 50, '.' * 49 + 'L']
print(s.travel(p))





















































