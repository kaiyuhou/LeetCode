# # class Solution:
# #     def validMountainArray(self, A):
# #         """
# #         :type A: List[int]
# #         :rtype: bool
# #         """
# #         l = len(A)
# #         if l < 3:
# #             return False
# #
# #         m = max(A)
# #         index = A.index(m)
# #
# #         if index == l - 1 or index == 0:
# #             return False
# #
# #
# #         for i in range(index - 1):
# #             if A[i] >= A [i + 1]:
# #                 # print("in 1")
# #                 return False
# #
# #         for i in range(index, l - 1):
# #             if A[i] <= A[i + 1]:
# #                 return False
# #
# #         return True
# #
# #
# # s = Solution()
# # # A = [3, 5 ,3]
# # A = [9,8,7,6,5,4,3,2,1,0]
# # print(s.validMountainArray(A))
# #
#
#
# class Solution:
#     def minDeletionSize(self, A):
#         """
#         :type A: List[str]
#         :rtype: int
#         """
#         N = len(A)
#         if N == 1:
#             return 0
#
#         M = len(A[0])
#
#         ans = 0
#         for j in range(M):
#             for i in range(N - 1):
#                 if ord(A[i][j]) > ord(A[i + 1][j]):
#                     ans += 1
#                     break
#
#         return ans
#
# s = Solution()
# # A = ["cba","daf","ghi"]
# # A = ["a","b"]
# A = ["zyx","wvu","tsr"]
# print(s.minDeletionSize(A))


# class Solution:
#     def diStringMatch(self, S):
#         """
#         :type S: str
#         :rtype: List[int]
#         """
#         ans = []
#         l = 0
#         r = len(S)
#         for i in S:
#             if i == 'I':
#                 ans.append(l)
#                 l += 1
#             if i == 'D':
#                 ans.append(r)
#                 r -= 1
#
#         ans.append(l)
#
#         return  ans
#
# s = Solution()
# # S = "IDID"
# # S = "III"
# # S = "DDI"
# S = 'D'
# print(s.diStringMatch(S))


class Solution:
    def get_l_r(self, a, b):
        n = min(len(a), len(b))
        n -= 1
        l = 0
        r = 0
        la = len(a)
        lb = len(b)

        i = n
        while i > 0:
            if a[la - i : ] == b[ : i]:
                l = i
                break
            i -= 1

        i = n
        while i > 0:
            if b[lb - i :] == a [ : i]:
                r = i
                break
            i -= 1

        return l, r

    def get_Ans(self, A):
        dp = {}
        n = len(A)

        if n == 1:
            return A[0]


        for i in range(n - 1):
            for j in range(i + 1, n):
                l, r = self.get_l_r(A[i], A[j])
                dp[i, j] = (l, r)
                dp[j ,i] = (r, l)



        if n == 2:
            l, r = dp[0, 1]
            a = A[0] + A[1][l:]
            b = A[1] + A[0][r:]
            if len(a) < len(b):
                return a
            else:
                return b


        max_cur = -1
        max_l = -1
        max_r = -1
        maxn = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                for k in range(n):
                    if i == k or j == k:
                        continue

                    l = dp[i, j][0]
                    r = dp[i, k][1]
                    if l + r > maxn:
                        max_cur = i
                        max_l = j
                        max_r = k
                        maxn = l + r

        if maxn == 0:
            return "".join(A)


        new_str = str(A[max_cur])
        a = str(A[max_cur])


        b = ""
        if (max_l != -1):
            b = str(A[max_l])
            l, r = dp[max_cur, max_l]
            new_str = new_str + b[l:]


        c = ""
        if (max_r != -1):
            c = str(A[max_r])
            A.remove(c)
            l, r = dp[max_r, max_cur]
            new_str = c + new_str[l:]

        A.remove(a)
        if b != "":
            A.remove(b)

        A.append(new_str)
        # print(a, b, c)
        # print(new_str)


        return self.get_Ans(A)

    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        n = len(A)

        ans = ""
        remove_list = []
        for a in A:
            if len(a) == 1:
                remove_list.append(a)

        for a in remove_list:
            A.remove(a)
            ans += a
            n -= 1

        if n == 0:
            return ans

        return self.get_Ans(A) + ans



s= Solution()
# A = ["catg","ctaagt","gcta","ttca","atgcatc"]
# A = ["ift","efd","dnete","tef","fdn"]
# A = ["alex","loves","leetcode"]
A = ["abcde","xyzab"]
print(s.shortestSuperstring(A))
print(len(s.shortestSuperstring(A)))
