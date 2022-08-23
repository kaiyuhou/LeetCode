def fun():
    MOD = 1000000007
    nmax = 100000 * 2
    dp = []
    for i in range(500):
        if i * i < nmax:
            dp.append(i * i)

    for n in range(2000, 10000):
        # a, b = map(int, input().split())
        print(n)
        A = [-1] * n
        # Can_in = [[] for _ in range(n)]
        # Can_have = [[] for _ in range(n)]
        used = set()
        ans = True
        for i in range(n - 1, -1, -1):
            possible = - 1
            for j, s in enumerate(dp):
                if s < i:
                    continue
                if s - i >= n:
                    if possible != -1:
                        A[i] = possible
                        used.add(possible)
                    else:
                        ans = False
                    break
                cur = s - i
                if cur not in used:
                    possible = cur
            if ans is False:
                break
        if ans:
            assert -1 not in A
            assert max(used) == n - 1
            assert len(used) == n
            continue
        else:
            print(n, -1, A)
            c = input()

fun()