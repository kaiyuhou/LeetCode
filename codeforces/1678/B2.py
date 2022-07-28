# Problem: B2. Tokitsukaze and Good 01-String (hard version)
# Contest: Codeforces - Codeforces Round #789 (Div. 2)
# URL: https://codeforces.com/contest/1678/problem/B2
# Memory Limit: 256 MB
# Time Limit: 1000 ms
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
        S = input()

        def f(S):
            n = len(S)
            last = S[0]
            cnt = 1
            A = []
            C = []
            for i in range(1, n):
                if last != S[i]:
                    A.append(cnt)
                    C.append(last)
                    cnt = 1
                    last = S[i]
                else:
                    cnt += 1
            A.append(cnt)
            C.append(last)
            # print(A)
            
            ans = 0
            seg = 0
            last_c = '2'
            
            
            
            for i in range(len(A) - 1):
                if A[i] == 0:
                    continue
                if A[i] == 1:
                    if C[i] == last_c:
                        A[i] = 0
                        A[i + 1] -= 1
                        ans += 1
                    else:
                        A[i] = 0
                        A[i + 1] += 1
                        ans += 1
                    continue
                
                if last_c != C[i]:
                    seg += 1
                    last_c = C[i]
                
    
                if A[i] % 2 == 1:
    
                    A[i] += 1
                    if A[i + 1] == 1:
                        ans += 1
                        A[i + 1] = 0
                    elif A[i + 1] == 2:
                        ans += 2
                        A[i + 1] = 0
                        A[i + 2] += 1
                    else:
                        ans += 1
                        A[i + 1] -= 1
                # print(A)
            if A[-1] > 0:
                if last_c != C[-1]:
                    seg += 1
            return ans, seg
        ans, seg1 = f('1111' + S)
        ans, seg2 = f('0000' + S)
        # seg2 = 20
        print(ans, min(seg1, seg2))


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
