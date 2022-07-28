# Problem: F. Desktop Rearrangement
# Contest: Codeforces - Codeforces Round #786 (Div. 3)
# URL: https://codeforces.com/contest/1674/problem/F
# Memory Limit: 256 MB
# Time Limit: 3000 ms
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
        n, m, q = map(int, input().split())
        A = []
        cnt = 0
        for _ in range(n):
            row = input()
            A.append(list(row))
            cnt += row.count('*')
        if cnt == 0:
            px, py = -1, -1
        else:
            py = (cnt - 1) // n
            px = cnt - (py * n) - 1 
        
        def in_used(a, b):
            if b < py:
                return True
            if b == py and a <= px:
                return True
            return False

        def next_p(px, py):
            if px == -1:
                return 0, 0
            px += 1
            if px == n:
                py += 1
                px = 0
            return px, py
            
        def pre_p(px, py):
            if (px, py) == (0, 0):
                return -1, -1
            px -= 1
            if px == -1:
                py -= 1
                px = n - 1
            return px, py
   
                    
        used = 0
        for i in range(n):
            for j in range(m):
                if in_used(i, j) and A[i][j] == '*':
                    used += 1 

        # print(px, py)
        for _ in range(q):
            x, y = map(int, input().split())
            x -= 1
            y -= 1
            if A[x][y] == '.': # add
                px, py = next_p(px, py)
                cnt += 1
                if in_used(x, y):
                    used += 1
                if (x, y) != (px, py) and A[px][py] == '*':
                    used += 1
                # print('cnt, used', cnt, used)
                print(cnt - used)
                A[x][y] = '*'
            else: # remove
                cnt -= 1
                if in_used(x, y):
                    used -= 1
                A[x][y] = '.'
                if used > 0 and A[px][py] == '*':
                    used -= 1
                px, py = pre_p(px, py)
                # print('2 cnt, used', cnt, used)
                print(cnt - used)
                
            # print(px, py)


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
