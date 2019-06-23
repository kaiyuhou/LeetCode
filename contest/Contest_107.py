# class Solution:
#     def isLongPressedName(self, name, typed):
#         """
#         :type name: str
#         :type typed: str
#         :rtype: bool
#         """
#         if name[0] != typed[0]:
#             return False
#
#         j = 0
#         for i in range(len(name)):
#             if j == len(typed):
#                 return False
#
#             if name[i] == typed[j]:
#                 j += 1
#             else:
#                 while j < len(typed):
#                     if typed[j] == typed[j-1]:
#                         j += 1
#                     else:
#                         if typed[j] == name[i]:
#                             j += 1
#                             break
#                         else:
#                             return False
#                 if j == len(typed) and not (typed[j-1] == name[-1]) :
#                     return False
#
#         while j < len(typed):
#             if typed[j] == typed[j-1]:
#                 j += 1
#             else:
#                 return False
#         return True
#
# s = Solution()
# # name = "alex"
# # typed = "aaleex"
# # name = "kikcxmvzi"
# # typed = "kiikcxxmmvvzz"
# # name = "saeed"
# # typed = "ssaaedd"
# # name = "leelee"
# # typed = "lleeelee"
# name = "laiden"
# typed = "laiden"
# print (s.isLongPressedName(name, typed))
#
# class Solution:
#     def minFlipsMonoIncr(self, S):
#         """
#         :type S: str
#         :rtype: int
#         """
#         pre_1 = [0 for i in range(len(S) + 1)]
#         after_0 = []
#
#         cnt = 0
#         after_0.append(cnt)
#         for c in S:
#             if c == '1':
#                 cnt += 1
#             after_0.append(cnt)
#
#         cnt = 0
#         for i in range(len(S)-1, -1, -1):
#             if S[i] == '0':
#                 cnt += 1
#             pre_1[i] = cnt
#
#
#         # print(after_0)
#         # print(pre_1)
#
#         ans = [pre_1[i] + after_0[i] for i in range(len(S) + 1)]
#         return min(ans)
#
#
#
# s = Solution()
# # S = "00110"
# # S = "010110"
# # S = "00011000"
# S = "000111"
# print(s.minFlipsMonoIncr(S))

# class Solution:
#     def threeEqualParts(self, A):
#         """
#         :type A: List[int]
#         :rtype: List[int]
#         """
#         n = A.count(1)
#
#         m = n // 3
#         if n % 3 != 0:
#             return [-1, -1]
#
#         if n == 0:
#             return [0, 2]
#
#         index = []
#
#         cnt = 0
#         for i in range(len(A)):
#             if A[i] == 1:
#                 if cnt in [0, m, 2 * m]:
#                     index.append(i)
#                 cnt += 1
#                 if cnt in [m, 2*m, 3*m]:
#                     index.append(i)
#
#         A1 = A[index[0]:index[1] + 1]
#         A2 = A[index[2]:index[3] + 1]
#         A3 = A[index[4]:index[5] + 1]
#
#         if (A1 != A3) or (A1 != A2):
#             return [-1, -1]
#
#
#         last0 = len(A) - index[5] - 1
#         inter0 = index[4] - index[3] - 1
#         first0 = index[2] - index[1] - 1
#         # print(last0, inter0, first0)
#
#         if last0 > inter0 or last0 > first0:
#             return [-1, -1]
#
#         i = index[1] + last0
#         j = index[3] + last0 + 1
#         return [i, j]
#
#
# s = Solution()
# A = [1,0,1,0,1]
# #A = [1,1,0,1,1]
# # A = [0,0,0]
# # A = [1,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0]
# # A = [1,0,1,1,0]
# print(s.threeEqualParts(A))

class Solution:

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]

        if pid == qid:
            return

        for i in range(len(self.id)):
            if self.id[i] == qid:
                self.id[i] = pid

    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        initial.sort()
        N = len(graph)

        minAns = N
        ans = initial[0]
        for cur in initial:
            self.id = [i for i in range(N)]

            for i, l in enumerate(graph):
                if i == cur:
                    continue
                for j, a in enumerate(l):
                    if j == cur:
                        continue
                    if a == 1:
                        self.union(i, j)

            mem = set()
            for i in initial:
                if i == cur:
                    continue
                mem.add(self.id[i])

            # print(self.id)
            cur_ans = 0
            for i in range(N):
                if self.id[i] in mem:
                    cur_ans += 1

            # print(cur_ans)
            if cur_ans < minAns:
                minAns = cur_ans
                ans = cur
        return ans

s = Solution()
# graph = [[1,1,0],[1,1,1],[0,1,1]]
# initial = [0,1]
# graph = [[1,1,0],[1,1,0],[0,0,1]]
# initial = [0,1]
# graph = [[1,1,0],[1,1,1],[0,1,1]]
# initial = [0,1]
graph = [[1,1,0,0],[1,1,1,0],[0,1,1,1],[0,0,1,1]]
initial = [0,1]
print(s.minMalwareSpread(graph, initial))







