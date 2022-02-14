import collections
from functools import lru_cache
from sys import stdin, stdout
input = stdin.readline
print = lambda s: stdout.write(str(s) + '\n')
 

from types import GeneratorType
 
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
 
    return wrappedfunc

def main():
    n = int(input())
    H = list(map(int, input().split()))
    
    G = collections.defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    
    root = H.index(max(H))
    
    ans = 0
    
    @bootstrap
    def dfs(u, p):
        nonlocal ans
        
        mx1 = 0
        mx2 = 0
        
        for v in G[u]:
            if v != p:
                cur = dfs(v, u)
                if cur > mx1:
                    cur, mx1 = mx1, cur
                if cur > mx2:
                    cur, mx2 = mx2, cur
        if p != -1:
            diff = max(0, H[u] - mx1)
            ans += diff
            mx1 += diff
        else:
            ans += max(0, H[u] - mx1) + max(0, H[u] - mx2)
        
        yield mx1
    
    dfs(root, -1)        
    print(ans)
        
main()
    


# def dfs(now, fa):
    # global ans
#     
    # max_w = 0
    # if now != root:
        # for u in G[now]:
            # if u == fa:
                # continue
            # max_w = max(max_w, dfs(u, now))
        # if max_w < H[now]:
            # ans += H[now] - max_w
        # return max(max_w, H[now])
    # else:
        # if len(G[now]) == 1:
            # u = G[now][0]
            # max_w = max(max_w, dfs(u, now))
            # ans += 2 * H[now] - max_w
        # else:
            # s = []
            # for u in G[now]:
                # s.append(dfs(u, now))
            # s.sort()
            # ans += 2 * H[now] - (s[-1] + s[-2])
        # return 0    
#     
# dfs(root, root)

        
    
     