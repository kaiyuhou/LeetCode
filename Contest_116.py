# # class Solution:
# #     def repeatedNTimes(self, A):
# #         """
# #         :type A: List[int]
# #         :rtype: int
# #         """
# #         D = set()
# #         for a in A:
# #             if a in D:
# #                 return a
# #             else:
# #                 D.add(a)
# #
# # s = Solution()
# # A = [5,1,5,2,5,3,5,4]
# # print(s.repeatedNTimes(A))
#
# class Solution:
#     def maxWidthRamp(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#         N = len(A)
#         left_min = [0 for i in range(N)]
#         right_max = [0 for i in range(N)]
#
#         min_record = {}
#         max_record = [-1 for i in range(50001)]
#
#         cnt = 50001
#         for i,a in enumerate(A):
#             if a < cnt:
#                 min_record[a] = i
#                 cnt = a
#             left_min[i] = cnt
#
#         cnt = -1
#         for i in range(N-1, -1, -1):
#             if A[i] > cnt:
#                 max_record[A[i]] = i
#                 cnt = A[i]
#             right_max[i] = cnt
#
#
#         max_n = max(A)
#         cnt = -1
#         for i in range(max_n, -1, -1):
#             if max_record[i] == -1:
#                 max_record[i] = cnt
#             else:
#                 cnt = max_record[i]
#
#         # print(max_record)
#
#         ans = 0
#         for i in range(N):
#             cnt = max_record[A[i]] - i
#             if cnt > ans:
#                 ans = cnt
#         return ans
#
#
# s = Solution()
# # A = [6,0,8,2,1,5]
# A = [9,8,1,0,1,9,4,0,4,1]
# print(s.maxWidthRamp(A))
#
import math
class Solution:
    def get_k(self, p1, p2):
        if p1[0] - p2[0] == 0:
            return None
        return (p1[1] - p2[1])/(p1[0] - p2[0])

    def dis(self, p1, p2):
        return math.sqrt((p1[0] - p2[0])*()   )

    def the_four(self, p1, p2, p3):
        ans = [0, 0]
        ans[0] = p1[0] + p3[0] - p2[0]
        ans[1] = p1[1] + p3[1] - p2[1]
        return ans

    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        ans = 40000 * 40000 * 2
        N = len(points)
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue

                for k in range(N):
                    if k == i or k == j:
                        continue

                    k1 = self.get_k(points[i], points[j])
                    k2 = self.get_k(points[i], points[k])
                    p1 = points[i]
                    p2 = points[j]
                    p3 = points[k]


                    isOK = True
                    if k2 == None:
                        k2 = k1
                        k1 = None

                    if k2 == None:
                        continue

                    if k1 == None and abs(k2) != 1:
                        continue

                    elif k1 * k2 != -1:
                        continue

                    p4 = []
                    if ((p1[0] - p2[0])*(p2[0] - p3[0]) + (p1[1] - p2[1])*(p2[1]-p3[1]) == 0):
                        p4 = self.the_four(p1,p2,p3)
                    elif ((p1[0] - p3[0]) * (p2[0] - p3[0]) + (p1[1] - p3[1]) * (p2[1] - p3[1]) == 0):
                        p4 = self.the_four(p1, p3, p2)
                    elif ((p1[0] - p3[0]) * (p2[0] - p1[0]) + (p1[1] - p3[1]) * (p2[1] - p1[1]) == 0):
                        p4 = self.the_four(p3, p1, p2)

                    if p4 in points:
                        cnt = self.dis(p1, p2) * self.dis(p1, p3)
                        if cnt < ans:
                            ans = cnt
        return ans









