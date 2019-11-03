
# class Solution:
#     def maxLength(self, arr) -> int:
#         ans = 0
#
#         arr1 = []
#         for a in arr:
#             if len(set(list(a))) == len(a):
#                 arr1.append(a)
#         arr = arr1
#
#         N = len(arr)
#         dp = [set() for i in range(N)]
#         for i in range(N - 1):
#             for j in range(i + 1, N):
#                 if len(set(list(arr[i] + arr[j]))) != len(arr[i] + arr[j]):
#                     dp[i].add(j)
#                     dp[j].add(i)
#         # print(dp)
#
#         for i in range(1, 2 ** N):
#             S = set()
#             cur = 0
#             for j in range(N):
#                 if i & (2 ** j):
#                     if j in S: break
#                     S = S.union(dp[j])
#                     cur += len(arr[j])
#             ans = max(ans, cur)
#         return ans
#
# s = Solution()
# arr = ["un","iq","ue"]
# # arr = ["cha","r","act","ers"]
# # arr = ["abcdefghijklmnopqrstuvwxyz"] * 16
# arr = ["boyigtseknrzdw","zonypbkfqma","izyufqpgmoek","xkmvl","agrtujmhyzdseck","vmhsigowfqejuap","bqxaueskmdyifjvptro","sztlidyoqjfrkbg","ndwaijysqfbzh","mnazfdiph","bha","vgfcjwpieunm","jagonvhpbkq","pfowzdtsemrjgahc","yinfdcgwljs"]
# print(s.maxLength(arr))


class Solution:
    def circularPermutation(self, n: int, start: int):
        S = set()
        N = 2 ** n
        dp = [0] * n
        ans = [start]
        for i in range(n):
            if start & (2 ** i):
                dp[i] = 1
        S.add(tuple(dp))

        def F(A):
            ans = 0
            for i in range(n):
                if A[i] == 1:
                    ans += 2 ** i
            return ans

        for i in range(N - 1):
            for j in range(n):
                dp[j] = 1 - dp[j]
                if tuple(dp) in S:
                    dp[j] = 1 - dp[j]
                else:
                    S.add((tuple(dp)))
                    ans.append(F(dp))
                    break
        return ans

s = Solution()
print(s.circularPermutation(4, 0))


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        A = [] * 15
        A[1] = [1]
        A[2] = [2, 1]
        A[3] = [3, 3, 1]
        A[4] = [4, 2, 4, 1]
        A[5] = [5, 4, 4, 5, 1]
        A[6] = [6, 3, 2, 3, 5, 1]
        A[7] = [7, 5, 5, 5, 5, 5, 1]
        A[8] = [8, 4, 5, 2, 5, 4, 7, 1]
        A[9] = [9, 6, 3, 6, 6, 3, 6, 7, 1]
        A[10] = [10, 5, 6, 4, 2, 4, 6, 5, 6, 1]
        A[11] = [11, 7, 6, 6, 6, 6, 6, 6, 7, 6, 1]
        A[12] = [12, 6, 4, 3, 6, 2, 6, 3, 4, 5, 7, 1]
        A[13] = [13, 8, 7, 7, 6, 6, 6, 6, 7, 7, 6, 7, 1]

        if n < m:
            n, m = m ,n
        return A[n][m]





