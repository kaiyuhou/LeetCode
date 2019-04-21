from math import *
t = int(input())
for T in range(1, t + 1):
    N = int(input())
    S = []
    E = []
    L = []
    for _ in range(N):
        s, e, l = [int(s) for s in input().split(" ")]
        S.append(s)
        E.append(e)
        L.append(l)
    # V = set()
    # for i in range(N):
    #     V.add(i)
    # ans = [0]
    #
    # # print(S, E, L)
    #
    # def get_possible(t):
    #     rnt = 0
    #     for i in range(N):
    #         if V[i] == 0:
    #             rnt += max(0, E[i] - L[i] * t)
    #     return rnt
    #
    # def dfs(cur, cur_ans, t):
    #     # print(cur, cur_ans, t)
    #     ans[0] = max(ans[0], cur_ans)
    #     if cur_ans + get_possible(t) > ans[0]:
    #         for i in range(N):
    #             if V[i] == 0 and (E[i] - L[i] * t) > 0:
    #                 V[i] = 1
    #                 dfs(i, cur_ans + (E[i] - L[i] * t), t + S[i])
    #                 V[i] = 0
    #
    # for i in range(N):
    #     V.remove(i)
    #     if E[i] + get_possible(S[i]) > ans[0]:
    #         dfs(i, E[i], S[i])
    #     V.add(i)
    #
    # print("Case #{}: {}".format(T, ans[0]))
    # S = []
    # E = []
    # L = []

    def get_v(A):
        ans = 0
        t = 0
        for i in A:
            if E[i] - t * L[i] <= 0:
                continue
            ans += E[i] - t * L[i]
            t += S[i]
        return ans

    def clean(A):
        rnt = []
        t = 0
        for i in A:
            if E[i] - t * L[i] <= 0:
                continue
            rnt.append(i)
            t += S[i]
        return rnt

    best = [0]
    ans = E[0]
    for i in range(1, N):
        cur_best = []
        cur_max = 0
        for k in range(0, len(best) + 1):
            cur = best[0 : k] + [i] + best[k:]
            v = get_v(cur)
            if v > cur_max:
                cur_max = v
                cur_best = list(cur)

        if cur_max > ans:
            ans = cur_max
            best = clean(cur_best)

    print("Case #{}: {}".format(T, ans))

