# Problem: D. Tournament Countdown
# Contest: Codeforces - Codeforces Round #812 (Div. 2)
# URL: https://codeforces.com/contest/1713/problem/D
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
    MOD = 1000000007
    T = int(input())
    def Q(a, b):
        print(f'? {a} {b}')
        sys.stdout.flush()
        return int(input())
    
    
    for _ in range(T):
        # a, b = map(int, input().split())
        n = int(input())
        A = [i + 1 for i in range(2 ** n)]
        while n >= 2:
            n -= 2
            B = [-1 for i in range(2 ** n)]
            to_q = []
            for i in range(2 ** n):
                to_q.append(f'? {A[i * 4 + 0]} {A[i * 4 + 2]}')
            print('\n'.join(to_q))
            sys.stdout.flush()
            to_q2 = []
            rets = []
            for i in range(2 ** n):
                ret1 = int(input())
                rets.append(ret1)
                if ret1 == 0:
                    to_q2.append(f'? {A[i * 4 + 1]} {A[i * 4 + 3]}')
                elif ret1 == 1:
                    to_q2.append(f'? {A[i * 4 + 0]} {A[i * 4 + 3]}')
                elif ret1 == 2:
                    to_q2.append(f'? {A[i * 4 + 1]} {A[i * 4 + 2]}')
            print('\n'.join(to_q2))
            sys.stdout.flush()
            for i in range(2 ** n):
                ret1 = rets[i]
                ret2 = int(input())
                if ret1 == 0:
                    B[i] = A[i * 4 + 1] if ret2 == 1 else A[i * 4 + 3]
                elif ret1 == 1:
                    B[i] = A[i * 4 + 0] if ret2 == 1 else A[i * 4 + 3]
                elif ret1 == 2:
                    B[i] = A[i * 4 + 1] if ret2 == 1 else A[i * 4 + 2]
                # a1 = A[i * 4 + 0]
                # a2 = A[i * 4 + 1]
                # a3 = A[i * 4 + 2]
                # a4 = A[i * 4 + 3]
                # ret1 = Q(a1, a3)
                # if ret1 == 0:
                    # ret2 = Q(a2, a4)
                    # B[i] = a2 if ret2 == 1 else a4
                # elif ret1 == 1:
                    # ret2 = Q(a1, a4)
                    # B[i] = a1 if ret2 == 1 else a4
                # elif ret1 == 2:
                    # ret2 = Q(a2, a3)
                    # B[i] = a2 if ret2 == 1 else a3
                # else:
                    # return -1          
            A = B
        if n == 1:
            ret = Q(A[0], A[1])
            ans = A[0] if ret == 1 else A[1]
            print(f'! {ans}')
            sys.stdout.flush()
        else:
            print(f'! {A[0]}')
            sys.stdout.flush()


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
