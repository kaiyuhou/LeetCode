import os
import sys
from io import BytesIO, IOBase

import collections

def main():
    T = int(input())
    for _ in range(T):
        n, m = list(map(int, input().strip().split()))
        A = list(map(int, input().strip().split()))
        # bad = [tuple(map(int, input().split())) for _ in range(m)]
        # V = set(bad)
        V = set()
    
        for i in range(m):
            a, b = list(map(int, input().split()))
            V.add((a, b))
                     
        C = collections.Counter(A)
        cnt_lists = collections.defaultdict(list)
        for k, v in C.items():
            cnt_lists[v].append(k)

        for k, v in cnt_lists.items():
            v.sort(reverse=True)

        cnt_array = list(cnt_lists.keys())
        cnt_array.sort()
        
        
        ans = 0
        for i, cnt_x in enumerate(cnt_array):
            for x in cnt_lists[cnt_x]:
                for j in range(i + 1):
                    cnt_y = cnt_array[j]
                    for y in cnt_lists[cnt_y]:
                        if x != y and (x, y) not in V and (y, x) not in V:
                            ans = max(ans, (cnt_x + cnt_y) * (x + y))
                            break
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

main()
            
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    