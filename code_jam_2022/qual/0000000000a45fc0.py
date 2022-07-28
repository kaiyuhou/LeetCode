# Problem: Twisty Little Passages
# Contest: Google Coding Competitions - Qualification Round 2022 - Code Jam 2022
# URL: https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45fc0
# Memory Limit: 1024 MB
# Time Limit: 120000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
# sys.setrecursionlimit(100000)

import collections
import math
import random

from functools import lru_cache


def main():
    T = int(input())
    random.seed(T)
    for _ in range(T):
        N, K = map(int, input().split())
        r, c = map(int, input().split())
        if K >= N - 1:
            A = list(range(1, N + 1))
        else:
            A = random.sample(range(1, N + 1), K + 1)
            if r not in A:
                A = A[:-1]
        
        
            
        ans = []
        ans.append(c)
        for a in A:
            if a == r:
                continue
            print(f'T {a}')
            sys.stdout.flush()
            _, c = map(int, input().split())
            ans.append(c)
        
        if K >= N - 1:
            print(f'E {sum(ans) // 2}')
        else:
            ret = sum(ans) * N // ((K + 1) * 2)
            if ret < ((N  + 1)// 2):
                ret = (N  + 1)// 2
            print(f'E {ret}') 
        sys.stdout.flush()


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
