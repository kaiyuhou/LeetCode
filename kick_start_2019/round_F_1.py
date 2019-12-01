from math import *
t = int(input())
for T in range(1, t + 1):
    N, K = [int(s) for s in input().split(" ")]
    A = [int(s) for s in input().split(" ")]
    H = set(A)

    dp ={(h, 0): 0 for h in H} # step, diff

    for a in A:
        dpa = {}
        for (end, diff), step in dp.items():
            if end == a:
                if (end, diff) in dpa.keys():
                    dpa[(end, diff)] = min(step, dpa[(end, diff)])
                else:
                    dpa[(end, diff)] = step
            else:
                if (a, diff + 1) in dpa.keys():
                    dpa[(a, diff + 1)] = min(step, dpa[(a, diff + 1)])
                else:
                    dpa[(a, diff + 1)] = step

                if (end, diff) in dpa.keys():
                    dpa[(end, diff)] = min(step + 1, dpa[(end, diff)])
                else:
                    dpa[(end, diff)] = step + 1
        dp = dpa

    ans = 105
    for (end, diff), step in dp.items():
        if diff <= K:
            ans = min(ans, step)
    print("Case #{}: {}".format(T, ans))
