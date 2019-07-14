from contest.Tree import *

# class Solution:
#     def sampleStats(self, count):
#         ans = []
#         for i, a in enumerate(count):
#             if a > 0:
#                 ans.append(i)
#                 break
#
#         for i in range(255, -1, -1):
#             if count[i] > 0:
#                 ans.append(i)
#                 break
#
#         cnt = 0
#         for i, a in enumerate(count):
#             cnt += i * a
#         ans.append(cnt / sum(count))
#
#         total = sum(count)
#         if total % 2 == 1:
#             cnt = 0
#             for i, a in enumerate(count):
#                 cnt += a
#                 if cnt >= (total // 2) + 1:
#                     ans.append(i)
#                     break
#         else:
#             cnt = 0
#             m = 0
#             for i, a in enumerate(count):
#                 cnt += a
#                 if cnt >= (total // 2):
#                     m += i
#                     break
#             cnt = 0
#             for i, a in enumerate(count):
#                 cnt += a
#                 if cnt >= (total // 2) + 1:
#                     m += i
#                     break
#             ans.append(m / 2)
#
#         maxi = max(count)
#         ans.append(count.index(maxi))
#
#         ans = [float(i) for i in ans]
#
#         return ans
#
#
# s = Solution()
# # count = [1,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# # count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# print(s.sampleStats(count))

# class Solution:
#     def carPooling(self, trips, capacity: int) -> bool:
#         pick = [0 for _ in range(1001)]
#         drop = [0 for _ in range(1001)]
#
#         for a, b, c in trips:
#             pick[b] += a
#             drop[c] += a
#
#         for i in range(1001):
#             capacity += drop[i]
#             capacity -= pick[i]
#             if capacity < 0 :
#                 return False
#
#         return True
#
# s = Solution()
# # trips = [[2,1,5],[3,3,7]]
# # capacity = 4
# # trips = [[2,1,5],[3,3,7]]
# # capacity = 5
#
# # trips = [[2,1,5],[3,5,7]]
# # capacity = 3
#
# trips = [[3,2,7],[3,7,9],[8,3,9]]
# capacity = 11
#
# print(s.carPooling(trips, capacity))

#
# class MountainArray:
#    def get(self, index: int) -> int:
#         return A[index]
#    def length(self) -> int:
#         return len(A)
#
#
# class Solution:
#     def findInMountainArray(self, target: int,  M: 'MountainArray') -> int:
#         N = M.length()
#
#         mem = [-1 for _ in range(N)]
#         def get_i(i):
#             if mem[i] == -1:
#                 mem[i] = M.get(i)
#             return mem[i]
#
#         l = 0
#         r = N - 1
#         while l < r:
#             m = l + (r - l) // 2
#             if get_i(m) < get_i(m + 1):
#                 l = m + 1
#             else:
#                 r = m
#
#         pick = l
#
#         # print(pick)
#
#         if get_i(pick) == target:
#             return pick
#
#         l = 0
#         r = pick
#         while l < r:
#             m = l + (r - l) // 2
#             if get_i(m) == target:
#                 return m
#             elif get_i(m) < target:
#                 l = m + 1
#             else:
#                 r = m
#
#         if get_i(N - 1) == target:
#             return N - 1
#
#         l = pick + 1
#         r = N - 1
#         while l < r:
#             m = l + (r - l) // 2
#             if get_i(m) == target:
#                 return m
#             elif get_i(m) > target:
#                 l = m + 1
#             else:
#                 r = m
#
#         return -1
#
#
# s = Solution()
# m = MountainArray()
#
# A =  [2,3,4,5,3,1]
# # A = [0,1,2,4,2,1]
# target = 1
#
# print(s.findInMountainArray(target, m))

class Solution:
    def mult(self, A, B):
        ans = []
        for a in A:
            for b in B:
                ans.append(a + b)
        return ans

    def analysis(self, A):

        # print(A)

        part = []
        cnt = 0
        buf = ''

        for i, a in enumerate(A):
            if a == ',' and cnt == 0:
                part.append(buf)
                buf = ''
            else:
                if a == '{':
                    cnt += 1
                elif a == '}':
                    cnt -= 1
                buf += a
        part.append(buf)

        ans = []
        for p in part:
            cnt = 0
            buf = ''
            prefix = ['']
            for i, a in enumerate(p):
                if a == '{':
                    cnt += 1
                    if cnt == 1:
                        continue

                elif a == '}':
                    cnt -= 1
                    if cnt == 0:
                        prefix = self.mult(prefix, self.analysis(buf))
                        buf = ''
                        continue

                if cnt > 0:
                    buf += a

                if cnt == 0 and a != '{' and a!= '}':
                    for j in range(len(prefix)):
                        prefix[j] += a

            ans += prefix

        ans = set(ans)
        ans = list(ans)
        ans.sort()
        return ans

    def braceExpansionII(self, A: str):
        return self.analysis(A)


s = Solution()
# A = "{a,b}{c{d,e}}"
A = "{{a,z},a{b,c},{ab,z}}"
print(s.analysis(A))




































