# Problem: E. Breaking the Wall
# Contest: Codeforces - Codeforces Round #786 (Div. 3)
# URL: https://codeforces.com/contest/1674/problem/E
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
    T = 1
    for _ in range(T):
        # a, b = map(int, input().split())
        n = int(input())
        A = list(map(int, input().split()))
        ans = A[0] + A[1]
        for i in range(n - 1):
            a = A[i]
            b = A[i + 1]
            a, b = max(a, b), min(a, b)
            if b * 2 <= a:
                ans = min((a + 1) // 2, ans)
            else:
                x1 = int(((a + b) / 3 + a - b) / 2)
                x2 = max(0, x1 - 1)
                x3 = x1 + 1
                for x in (x1, x2, x3):
                    ta, tb = a, b
                    ta -= 2 * x
                    tb -= x
                    cur = (tb + 1) // 2
                    ta -= cur
                    cur += (ta + 1) // 2
                    ans = min(ans, x + cur)
            if i > 0:
                a = min(A[i - 1], A[i + 1])
                b = max(A[i - 1], A[i + 1])
                cur = a
                b -= a
                cur += (b + 1) // 2              
                ans = min(ans, cur)
        A.sort()
        cur = (A[0] + 1) // 2 + (A[1] + 1) // 2
        ans = min(ans, cur)
        print(ans)

##################################
# Region FastIO
# * code below is for accelerating IO in Python
# * not directly related to the solution
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
