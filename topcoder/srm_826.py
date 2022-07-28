# class GetGas:
#     def optimize(self, G, Dto, Dfrom, gasPrice):
#         ans = float('inf')
#         for i, d1 in enumerate(Dto):
#             if G * 25 < Dto[i]:
#                 continue
#
#             total = Dto[i] + Dfrom[i]
#             rest = total - G * 25
#             if rest <= 0:
#                 ans = 0
#             else:
#                 ans = min(ans, rest * gasPrice[i] * 1.0 / 25)
#         return ans
#
# s = GetGas()
# print(s.optimize(10, (240, 260), (1000, 10), (417, 233)))

# class VisitPoints:
#     def visit(self, Xs, Ys):
#         n = len(Xs)
#         Ps = set()
#         for x, y in zip(Xs, Ys):
#             Ps.add((x, y))
#         restP = set([i for i in range(n)])
#
#         curX, curY = 0, 0
#         ans = ''
#
#         def get_small():
#             ret = 0
#             min_dis = 100
#             for i in restP:
#                 x, y = Xs[i], Ys[i]
#                 dis = abs(curX - x) + abs(curY - y)
#                 if dis < min_dis:
#                     min_dis = dis
#                     ret = i
#             return ret
#
#         x_to_d = {
#             1: 'E',
#             -1: 'W'
#         }
#
#         y_to_d = {
#             1: 'N',
#             -1: 'S'
#         }
#
#         def get_path(nxtX, nxtY, curX, curY):
#             diX, diY = 1, 1
#             if curX > nxtX:
#                 diX = -1  # 1: E, -1: W
#             if curY > nxtY:
#                 diY = -1  # 1: N, -1: S
#
#             ret = ''
#             while curX != nxtX:
#                 x, y = curX + diX, curY
#                 if (x, y) not in Ps:
#                     ret += x_to_d[diX]
#                 else:
#                     if (x, y) == (nxtX, nxtY):
#                         ret += x_to_d[diX]
#                         return ret
#                     y += curY + diY
#                     ret += y_to_d[diY]
#                     ret += x_to_d[diX]
#                     if curY > nxtY:
#                         diY = -1
#                     else:
#                         diY = 1
#                 curX, curY = x, y
#
#             while curY != nxtY:
#                 x, y = curX, curY + diY
#                 if (x, y) not in Ps:
#                     ret += y_to_d[diY]
#                 else:
#                     if (x, y) == (nxtX, nxtY):
#                         ret += y_to_d[diY]
#                         return ret
#                     y += diY
#                     ret += x_to_d[diX]
#                     ret += y_to_d[diY]
#                     ret += y_to_d[diY]
#                     ret += x_to_d[-1 * diX]
#                 curX, curY = x, y
#
#             return ret
#
#         while len(restP) > 0:
#             pi = get_small()
#             restP.remove(pi)
#             nxtX, nxtY = Xs[pi], Ys[pi]
#             # print(pi, curX, curY, nxtX, nxtY)
#             ans += get_path(nxtX, nxtY, curX, curY)
#             curX, curY = nxtX, nxtY
#
#         return ans
#
#
# s = VisitPoints()
# X = (1, 2, 3)
# Y = (1, 3, 5)
# X = (1, 7, 3, 9, 5)
# Y = (1, 1, 1, 1, 1)
# X = (4, 11, 13, 18, 12)
# Y = (21, 4, 17, 9, 19)
# print(s.visit(X, Y))

class TwoFairDice:
    def finish(self, A, B):
        A = list(A)
        B = list(B)
        if len(B) == 0:
            return 0

        A.sort()

        # tot_case = 36
        win_case, loss_cass, tie_cass = 0, 0, 0
        for b in B:
            for a in A:
                if b == a:
                    tie_cass += 1
                elif b < a:
                    loss_cass += 1
                else:
                    win_case += 1

        rest_case = 36 - len(A) * len(B)
        unfair_case = abs(win_case - loss_cass)
        if rest_case < unfair_case:
            return 0

        rest_die = 6 - len(B)

        ans = 0

        def get_win_loss(cur):
            win, loss = 0, 0
            for a in A:
                if cur < a:
                    loss += 1
                if cur > a:
                    win += 1
            return win, loss

        def dfs(rest_die, unfair_case):
            nonlocal ans
            if rest_die == 1:
                if unfair_case > 6:
                    ans += 0
                if unfair_case == 0:
                    if B[2] == B[3]:
                        cur = B[2]
                        win, loss = get_win_loss(cur)
                        if win == loss:
                            ans += 1
                    else:
                        cur = B[2] + 1
                        win, loss = get_win_loss(cur)
                        if win == loss:
                            ans += B[3] - B[2] - 1





































































