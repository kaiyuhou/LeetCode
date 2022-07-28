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
        A, B = map(int, input().split())
        if A >= B:
            print(A - B)
            continue
        
        ans = B - A
        if A | B == B:
            ans = 1
        elif ((A + 1) | B == B) or ((B + 1) | A == (B + 1)):
            ans = min(ans, 2)           
        else: # B = 101000, A =100100, ans = 2 
            BS = bin(B)[2:]
            n = len(BS)
            AS = bin(A)[2:]
            AS = '0' * (n - len(AS)) + AS
            
            last_1_in_B = None  
            for i in range(n):
                if BS[i] == '1':
                    last_1_in_B = i

            # print(AS, BS, last_1_in_B)
            
            for i in range(0, last_1_in_B + 1):
                if BS[i] == '0' and AS[i] == '1':
                    # print(i)
                    break
                if i == last_1_in_B and AS[i] == '1':  # 00110 10100 3
                    break
            else:
                ans = min(ans, 2)
        
            ans = min(ans, 3)
        
        print(ans)
        
        


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
