# class Solution:
#     def isAlienSorted(self, words, order):
#         """
#         :type words: List[str]
#         :type order: str
#         :rtype: bool
#         """
#
#         o = {}
#         for i in range(26):
#             o[order[i]] = i
#
#         if len(words) == 1:
#             return True
#
#         pre_word = words[0]
#         for i in range(len(words) -1):
#             word = words[i + 1]
#
#             l = min(len(pre_word), len(word))
#             for j in range(l):
#                 if o[pre_word[j]] > o[word[j]]:
#                     return False
#                 if o[pre_word[j]] < o[word[j]]:
#                     break
#                 else:
#                     if j == len(word) - 1 and len(word) < len(pre_word):
#                         return False
#
#             pre_word = words[i + 1]
#
#
#         return True
#
#
#
# s = Solution()
# # words = ["hello","leetcode"]
# # order = "hlabcdefgijkmnopqrstuvwxyz"
# # words = ["apple","app"]
# # order = "abcdefghijklmnopqrstuvwxyz"
# # words = ["word","world","row"]
# # order = "worldabcefghijkmnpqstuvxyz"
# words = ["aa", "ab", "aa"]
# order = "abcdefghijklmnopqrstuvwxyz"
#
# print(s.isAlienSorted(words, order))


# class Solution:
#     def check(self, A):
#         A.sort()
#         l = len(A)
#
#         dp = [0 for i in range(100001)]
#         for a in A:
#             dp[a] += 1
#
#
#         for i in range(l-1, -1, -1):
#             if dp[A[i]] == 0:
#                 continue
#
#             if A[i] % 2 == 1:
#                 return False
#
#             dp[A[i]] -= 1
#
#             if dp[A[i] // 2] == 0:
#                 return False
#
#             dp[A[i] // 2] -= 1
#
#         return True
#
#     def canReorderDoubled(self, A):
#         """
#         :type A: List[int]
#         :rtype: bool
#         """
#         count_0 = 0
#         B = []
#         C = []
#
#         for a in A:
#             if a == 0:
#                 count_0 += 1
#             elif a > 0:
#                 B.append(a)
#             else:
#                 C.append(-a)
#
#         if count_0 % 2 == 1:
#             return False
#
#         return  self.check(B) and self.check(C)
#
# s = Solution()
# # A = [3,1,3,6]
# # A = [2,1,2,6]
# # A = [4,-2,2,-4]
# # A = [1,2,4,16,8,4]
# A = [2,1,2,4]
# print(s.canReorderDoubled(A))

# class Solution:
#     def minDeletionSize(self, A):
#         return len(self.DeletionSize(A, 0))
#
#     def DeletionSize(self, A, start):
#
#         ans = set()
#
#         N = len(A)
#         if N <= 1:
#             return ans
#
#         for j in range(len(A[0])):
#             pre = A[0][j]
#             isOk = True
#
#             for i in range(N-1):
#                 if ord(pre) > ord(A[i + 1][j]):
#                     ans.add(start + j)
#                     isOk = False
#                     break
#                 pre = A[i + 1][j]
#
#             if j == len(A[0]) - 1:
#                 return ans
#
#             if isOk:
#                 B = []
#                 pre = A[0][j]
#                 is_first = True
#
#                 for i in range(N-1):
#                     if pre == A[i + 1][j]:
#                         if is_first:
#                             B.append(A[i][j+1:])
#                             B.append(A[i+1][j+1:])
#                             is_first = False
#                         else:
#                             B.append(A[i + 1][j + 1:])
#
#                     else:
#                         is_first = True
#                         if len(B) > 1:
#                             new_ans = self.DeletionSize(B, j + 1)
#                             print(B)
#                             print(new_ans)
#                             for a in new_ans:
#                                 ans.add(a)
#
#                         B = []
#
#                     pre = A[i + 1][j]
#
#                 if len(B) > 1:
#                     new_ans = self.DeletionSize(B, j + 1)
#                     print(B)
#                     print(new_ans)
#                     for a in new_ans:
#                         ans.add(a)
#
#                 return ans
#
# s = Solution()
# # A = ["ca","bb","ac"]
# # A = ["xc","yb","za"]
# # A = ["zyx","wvu","tsr"]
# # A = ["abx","agz","bgc","bfc"]
# A = ["bwwdyeyfhc","bchpphbtkh","hmpudwfkpw","lqeoyqkqwe","riobghmpaa","stbheblgao","snlaewujlc","tqlzolljas","twdkexzvfx","wacnnhjdis"]
#
# print(s.minDeletionSize(A))




# abcdefghijklmnopqrstuvwxyz

class Solution:
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        dp = [0 for i in range(21)]
        for a in rods:
            dp[a] += 1

        ans = 0
        can_use = []
        for i in range(21):
            ans += (dp[i] // 2) * i
            if dp[i] % 2 == 1:
                can_use.append(i)

        max_len = sum(can_use) // 2








