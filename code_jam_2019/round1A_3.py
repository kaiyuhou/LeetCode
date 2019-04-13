
total = 0
def dfs(visited, count, path, x, y, n, m):
    visited[x][y] = 1

    if count == total:
        return True

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and i != x and j != y and (i - j) != (x - y) and (i + j) != (x + y):
                path.append((i, j))
                if dfs(visited, count + 1, path, i, j, n, m):
                    return True
                else:
                    path.pop()

    visited[x][y] = 0
    return False

t = int(input())
for T in range(1, t + 1):
    n, m = [int(s) for s in input().split(" ")]
    total = n * m

    if total <= 8:
        print("Case #{}: {}".format(T, "IMPOSSIBLE"))
        continue

    visited = []
    flag = False
    path = ()
    for i in range(n):
        visited.append([0 for j in range(m)])

    flag = False
    for i in range(n):
        if flag:
            break

        for j in range(m):
            path = [(i, j)]
            if dfs(visited, 1, path, i, j, n, m):
                flag = True
                break



    if flag:
        print("Case #{}: {}".format(T, "POSSIBLE"))
        for x, y in path:
            print("{} {}".format(x + 1, y + 1))
    else:
        print("Case #{}: {}".format(T, "IMPOSSIBLE"))
