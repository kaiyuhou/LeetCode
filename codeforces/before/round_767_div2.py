# import sys
# for line in sys.stdin:
#     A = line.split()
#     print(int(A[0]) + int(A[1]))
#
# while True:
#     try:
#         a, b = map(int, input().strip().split())
#     except EOFError:
#         break
#
# a, b = map(int, input().split(" "))
# A = list(map(int, input().strip().split()))




def solve2(n, m):
    ans = []
    ball = 0

    half_n = (n + 1) // 2
    half_m = (m + 1) // 2
    dis = (n - half_n) + (m - half_m)
    turn = 0
    n_flag = n % 2 == 1
    m_flag = m % 2 == 1
    while ball < m * n:
        if turn >= half_m or turn >= half_n:
            turn = turn
            if turn == half_m:
                n_flag = False
            if turn == half_n:
                m_flag = False
        else:
            turn += 1

        this_turn = turn * 4
        if n_flag:
            this_turn -= 2
        if m_flag:
            this_turn -= 2
        if this_turn == 0:
            this_turn = 1

        next_ball = ball + this_turn
        while ball < m * n and ball < next_ball:
            ans.append(dis)
            ball += 1
        dis += 1
    # print(*ans)
    return ans


def solve1(n, m):
    ans = []
    for i in range(n):
        for j in range(m):
            ans.append(max(i + j, i + m - j - 1, j + n - i - 1, m - j - 1 + n - i - 1))
    ans.sort()
    # print(*ans)
    return ans

# T = int(input())
# for _ in range(T):
#     n, m = map(int, input().split(" "))

for i in range(2, 7):
    for j in range(2, 7):
        if solve1(i, j) != solve2(i, j):
            print(i, j)
            print(solve1(i, j))
            print(solve2(i, j))



















