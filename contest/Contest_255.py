from typing import *
from Tree import *

# import functools
# functools.lru_cache(None)

# class Solution:
#     def findGCD(self, nums: List[int]) -> int:
#         ma = max(nums)
#         mi = min(nums)
#
#         for i in range(mi, 0, -1):
#             if ma % i == 0 and mi % i == 0:
#                 return i
#
# s = Solution()
# print(s.findGCD([3,3]))

# class Solution:
#     def findDifferentBinaryString(self, nums: List[str]) -> str:
#         n = len(nums)
#         mem = [1 for i in range(18)]
#
#         for num in nums:
#             if int(num, 2) < 17:
#                 mem[int(num, 2)] = 0
#
#         for i in range(18):
#             if mem[i] == 1:
#                 ans = bin(i)[2:]
#                 extra_0 = n - len(ans)
#                 ans = '0' * extra_0 + ans
#                 return ans
#
# s = Solution()
# nums = ["01","10"]
# nums = ["00","01"]
# nums= ["111","011","001"]
# print(s.findDifferentBinaryString(nums))

# import functools
#
# class Solution:
#     def minimizeTheDifference(self, A: List[List[int]], target: int) -> int:
#         ans = [70 * 805]
#         M = len(A)
#         N = len(A[0])
#
#         @functools.lru_cache(None)
#         def dfs(m, target):
#             if ans[0] == 0:
#                 return
#
#             if m == M:
#                 ans[0] = min(ans[0], abs(target))
#                 return
#
#             if target < 0 and abs(target) > ans[0]:
#                 return
#
#             if target <= 0:
#                 dfs(m + 1, target - min(A[m]))
#
#
#             for i in range(N):
#                 dfs(m + 1, target - A[m][i])
#
#         dfs(0, target)
#         return ans[0]
#
# s = Solution()
# mat = [[1,2,3],[4,5,6],[7,8,9]]
# target = 13
# mat = [[1],[2],[3]]
# target = 100
# mat = [[1,2,9,8,7]]
# target = 6
#
#
# print(s.minimizeTheDifference(mat, target))

from collections import Counter
import math
class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        ans = []
        c = Counter(sums)

        zero_exp = min(c.values())
        if zero_exp != 1:
            zero_cnt = int(math.log2(zero_exp))
            ans += [0] * zero_cnt
            sums.sort()
            new_array = sums[::zero_exp]
            # print(new_array)
            print(zero_cnt)
            zero_index = new_array.index(0)
            # print(zero_index)
            # print(new_array, new_array[:zero_index], new_array[zero_index + zero_cnt:])
            new_array = new_array[:zero_index] + new_array[zero_index + zero_cnt:]
            # print(new_array)
        else:
            sums.sort()

            new_array = sums
            # zero_index = new_array.index(0)
            new_array.remove(0)

        print(sums)
        print(len(sums))

        def dfs(A):
            if len(A) == 0:
                return

            if len(A) == 1:
                ans.append(A[0])
                return

            if A[-1] < 0:
                cur_num = A[-1]
            elif A[-1] > 0 and A[-2] < 0:
                cur_num = A[-1]
            else:
                cur_num = A[-1] - A[-2]
                if cur_num not in A:
                    cur_num = -cur_num
                    if cur_num not in A:
                        cur_num = None


            if A[0] > 0:
                cur_A = A[0]
            elif A[0] < 0 and A[1] > 0:
                cur_A = A[0]
            else:
                cur_A = A[0] - A[1]
                if cur_A not in A:
                    cur_A = -cur_A
                    if cur_A not in A:
                        cur_A = None

            if cur_num is None:
                cur_num = cur_A
            elif cur_A is None:
                pass
            else:
                if abs(cur_A) < abs(cur_num):
                    cur_num = cur_A





            print(f"cur_num: {cur_num}")
            ans.append(cur_num)
            A.remove(cur_num)
            print(f"A to: {len(A)}")


            S = []

            if cur_num < 0:
                while len(A) > 0:
                    a = A.pop(-1)
                    if a + cur_num in A:
                        A.remove(a + cur_num)
                        S.append(a)
                    else:
                        print(f"not include {a}")


            else: # cur_num > 0
                while len(A) > 0:
                    a = A.pop(0)
                    if a + cur_num in A:
                        A.remove(a + cur_num)
                        S.append(a)
                    else:
                        print(f"not include {a}")

            S.sort()
            print(S)
            print(len(S))

            dfs(S)

        dfs(new_array)
        return ans




s = Solution()
# n = 4
# sums = [0,0,5,5,4,-1,4,9,9,-1,4,3,4,8,3,8]
#
# n = 3
# sums = [-3,-2,-1,0,0,1,2,3]

# n = 2
# sums = [0,0,0,0]

# n = 4
# sums = [-762, -457, -381, -381, -183, -76, -76, 0, 122, 198, 198, 305, 503, 503, 579, 884]

n = 8
sums = [408,-307,86,-886,-164,784,-377,49,-1424,14,0,310,-589,162,735,872,-80,557,-590,-290,319,-51,-1173,-715,216,-1207,-392,333,-437,539,276,459,522,-233,527,390,-472,-388,-521,-486,-1011,-457,-278,596,-452,-62,-145,-262,-1048,-427,-852,-159,-402,171,264,704,-1287,-210,-126,345,114,1168,443,-263,-119,-1389,-502,-347,-338,117,57,-880,494,378,-897,-733,1066,212,1293,-623,137,488,492,37,-165,508,-1128,-946,201,265,-639,167,364,23,-960,710,770,-293,261,30,-635,-482,-509,-911,-15,34,284,-772,-327,-698,997,-45,-441,-57,-206,196,-343,952,-915,151,231,458,-114,515,82,383,1248,428,344,-668,-604,-227,363,595,239,-817,721,-308,-736,-161,986,306,-395,-691,-619,972,-270,51,-95,-415,-664,-199,251,296,-11,-539,-653,414,-835,892,-50,-460,-816,659,-966,102,815,602,-190,326,-372,-81,94,87,69,131,-125,-258,-703,-12,-634,1017,560,-771,755,-1242,-1068,-245,-866,1213,-176,219,-931,-182,246,-31,18,1031,68,-213,299,-1162,1111,572,63,-1469,-357,690,182,-358,-239,-1148,226,447,-559,-225,-540,-1113,-554,-584,-1344,281,477,-313,917,-422,132,-778,790,-475,-244,-1093,-684,-991,835,463,-670,-495,413,641,937,-17,-131,739,676,181,-520,640,-440,-96,6,-194,-1193,-407,-566,-748]
print(len(sums))

print(s.recoverArray(n, sums))





























