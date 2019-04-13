from math import *
import sys
t, n, m = [int(s) for s in input().split(" ")]
primes = [4, 3, 5, 7, 11, 13, 17]
reply = 1
for T in range(1, t + 1):
    if reply == -1:
        break

    ans = []
    for p in primes:
        s = str(p)
        for i in range(17):
            s = s + " " + str(p)
        print(s)
        sys.stdout.flush()
        A = [int(s) for s in input().split(" ")]
        ans.append(sum(A))

    for ret in range(1000005):
        for i, p in enumerate(primes):
            if ret < ans[i]:
                break
            if (ret - ans[i]) % p != 0:
                break
        else:
            print(ret)
            sys.stdout.flush()
            reply = int(input())
            break
