def solve(T):
    A = [[8, 9, 1, 13],
         [3, 12, 7, 5],
         [0, 2, 4, 11],
         [6, 10, 15, 14]]

    if T == 1:
        return A



    N = T * 4
    ans = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # if i % 4 == 0 and j % 4 == 0:
            #     G = 0
            #     a, b = i, j
            #     for k in range(1, T):
            #         G += A[a % 4][b % 4] * (16 ** k)
            for k in range(T):
                ans[i][j] += A[a % 4][b % 4] * (16 ** k)
                a, b = a // 4, b // 4
    return ans

if __name__ == "__main__":

    N = int(input())
    ans = solve(N // 4)
    print(ans)


