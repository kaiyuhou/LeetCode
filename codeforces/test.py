import itertools

A = [i + 1 for i in range(6)]

for B in itertools.permutations(A):
    # print(B, end=' ')
    last_ans = 0
    for i, a in enumerate(B):
        if i == 0:
            last_ans += 1
            continue
        if max(B[:i]) < a and min(B[i:]) > max(B[:i]):
            last_ans += 1
    # print(last_ans)

    n = 6
    min_arr = [0] * n
    last = n + 1
    for i in range(n - 1, -1, -1):
        if B[i] < last:
            last = B[i]
        min_arr[i] = last


    ans = 0
    for i, a in enumerate(B):
        if i == 0:
            ans += 1
            max_before = a
        if max_before < a and min_arr[i] > max_before:
            ans += 1
        max_before = max(max_before, a)
    if last_ans != ans:
        print('NO')
