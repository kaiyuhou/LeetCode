import os
import shutil
import random


def test():
    n = 10
    A = [0] * n
    for i in range(n):
        A[i] = random.randint(-20, 20)
    # print(A)

    ground = True
    L, R = 0, 0
    for i in range(n - 1):
        for j in range(i + 1, n + 1):
            if max(A[i:j]) < sum(A[i:j]):
                ground = False
                L, R = i, j
                break

    ans = get_ans(A, n)

    if ans != ground:
        print(*A, ground, ans, L, R)
        return False


def get_ans(A, n):
    ans = True
    for i in range(n - 1):
        if A[i] > 0 and A[i + 1]> 0:
            # print('NO')
            ans = False
    if not ans:
        return ans

    B = [A[0]]
    for i in range(1, n):
        if A[i] <= 0 and B[-1] <= 0:
            B[-1] += A[i]
        else:
            B.append(A[i])
    A = B
    n = len(B)

    last = A[0]
    ma = A[0]

    for i in range(1, n):
        a = A[i]
        if a > 0:
            if last <= 0:
                last = a
                ma = a
            else:
                if (last + a) > max(ma, a):
                    ans = False
                    break
                if a > abs(A[i-1]):
                    ans = False
                    break

                last = last + a
                ma = max(ma, a)
        else:
            if last + a <= 0:
                last = a
                ma = 0
            else:
                last = last + a
    return ans


for i in range(10000):
    test()





