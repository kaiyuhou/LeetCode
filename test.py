# T = int(input())
# for _ in range(T):
#     n = int(input())
#     A = list(map(int, input().strip().split()))
#
#     cur = A[1]
#     for a in A:
#         cur &= a
#
#     if cur == 0:
#         print('-1')
#     else:
#         ans = 1
#         while cur % 2 == 0:
#             cur //= 2
#             ans += 1
#         print(ans)

n, m, r = map(int, input().strip().split())
IN = []
for _ in range(n):
    IN.append(list(input().strip().split()))

ops = list(map(int, input().strip().split()))

A = [[1, 2],
     [4, 3]]
B = [[('0', '0'), 2],
     [3, ('')]]

for op in ops:
    if op == 1:
        A[0], A[1] = A[1], A[0]
        B[0], B[1] = B[1], B[0]
    elif op == 2:
        A[0][0], A[0][1] = A[0][1], A[0][0]
        A[1][0], A[1][1] = A[1][1], A[1][0]

        B[0][0], B[0][1] = B[0][1], B[0][0]
        B[1][0], B[1][1] = B[1][1], B[1][0]
    elif op == 3:
        A[0][0], A[0][1], A[1][0], A[1][1] = A[1][0], A[0][0], A[1][1], A[0][1]
        B[0][0], B[0][1], B[1][0], B[1][1] = B[1][0], B[0][0], B[1][1], B[0][1]
    elif op == 4:
        A[0][0], A[0][1], A[1][0], A[1][1] = A[0][1], A[1][1], A[0][0], A[1][0]
        B[0][0], B[0][1], B[1][0], B[1][1] = B[0][1], B[1][1], B[0][0], B[1][0]
    elif op == 5:
        A[0][0], A[0][1], A[1][0], A[1][1] = A[1][0], A[0][0], A[1][1], A[0][1]
    else:
        A[0][0], A[0][1], A[1][0], A[1][1] = A[0][1], A[1][1], A[0][0], A[1][0]

# print(IN)

C, D = [], []
for i in range(n):
    C.append(IN[i][:m//2])
    D.append(IN[i][m//2:])

# print(C, D)

E = {
    1: C[:n//2],
    2: D[:n//2],
    3: D[n//2:],
    4: C[n//2:]
}

# print(E)

for i in range(1, 5):
    e = E[i]



ans = []

b1 = E[A[0][0]]
b2 = E[A[0][1]]
hi = len(b1)


for i in range(hi):
    ans.append(b1[i] + b2[i])

b3 = E[A[1][1]]
b4 = E[A[1][0]]
hi = len(b3)

for i in range(hi):
    ans.append(b4[i] + b3[i])

print(ans)

# for a in ans:
#     print(' '.join(a))




























