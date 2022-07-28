# Problem: Pile Partition
# Contest: CodeChef - CodeChef Starters 31 Division 3 (Rated)
# URL: https://www.codechef.com/START31C/problems/PARTGAME
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
    T = int(input())
    for _ in range(T):
        n = int(input())
        A = list(map(int, input().split()))
        if n == 2:
            if A[0] % 2 == 0 or A[1] % 2 == 0:
                print('Alice')
            else:
                print('Bob')
            continue
        
        alice = False
        for a in A:
            if a < n:
                continue
            if a <= (n - 1) * n:
                alice = True
                break
            # Bob win if a in 
            # (n-1)*n + 1 to (n-1)*n + (n-1)
            # Alice win if a in 
            # (n-1)*n + (n-1) + 1 to (n-1)*n + (n-1)*(n-1)
            # everytime, Alice can drop: n - 1 to (n-1)*(n-1)
            # 
            a_rest = a - (n - 1) * n
            n12 = (n - 1) * (n - 1)
            turn = (a_rest + (n12 - 1)) // n12
            rest = a_rest % n12
            # print(turn, rest)
            if turn % 2 == 1:
                if (n - 1) + 1 <= rest < n12 or rest == 0:
                    alice = True
                    break
            else:
                if 1 <= rest <= n - 1:
                    alice = True
                    break
        
        print('Alice' if alice else 'Bob')


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