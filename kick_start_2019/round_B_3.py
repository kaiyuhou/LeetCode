from math import *
t = int(input())
for T in range(1, t + 1):
    n, S = [int(s) for s in input().split(" ")]
    A = [int(s) for s in input().split(" ")]
    dp = [0 for _ in range(n + 1)]
    start = [1 for _ in range(n + 1)]
    record = {}
    for i in range(1, n + 1):
        # print(i)
        # print(dp)
        # print(start)

        if A[i - 1] not in record.keys():
            record[A[i - 1]] = 1
            start[i] = start[i - 1]
            dp[i] = dp[i - 1] + 1
            continue

        if record[A[i - 1]] < S:
            record[A[i - 1]] += 1
            dp[i] = dp[i - 1] + 1
            start[i] = start[i - 1]
            continue

        if record[A[i - 1]] > S:
            record[A[i - 1]] += 1
            dp[i] = dp[i - 1]
            start[i] = start[i - 1]
            continue

        record[A[i - 1]] = S + 1
        new_record = dict(record)
        new_record2 = dict(record)
        dp[i] = dp[i - 1] - S
        start[i] = start[i - 1]

        # to right
        new_record[A[i - 1]] += 1
        L = start[i - 1]

        while L < i - 1:
            new_record[A[L - 1]] -= 1
            L += 1
            if new_record[A[i - 1]] <= S:
                break

        cur = 0
        for k in new_record.keys():
            if new_record[k] <= S:
                cur += new_record[k]
        if cur >= dp[i]:
            dp[i] = cur
            start[i] = L
            record = new_record

        # to left
        L = start[i - 1]
        while L > 0:
            if new_record2[A[L - 1]] < S or new_record2[A[L - 1]] > S:
                new_record2[A[L - 1]] += 1
            else:
                break
            L -= 1

        cur = 0
        for k in new_record2.keys():
            if new_record2[k] <= S:
                cur += new_record2[k]
        if cur >= dp[i]:
            dp[i] = cur
            start[i] = L
            record = new_record2

    print("Case #{}: {}".format(T, max(dp)))
