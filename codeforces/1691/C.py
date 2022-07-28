# Problem: C. Sum of Substrings
# Contest: Codeforces - CodeCraft-22 and Codeforces Round #795 (Div. 2)
# URL: https://codeforces.com/contest/1691/problem/C
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
        n, k = map(int, input().split())
        # n = int(input())
        S = input()
        # A = list(map(int, input().split()))
        C = collections.Counter(S)
        if C['1'] == 0:
            print(0) 
            continue
        
        ans = 0
        for i in range(n - 1):
            if S[i:i+2] == '01':
                ans += 1
            elif S[i:i+2] == '11':
                ans += 11
            elif S[i:i+2] == '10':
                ans += 10
                
        if C['1'] == 1:
            idx = S.index('1')
            if S[n - 1] != '1':
                to_right = n - 1 - idx
                if to_right <= k:
                    print(1)
                    continue
            if S[0] != '1' and S[n - 1] != '1':
                to_left = idx
                if to_left <= k:
                    print(10)
                    continue
            print(ans)
            continue
        
        if S[n - 1] != '1':
            idx = S[::-1].index('1')
            if idx <= k:
                k -= idx
                ans -= 10
        if S[0] != '1':
            idx = S.index('1')
            if idx <= k:
                ans -= 1
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
