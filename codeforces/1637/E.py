import collections

T = int(input())
for _ in range(T):
    n, m = list(map(int, input().strip().split()))
    A = list(map(int, input().strip().split()))
    
    V = set()

    for i in range(m):
        a, b = list(map(int, input().strip().split()))
        V.add((a, b))
        V.add((b, a))
    
    C = collections.Counter(A)
    cnt_lists = collections.defaultdict(list)
    for k, v in C.items():
        cnt_lists[v].append(k)
    for k, v in cnt_lists.items():
        v.sort(reverse=True)
    cnt_array = list(cnt_lists.keys())

    
    # print(cnt_lists[2])
    
    
    ans = 0
    for i, cnt_x in enumerate(cnt_array):
        for x in cnt_lists[cnt_x]:
            for j in range(i + 1):
                cnt_y = cnt_array[j]
                for y in cnt_lists[cnt_y]:
                    if x != y and (x, y) not in V:
                        ans = max(ans, (cnt_x + cnt_y) * (x + y))
                        break
    print(ans) 
    
    
    
    
    
    # D = []
    # for k, v in C.items():
        # D.append((k * v, k, v))
    # D.sort(reverse=True)
# 
    # t = 4 * (10 ** 5)
    # q = [(0, 1)]
    # ans = 0
    # visited = set()
    # visited.add((0, 1))
# 
    # N = len(D)
# 
    # def append_next(a, b):
        # if a == b:
            # return 
        # if a >= N or b >= N:
            # return
        # if (a, b) in visited:
            # return
        # visited.add((a, b))
        # q.append((a, b))
#         
#         
    # # print(V)
    # idx = 0
# 
    # while idx < len(q) and t > 0:
        # t -= 1
        # i, j = q[idx]
        # idx += 1
        # if (D[i][1], D[j][1]) not in V:
            # cur = D[i][0] + D[j][0] + D[i][1] * D[j][2] + D[j][1] * D[i][2]
            # ans = max(ans, cur)
            # # print(ans, D[i], D[j])
        # append_next(i + 1, j)
        # append_next(i, j + 1)    
#         
#     
    # print(ans)
    
    
            
            
            
            
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    