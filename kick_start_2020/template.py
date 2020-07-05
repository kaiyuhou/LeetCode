from math import *
t = int(input())

def cnt_x_y(x, y, line):
    n = line
    m = abs(line - x) + 1
    return factorial(n - 1) / (factorial(m - 1) * factorial(n - 1))


def prop(x, y):
    line = x + y - 1
    total = x ** (line - 1)




for T in range(1, t + 1):
    W, H, L, U, R, D = [int(s) for s in input().split(" ")]
    if (L == 1 and R == W) or (U == 1 and D == H):
        print("Case #{}: {}".format(T, 0.0))
    else:
        ans = 0
        # (R + 1, U - 1)
        if R + 1 > W or U - 1 < 0:
            pass
        else:
            ans += prop(R + 1, U - 1)
        if L - 1 < 0 or D + 1 > H:
            pass
        else:
            ans += prop(L - 1, D + 1)



        # (L -1, D + 1)



        # dp = [[0 for _ in range(W)] for _ in range(H)]
        #
        #
        # for j in range(W):
        #     dp[0][j] = 1 / (2 ** j)
        # for i in range(1, H):
        #     print(dp[i - 1])
        #     for j in range(W):
        #         if j == 0:
        #             dp[i][j] = dp[i-1][j] / 2
        #         elif j == W - 1:
        #             dp[i][j] = dp[i-1][j] + dp[i][j-1] / 2
        #         elif i == H - 1:
        #             dp[i][j] = dp[i - 1][j]/2  + dp[i][j-1]
        #         else:
        #             dp[i][j] = (dp[i-1][j] + dp[i][j-1]) / 2
        # print(dp[i])

        # ans = 0
        # if L != 0:
        #     for i in range(U, D + 1):
        #         ans += (dp[i][L - 1])/2
        #     if D + 1 == H:
        #         ans += (dp[D][L-1]) / 2
        # if U != 0:
        #     for j in range(L, R + 1):
        #         ans += dp[U-1][j]/2
        #     if R + 1 == W:
        #         ans += (dp[U-1][R])/2

        print("Case #{}: {}".format(T, 1 - ans))


        # random.seed(T)
        # p = 1000000
        # c = 0
        # for _ in range(p):
        #     x, y = 1, 1
        #     xin = False if L != 0 else True
        #     yin = False if U != 0 else True
        #
        #     xin, yin = False, False
        #     for i in range(W + H - 2):
        #         if random.randrange(2) == 0:
        #             x += 1
        #             if x == L:
        #                 if yin:
        #                     break
        #                 else:
        #                     xin = True
        #             elif x == R + 1:
        #                 c += 1
        #                 break
        #         else:
        #             y += 1
        #             if y == U:
        #                 if xin:
        #                     break
        #                 else:
        #                     yin = True
        #             elif y == D + 1:
        #                 c += 1
        #                 break