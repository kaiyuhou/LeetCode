# class SubtractionGenerator:
#     def generate(self, result):
#         n = len(str(result))
#         y = 10 ** n - 1
#         x = y + result
#         return (x, y)


class HopscotchCounting:
    def count(self, n):
        dp = {}
        dp[1, 1] = 1
        dp[1, 2] = 0
        dp[2, 1] = 1
        dp[2, 2] = 1
        mod = 1000000007
        for i in range(3, n + 1):
            dp[i, 1] = (dp[i - 1, 1] + dp[i - 1, 2]) % mod
            dp[i, 2] = dp[i - 2, 1]
        # print(dp)
        return (dp[n, 1] + dp[n, 2]) % mod
#
n = 998768
S = HopscotchCounting()
print(S.count(n))

# def computeGCD(x, y):
#     while(y):
#         x, y = y, x % y
#     return x
#
#
# class ExactRate():
#     def getLongest(self, n, seed, threshold, S, F):
#         A = [0] * (n + 1)
#         last = (seed * 1103515245 + 12345) % (2 ** 31)
#         A[1] = 1 if (last > threshold) else 0
#         for i in range(2, n + 1):
#             last = (last * 1103515245 + 12345) % (2 ** 31)
#             A[i] = A[i - 1] + 1 if (last > threshold) else A[i - 1]
#
#         G = computeGCD(S, F)
#         S //= G
#         F //= G
#
#         if S + F > n or S > A[n] or F > n - A[n]:
#             return 0, 0
#
#         ratio = n // (S + F)
#         for T in range(ratio, 0, -1):
#             L = (S + F) * T
#             cur_S = S * T
#             cur_F = F * T
#             if cur_S > A[n] or cur_F > n - A[n]:
#                 continue
#             lo = 0
#             hi = lo + L
#             while hi < n + 1:
#                 if A[hi] - A[lo] == cur_S:
#                     return (lo, hi)
#                 lo += 1
#                 hi += 1
#         return 0, 0


















