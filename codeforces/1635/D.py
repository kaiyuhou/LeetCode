# Problem: D. Infinite Set
# Contest: Codeforces - Codeforces Round #772 (Div. 2)
# URL: https://codeforces.com/contest/1635/problem/D
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

import os
import sys
from io import BytesIO, IOBase
# sys.setrecursionlimit(100000)

def main():
    n, p = map(int, input().split())
    mod = 1000000007
    A = list(map(int, input().split()))
    A.sort()
    
    dp = [0] * (p + 3)
    dp_ans = [0] * (p + 3)
    
    dp[0] = 1
    dp_ans[0] = 1
    
    dp[1] = 1
    dp_ans[1] = 2
    
    dp[2] = 2
    dp_ans[2] = 4
    
    for i in range(3, p + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
        dp_ans[i] = (dp_ans[i - 1] + dp[i]) % mod
        
    # print(dp)
    # print(dp_ans)
    
    V = set()
    ans = 0
    for a in A:
        b = a
        flag = False
        while b:
            if b in V:
                flag = True
                break
            if b % 2 == 0 and b % 4 != 0:
                break
            
            if b % 4 == 0:
                b //= 4
            elif b % 2 == 1:
                b //= 2
        
        # print(a, flag)
        if not flag:
            V.add(a)
            len_a = len(bin(a)) - 2
            if len_a > p:
                continue
            ans += dp_ans[p - len_a]
            ans %= mod
            
    print(ans)
    
        
##################################
# region fastio

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
