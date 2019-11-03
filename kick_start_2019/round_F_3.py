from math import *
t = int(input())
for T in range(1, t + 1):
    N = int(input())
    A = [int(i) for i in input().split(' ')]
    G = [[i] for i in range(N)]
    for i in range(N - 1):
        x, y = [int(s) - 1 for s in input().split(" ")]
        G[x].append(y)
        G[y].append(x)

    # D = [0] * N
    # for i in range(N):
    #     for e in G[i]:
    #         D[i] += A[e]
    #
    # ans = 0
    #
    # while True:
    #     cur = max(D)
    #     i = D.index(cur)
    #     if cur <= 0:
    #         break
    #     ans += cur
    #     for e in G[i]:
    #         for ev in G[e]:
    #             D[ev] -= A[e]
    #         A[e] = 0
    #     # print(D)

    ans = 0
    for i in range(1 << N):
        select = []
        cur = 0
        for j in range(N):
            if i & (1 << j) > 0:
                select.append(j)
        V = [False] * N
        for village in select:
            for v in G[village]:
                if V[v]: continue
                V[v] = True
                cur += A[v]
        ans = max(ans, cur)
    print("Case #{}: {}".format(T, ans))
