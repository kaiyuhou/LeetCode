# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
# t = int(input())  # read a line with a single integer
# for i in range(1, t + 1):
#     n = input()
#     A, B = [], []
#     flag = False
#     for a in n:
#         if a == '4':
#             A.append('2')
#             B.append('2')
#             flag = True
#         else:
#             A.append(a)
#             if flag:
#                 B.append('0')
#
#     print("Case #{}: {} {}".format(i, "".join(A), "".join(B)))
    # check out .format's specification for more formatting options

# t = int(input())  # read a line with a single integer
# for i in range(1, t + 1):
#     n = input()
#     s = input()
#     m = {'E': 'S', 'S': 'E'}
#     ans = [m[i] for i in s]
#     print("Case #{}: {}".format(i, "".join(ans)))

import math
t = int(input())  # read a line with a single integer
for T in range(1, t + 1):
    n, l = [int(s) for s in input().split(" ")]
    A = [int(s) for s in input().split(" ")]
    pset = set()
    for i in range(len(A) - 1):
        if A[i] == A[i + 1]:
            continue
        pset.add(math.gcd(A[i], A[i + 1]))
        pset.add(A[i] // math.gcd(A[i], A[i + 1]))
        pset.add(A[i + 1] // math.gcd(A[i], A[i + 1]))

    plist = list(pset)
    plist.sort()

    # d = {}
    d = {}
    for i, p in enumerate(plist):
        d[p] = chr(ord('A') + i)

    # for i, p in enumerate(plist):
    #     for j, q in enumerate(plist):
    #         d[p * q] = chr(ord('A') + i) + chr(ord('A') + j)

    ans = ['a' for i in range(len(A) + 1) ]
    k = -1
    last = -1
    for i in range(len(A) - 1):
        if A[i] != A[i + 1]:
            k = i + 1
            last = math.gcd(A[i], A[i + 1])
            ans[k] = d[last]

    back_last = last

    # print(d)

    for i in range(k + 1, len(ans)):
        last = A[i - 1] //  last
        ans[i] = d[last]

    last = back_last
    for i in range(k - 1, -1, -1):
        last = A[i] // last
        ans[i] = d[last]

    print("Case #{}: {}".format(T, "".join(ans)))

