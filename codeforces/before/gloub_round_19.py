T = int(input())
for _ in range(T):
    n = int(input())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))

    total = (sum(A) + sum(B)) // 2

    visited = set()
    best_path = 0
    best_t = 0

    def dfs(cur, i, path):
        global best_path, best_t

        if cur > total:
            return

        if (cur, i) in visited:
            return
        visited.add((cur, i))

        if i == n:
            if cur > best_t:
                best_path = tuple(path)
                best_t = cur
            return

        dfs(cur + A[i], i + 1, path + (1, ))
        dfs(cur + B[i], i + 1, path + (2, ))

    def cal(A, B):
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                a = A[i] if best_path[i] == 1 else B[i]
                b = B[j] if best_path[j] == 1 else A[j]
                ans += (a + b) * (a + b)
        return ans

    dfs(0, 0, tuple())
    print(cal(A, B) + cal(B, A))