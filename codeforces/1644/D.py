# Problem: D. Cross Coloring
# Contest: Codeforces - Educational Codeforces Round 123 (Rated for Div. 2)
# URL: https://codeforces.com/contest/1644/problem/D
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
# sys.setrecursionlimit(100000)

import collections
import math

from functools import lru_cache


def main():
    T = int(input())
    X = [-1] * (2 * 100000)
    Y = [-1] * (2 * 100000)
    for _ in range(T):
        n, m, k, q = map(int, input().split())
        ops = [list(map(int, input().split())) for _ in range(q)]
#         
        # X, Y = set(), set()
        # cnt = 0
        # for x, y in ops[::-1]:
            # if x not in X or y not in Y:
                # X.add(x)
                # Y.add(y)
                # cnt += 1
            # if len(X) == n or len(Y) == m:
                # break
#             
        # mod = 998244353
        # print(pow(k, cnt, mod))

        
        for i, (x, y) in enumerate(ops):
            X[x - 1] = i
            Y[y - 1] = i
        
        minx = q
        miny = q
        for x in X:
            minx = min(x, minx)
            if x == -1:
                break
        for y in Y:
            miny = min(x, miny)
            if y == -1:
                break
                       
            
        minx, miny = min(X), min(Y)
        mi = max(minx, miny)
                 
        dp = set()
        
        for x in X:
            if x != -1 and x >= mi:
                dp.add(x)
 
                    
        for y in Y:
            if y != -1 and y >= mi:
                dp.add(y)
        
        total = len(dp)
        mod = 998244353
        
        print(pow(k, total, mod))
        



##################################
# region fastio
# not my code
##################################


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

# endregion

if __name__ == "__main__":
    main()
