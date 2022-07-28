# Problem: Magical Modulo
# Contest: CodeChef - February Lunchtime 2022 Division 4
# URL: https://www.codechef.com/LTIME105D/problems/MAGICMOD
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
        small = set()
        large = set()
        
        ans = True
        for a in A:
            if a <= n:
                if a not in small:
                    small.add(a)
                else:
                    ans = False
                    break
            else:
                if a not in large:
                    large.add(a)
                else:
                    ans = False
                    break
        
        
        if not ans:
            print('NO')
            continue
            
        if len(small) == n:
            print(f'YES {n + 1}')
            continue
            
        
        small_list = list(small)
        wait = len(small) + 1
        for i, a in enumerate(small):
            if a != i + 1:
                wait = i + 1
                break
                
        first_large = small 
        
        
        
        
        
        




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
