# Problem: D. Big Brush
# Contest: Codeforces - Codeforces Round #771 (Div. 2)
# URL: https://codeforces.com/contest/1638/problem/D
# Memory Limit: 256 MB
# Time Limit: 3000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

import collections
import math

from functools import lru_cache


import os
import sys
from io import BytesIO, IOBase


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")





def main():
    n, m = map(int, input().split())
    G = []
    for i in range(n):
        G.append(list(map(int, input().split())))
    
    coner = ((0, 0), (0, 1), (1, 0), (1, 1))
    nxt = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    
    ans = []
    possible = []
    visited = [[0] * m for _ in range(n)]
    rest = n * m
    
    def check(a, b):
        cur = 0
        for x, y in coner:
            if cur == 0:
                cur = G[a + x][b + y]
            elif G[a + x][b + y] and cur != G[a + x][b + y]:
                return False
        return cur
    
    def color(a, b):
        nonlocal rest
    
        color = 0
        for x, y in coner:
            if G[a + x][b + y] != 0:
                color = G[a + x][b + y]
                G[a + x][b + y] = 0
                rest -= 1

        if color:
            ans.append((a + 1, b + 1, color))
            
            for x, y in nxt:
                i = a + x
                j = b + y
                if 0 <= i < n - 1 and 0 <= j < m - 1 and not visited[i][j] and check(i, j):
                    possible.append((i, j))
                    visited[i][j] = 1
        
    for i in range(n - 1):
        for j in range(m - 1):
            if not visited[i][j] and check(i, j):
                color(i, j)
    
    while len(possible) > 0:
        if rest == 0:
            break
        color(*possible.pop())
    
    if rest == 0:
        ans.reverse()
        print(len(ans))
        for a in ans:
            print(*a)
    else:
        print(-1)


for _ in range(1):
    main()