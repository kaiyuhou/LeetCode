# Problem: D. Max GEQ Sum
# Contest: Codeforces - CodeCraft-22 and Codeforces Round #795 (Div. 2)
# URL: https://codeforces.com/contest/1691/problem/D
# Memory Limit: 256 MB
# Time Limit: 1500 ms
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
    for _ in range(T):
        # a, b = map(int, input().split())
        n = int(input())
        A = list(map(int, input().split()))
        ans = True
        for i in range(n - 1):
            if A[i] > 0 and A[i + 1]> 0:
                print('NO')
                ans = False
        if not ans:
            continue

        B = [A[0]]
        for i in range(1, n):
            if A[i] <= 0 and B[-1] <= 0:
                B[-1] += A[i]
            else:
                B.append(A[i])
        
        if B[0] <= 0:
            B = B[1:]
        if B[-1] <= 0
            B = B[:-1]
            
        C = []
        for i, b in enumerate(B):
            
            
        
            


        
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

        # stack = []
        # for b in B:
            # if len(stack) == 0:
                # if b <= 0:
                    # continue
                # else:
                    # stack.append(b)
            # else:
                # b > 0:

        if ans:
            print('YES')
        else:
            print('NO')
        

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
