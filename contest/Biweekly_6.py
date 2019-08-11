from Tree import  *


# class Solution:
# #     def isMajorityElement(self, nums, target: int) -> bool:
# #         N = len(nums)
# #         if target not in nums:
# #             return False
# #         start = nums.index(target)
# #         end = start + (N // 2)
# #         if end < N and nums[end] == target:
# #             return True
# #         return False
# #
# # s = Solution()
# # A = [10,101,101,100]
# # target = 101
# # print(s.isMajorityElement(A, target))

# class Solution:
#     def minSwaps(self, data) -> int:
#         M = sum(data)
#         N = len(data)
#         ans = N
#         cnt = [0 for _ in range(N + 1)]
#         for i in range(N):
#             cnt[i + 1] = cnt[i] + data[i]
#
#         for i in range(N):
#             if i + M - 1>= N:
#                 break
#             ans = min(ans, M - (cnt[M + i] - cnt[i]))
#
#         return ans
#
# s = Solution()
# # A = [1,0,1,0,1]
# # A = [0,0,0,1,0]
# A = [1]
# print(s.minSwaps(A))

# class Solution:
#     def canConvert(self, str1: str, str2: str) -> bool:
#         m = {}
#         if str1 == str2:
#             return True
#
#         for i, c in enumerate(str1):
#             if c in m.keys() and m[c] == str2[i]:
#                 continue
#             if c in m.keys() and m[c] != str2[i]:
#                 return False
#             if c not in m.keys():
#                 m[c] = str2[i]
#         if len(m.keys()) < 26:
#             return True
#
#         for i in range(26):
#             for j in range(26):
#                 if i == j: continue
#                 if m[chr(97 + i)] == m[chr(97 + j)]:
#                     return True
#         return False
#
# s = Solution()
# # str1 = "aabcc"
# # str2 = "ccdee"
# # str1 = "leetcode"
# # str2 = "codeleet"
# str1 = 'bacdefghijklmnopqrstuvwxyz'
# str2 = 'bbcdefghijklmnopqrstuvwxyz'
# print(s.canConvert(str1, str2))


class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        NU = len(set(username))

        website_name = list(set(website))
        website_name.sort()
        WMap = {}
        for w in website_name:
            WMap[w] = len(WMap.keys())

        V = set()
        ans = -1
        ans_max = -1
        A = [[] for _ in range(NU)]

        UMap = {}
        U_cnt = 0

        for i, u in enumerate(username):
            if u not in UMap.keys():
                UMap[u] = U_cnt
                U_cnt += 1
            A[UMap[u]].append((timestamp[i], WMap[website[i]]))

        for i, a in enumerate(A):
            a.sort()
            new_a = []
            for t, web in a:
                new_a.append(web)
            A[i] = new_a


        def contain_pattern(k, P):
            B = A[k]
            M = len(B)
            if M < 3:
                return 0

            if P[0] not in B:
                return 0
            a1 = B.index(P[0])
            if P[1] not in B[a1+1:]:
                return 0

            a2 = B.index(P[1], a1+1)
            if P[2] not in B[a2+1:]:
                return 0
            return 1

        for i in range(NU):
            cur_A = A[i]
            n = len(cur_A)
            if n < 3: continue
            for a1 in range(n - 2):
                for a2 in range(a1, n - 1):
                    for a3 in range(a2, n):
                        if (cur_A[a1], cur_A[a2], cur_A[a3]) in V:
                            continue
                        V.add((cur_A[a1], cur_A[a2], cur_A[a3]))
                        cnt = 0
                        for j in range(NU):
                            cnt += contain_pattern(j, (cur_A[a1], cur_A[a2], cur_A[a3]))
                        if cnt > ans_max:
                            ans = (cur_A[a1], cur_A[a2], cur_A[a3])
                            ans_max = cnt
                        elif cnt == ans_max:
                            if (cur_A[a1], cur_A[a2], cur_A[a3]) < ans:
                                ans = (cur_A[a1], cur_A[a2], cur_A[a3])

        return [website_name[ans[0]], website_name[ans[1]], website_name[ans[2]]]

s = Solution()
# username = ["joe","joe","joe","james","james","james","james","mary","mary","mary", "joe", "mary", "mary"]
# timestamp = [1,2,3,4,5,6,7,8,9,10, 11, 12, 13]
# website = ["home","about","career","home","cart","maps","home","home","about","career", "maps", "cart", "maps"]

username = ["dowg","dowg","dowg"]
timestamp = [158931262,562600350,148438945]
website = ["y","loedo","y"]
print(s.mostVisitedPattern(username, timestamp, website))


























