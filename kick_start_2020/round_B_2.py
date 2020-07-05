from math import *
t = int(input())
for T in range(1, t + 1):
    N, D = [int(s) for s in input().split(" ")]
    A = [int(s) for s in input().split(" ")]
    B = [0] * N
    for i in range(N-1, -1, -1):
        B[i] = (D // A[i]) * A[i]
        D = B[i]
    ans = B[0]
    print("Case #{}: {}".format(T, ans))