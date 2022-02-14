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


def get_mask(word):
    return sum(1 << (ord(c) - ord("a")) for c in word)


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.weight = [1 for _ in range(n)]

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            if self.weight[pu] < self.weight[pv]:
                self.parent[pu] = pv
                self.weight[pv] = self.weight[pu] + self.weight[pv]
            else:
                self.parent[pv] = pu
                self.weight[pu] = self.weight[pu] + self.weight[pv]


# T = int(input())
# for _ in range(T):
#     n, k = map(int, input().split())
#     s = input()
#
#     if k == 0:
#         print(1)
#         continue
#     if s == s[::-1]:
#         print(1)
#         continue
#     print(2)

# T = int(input())
# for _ in range(T):
#     n, x, y = map(int, input().split())
#     A = map(lambda a: int(a) % 4, input().split())
#     x = x % 4
#     cur = [0] * 4
#     cur[x] = 1
#     for i, a in enumerate(A):
#         nxt = [0] * 4
#         for j, f in enumerate(cur):
#             if f:
#                 nxt[(j + a) % 4] = 1
#                 nxt[j ^ a] = 1
#         cur = nxt
#     if cur[y % 4] == 1:
#         print('Alice')
#     else:
#         print('Bob')

# T = int(input())
# for _ in range(T):
#     n, k = map(int, input().split())
#     if k == 1:
#         print('YES')
#         for i in range(n):
#             print(i + 1)
#         continue
#     if n % 2 == 1:
#         print('NO')
#         continue
#     print('YES')
#     i = 1
#     for _ in range(n // 2):
#         for _ in range(k - 1):
#             print(i, end=' ')
#             i += 2
#         print(i)
#         i += 2
#     i = 2
#     for _ in range(n // 2):
#         for _ in range(k - 1):
#             print(i, end=' ')
#             i += 2
#         print(i)
#         i += 2


from sys import *
import collections

T = int(input())
for _ in range(T):
    n = int(input())
    order = []
    for i in range(3, n + 1):
        print(f'? 1 2 {i}')
        stdout.flush()
        resp = int(input())
        order.append(resp)

    if n == 4 and order[0] == order[1]:
        print(f'? 1 3 4')
        stdout.flush()
        resp1 = int(input())

        print(f'? 2 3 4')
        stdout.flush()
        resp2 = int(input())

        if resp1 == resp2:
            if resp1 < order[0]:
                print(f'! 1 2')
            else:
                print(f'! 3 4')
        else:
            print(f'! 1 2')
        stdout.flush()
        continue

    C = collections.Counter(order)
    besto = max(order)
    if C[besto] >= 2:
        print(f'! 1 2')
        stdout.flush()
        continue
    if C[besto] == 2:
        print(f'!', end='')
        for i, a in enumerate(order):
            if a == besto:
                print(f' {i + 3}', end='')
        print()
        stdout.flush()
        continue

    best_idx = order.index(besto) + 3
    order = []
    for i in range(2, n + 1):
        if i == best_idx:
            order.append(0)
            continue
        print(f'? 1 {best_idx} {i}')
        stdout.flush()
        resp = int(input())
        order.append(resp)

    C = collections.Counter(order)
    besto = max(order)
    if C[besto] >= 2:
        print(f'! 1 {best_idx}')
        stdout.flush()
        continue
    nxt_idx = order.index(besto) + 2
    print(f'! {nxt_idx} {best_idx}')
    stdout.flush()
    continue











































































