# import sys
# for line in sys.stdin:
#     A = line.split()
#     print(int(A[0]) + int(A[1]))
#
# while True:
#     try:
#         a, b = map(int, input().strip().split())
#     except EOFError:
#         break
#
# a, b = map(int, input().split(" "))
# A = list(map(int, input().strip().split()))


# T = int(input())
# for _ in range(T):
#     a = int(input())
#     if a % 7 == 0:
#         print(a)
#         continue
#     a = str(a)
#     for i in range(0, 10):
#         if int(str(a[:-1]) + str(i)) % 7 == 0:
#             print(str(a[:-1]) + str(i))
#             break


# T = int(input())
# for _ in range(T):
#     S = input().strip()
#     one = sum([1 for c in S if c == '1'])
#     zero = len(S) - one
#     if one == zero:
#         print(one - 1)
#     else:
#         print(min(one, zero))

# T = int(input())
# for _ in range(T):
#     hc, dc = map(int, input().strip().split())
#     hm, dm = map(int, input().strip().split())
#     k, w, a = map(int, input().strip().split())
#
#     right = dm * (hm - 1)
#     A = hc + dm - 1
#     B = dc + k * w
#     if a == 0 or w == 0:
#         n = 1
#     else:
#         n = (a * B - A * w) // (2 * a * w)
#
#     case = [0, 1, k, k - 1, n, n - 1, n + 1, n - 2, n + 2]
#
#     for c in case:
#         if c > k or c < 0:
#             continue
#         if (A + c * a) * (B - c * w) > right:
#             print('YES')
#             break
#     else:
#         print('NO')

T = int(input())
for _ in range(T):
    hc, dc = map(int, input().strip().split())
    hm, dm = map(int, input().strip().split())
    k, w, a = map(int, input().strip().split())

    for i in range(k + 1):
        if (hc + i * a - 1) // dm + 1 > (hm - 1) // (dc + (k - i) * w):
            print('YES')
            break
    else:
        print('NO')





























