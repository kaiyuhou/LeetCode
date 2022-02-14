import collections
T = int(input())
for _ in range(T):
    n = int(input())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))

    total = (sum(A) + sum(B)) // 2
  
    dp = collections.defaultdict(int)
    dp[-1, 0] = 1
    
    for i in range(n):
        for t in range(total + 1):
            if t >= A[i] and dp[i - 1, t - A[i]] != 0:
                dp[i, t] = 1
            if t >= B[i] and dp[i - 1, t - B[i]] != 0:
                dp[i, t] = 2
    
    newA = []
    newB = []
    idx = n - 1
    for t in range(total, -1, -1):
        if dp[idx, t] != 0:
            nxt_t = t
            while idx >= 0:
                if dp[idx, nxt_t] == 1:
                    newA.append(A[idx])
                    newB.append(B[idx])
                    nxt_t -= A[idx]
                else:
                    newA.append(B[idx])
                    newB.append(A[idx])
                    nxt_t -= B[idx]
                idx -= 1
            break
            
    def cal(A):
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                ans += (A[i] + A[j]) * (A[i] + A[j])
        return ans
    
    print(cal(newA) + cal(newB))
    
     
  
        
    # visited = set()
    # best_path = 0
    # best_t = 0

    # def dfs(cur, i, path):
        # global best_path, best_t 
#         
        # if cur > total:
            # return
#         
        # if (cur, i) in visited:
            # return
        # visited.add((cur, i))
#           
        # if i == n:
            # if cur > best_t:
                # best_path = tuple(path)
                # best_t = cur
            # return
#         
        # dfs(cur + A[i], i + 1, path + (1, ))
        # dfs(cur + B[i], i + 1, path + (2, ))
#         
    # def cal(A, B):
        # ans = 0
        # for i in range(n - 1):
            # for j in range(i + 1, n):
                # a = A[i] if best_path[i] == 1 else B[i]
                # b = A[j] if best_path[j] == 1 else B[j]
                # ans += (a + b) * (a + b)
        # return ans
#     
    # dfs(0, 0, tuple())
    # # print(best_path)
    # print(cal(A, B) + cal(B, A))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
                  
        
        
    
    
    
            
        
        
            
        
    
    


    # dp = {}
    # dp 
#     
    # AA = [A[0]]
    # BB = [B[0]]
#     
    # def cal(C, a):
        # ans = 0
        # for c in C:
            # ans += (c + a) * (c + a)
        # return ans
#     
    # for i in range(1, n):
        # a = A[i]
        # b = B[i]
        # if cal(AA, a) + cal(BB, b) <= cal(AA, b) + cal(BB, a):
            # AA.append(a)
            # BB.append(b)
            # ans += cal(AA, a) + cal(BB, b)
        # else:
            # AA.append(b)
            # BB.append(a)
            # ans += cal(AA, b) + cal(BB, a)
    # print(AA)
    # print(BB)
    # print(ans)
#     
        
        
        
    
