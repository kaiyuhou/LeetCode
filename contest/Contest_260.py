from typing import *
from Tree import *

# class Solution:
#     def maximumDifference(self, nums: List[int]) -> int:
#         ans = -1
#         cm = nums[0]
#         for i in range(1, len(nums)):
#             if nums[i] > cm:
#                 ans = max(ans, nums[i] - cm)
#             cm = min(cm, nums[i])
#         return ans
#
#
# s = Solution()


# class Solution:
#     def gridGame(self, grid: List[List[int]]) -> int:
#         n = len(grid[0])
#
#         l1 = [0]
#         for i in range(1, n):
#             l1.append(l1[i-1] + grid[0][i])
#
#         l2 = [0] * n
#         for i in range(n-2, -1, -1):
#             l2[i] = l2[i+1] + grid[1][i]
#
#         ans = None
#         for i in range(n):
#             best2 = max(l1[n-1] - l1[i], l2[0] - l2[i])
#             if ans is None:
#                 ans = best2
#             else:
#                 ans = min(ans, best2)
#         return ans
#
# s = Solution()
# grid = [[2,5,4],[1,5,1]]
# grid = [[3,3,1],[8,5,2]]
# grid = [[1,3,1,15],[1,3,3,1]]
# grid = [[1,0,0],[0,0,1]]
# print(s.gridGame(grid))

# class Solution:
#     def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
#         m = len(board)
#         n = len(board[0])
#         wc = len(word)
#         ans = False
#
#         def check(direct, i, j):
#             # print(direct, i, j)
#             nonlocal ans
#             for c in word:
#                 if board[i][j] == ' ' or c == board[i][j]:
#                     i += direct[0]
#                     j += direct[1]
#                 else:
#                     return
#             if i >= m or i < 0 or j >= n or j < 0 or board[i][j] == '#':
#                 ans = True
#             # print(direct, i, j)
#
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == '#':
#                     continue
#                 if board[i][j] == ' ' or board[i][j] == word[0]:
#                     if i == 0 or board[i-1][j] == '#':
#                         if (m - i) >= wc:
#                             check((1, 0), i, j)
#                     if i == m - 1 or board[i+1][j] == '#':
#                         if i + 1 >= wc:
#                             check((-1, 0), i, j)
#                     if j == 0 or board[i][j-1] == '#':
#                         if (n - j) >= wc:
#                             check((0, 1), i, j)
#                     if j == n - 1 or board[i][j+1] == '#':
#                         if j + 1 >= wc:
#                             check((0, -1), i, j)
#                     if ans:
#                         return True
#         return False
#
# s = Solution()
# board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]]
# word = "abc"
# # board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]]
# # word = "ac"
# # board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]]
# # word = "ca"
#
# print(s.placeWordInCrossword(board, word))


class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        exp_set = set()

        wrong_ans_set = set()

        op_map = {
            '+': lambda a, b: a + b,
            '*': lambda a, b: a * b
        }

        def e(nums, ops):
            ans = [0] * 15
            ans[0] = nums[0]
            j = 0
            for i in range(len(ops)):
                if ops[i] == '*':
                    ans[j] = ans[j] * nums[i + 1]
                else:
                    j += 1
                    ans[j] = nums[i + 1]
            return sum(ans)


        def dfs(nums, ops):
            if len(ops) == 0:
                wrong_ans_set.add(nums)
                return

            if (nums, ops) in exp_set:
                return
            exp_set.add((nums, ops))

            if len(ops) == 1 or ('*' not in ops) or ('+' not in ops):
                wrong_ans_set.add(e(nums, ops))
                return
            cur = e(nums, ops)
            if cur > 1000:
                return
            wrong_ans_set.add(cur)

            for i in range(len(ops)):
                dfs(nums[:i] + (op_map[ops[i]](nums[i], nums[i+1]),) + nums[i+2:], ops[:i] + ops[i+1:])

                # if ops[i] == '+':
                #     if (i > 0 and ops[i - 1] == '*') or (i < len(ops) - 1 and ops[i + 1] == '*'):
                #         dfs(nums[:i] + [str(eval(nums[i]+ops[i]+nums[i+1]))] + nums[i+2:], ops[:i] + ops[i+1:])
                # elif ops[i] == '*':
                #     if (i > 0 and ops[i - 1] == '+') or (i < len(ops) - 1 and ops[i + 1] == '+'):
                #         dfs(nums[:i] + [str(eval(nums[i]+ops[i]+nums[i+1]))] + nums[i+2:], ops[:i] + ops[i+1:])

        nums = [int(s[0])]
        ops = []
        for i in range(1, len(s)):
            if i % 2 == 1:
                ops.append(s[i])
            else:
                nums.append(int(s[i]))
        # print(nums, ops)
        dfs(tuple(nums), tuple(ops))

        correct_ans = e(nums, ops)

        rnt = 0
        for ans in answers:
            if ans == correct_ans:
                rnt += 5
            elif ans in wrong_ans_set:
                rnt += 2
        return rnt


ss = Solution()
# s = "7+3*1*2+7+3*1*2+7+3*1*2+7+3*1*2"
# answers = [20,13,42]
# s = "3+5*2"
# answers = [13,0,10,13,13,16,16]
# s = "6+0*1"
# answers = [12,9,6,4,8,6]
s = '4+4*2+6+4*4+4+4*6+4*6+2*6+4'
answers = [20,98,792]
s = "4*8*4+8*4*8*2+4*6+4*8+8*6+2*2"
answers = [856,972,748,460,1000,852,880,945,748,980,748,964,992,748,908,682,980,712,776,964,154,316,796,972,748,133,335,70,748,910,623,301,705,944,844,748,992,908,988,924,748,748,824,972,538,186,756,980,824,972,254,748,856,748,748,748,778,790,984,748,1000,347,944,125,972,875,748,992,333,972,748,880,69,988,830,47,748,748,852,748,748,980,748,364,748,828,699,701,908,876,421,693,844,197,996,748,748,989,956,21,9,748,904,748,776,880,824,748,980,728,872,796,910,748,228,748,828,964,824,997,748,477,346,972,748,748,67,872,872,960,952,944,748,571,748,201,336,863,828,748,60,892,776,748,1000,757,550,796,789,89,771,415,492,988,904,924,776,972,972,748,824,993,796,805,952,924,872,748,908,872,972,566,856,988,852,992,748,924,221,844,856,956,594,972,383,277,748,748,601,796,984,748,262,649,892,876,876,423,726,964,533,446,892,972,876,988,980,468,956,18,37,748,506,776,748,956,796,824,956,748,748,566,824,748,817,142,64,682,799,956,745,736,1000,748,904,828,856,876,748,908,748,748,396,406,748,988,748,78,952,905,748,748,748,748,924,655,748,471,920,23,996,476,776,790,828,952,924,964,748,856,980,168,791,988,748,748,305,748,748,748,992,62,944,509,748,331,892,974,201,748,996,748,257,992,748,748,796,952,748,856,944,70,892,902,852,748,876,748,796,748,980,748,908,159,876,1000,748,748,748,748,828,88,828,828,848,876,748,892,748,824,390,852,748,996,746,776,748,980,776,748,748,824,6,405,748,65,748,880,476,852,290,856,748,796,748,908,529,646,742,876,476,748,748,776,956,932,105,748,748,748,816,892,748,984,876,787,748,748,964,826,767,908,347,20,748,384,623,748,980,996,989,748,956,727,748,748,748,400,190,762,908,748,984,144,988,796,748,748,84,754,984,748,748,796,373,944,839,924,776,956,920,212,956,642,748,980,880,796,748,748,748,818,593,828,748,221,71,471,606,952,748,318,748,748,241,944,748,758,748,992,748,128,748,748,607,972,876,956,876,892,796,880,781,1000,964,431,458,964,80,776,118,956,880,813,944,238,724,748,215,748,984,457,996,748,748,952,748,710,692,748,916,952,279,748,803,748,748,748,748,102,904,920,748,753,776,748,748,952,367,916,944,748,748,658,620,748,748,1000,748,748,960,403,748,796,972,748,748,386,852,924,514,844,262,748,872,748,144,595,748,952,1000,650,748,749,816,980,748,748,924,748,748,260,940,996,956,920,908,691,491,773,748,748,31,920,853,748,748,476,275,952,748,748,852,748,972,748,748,748,504,559,964,748,988,748,136,964,802,748,358,677,748,75,904,895,748,996,29,420,798,748,128,748,337,852,748,876,748,748,748,748,748,984,229,704,833,748,748,596,748,579,892,748,852,933,390,796,748,475,748,748,180,737,6,748,430,872,748,132,605,319,545,944,748,908,892,844,748,624,956,776,2,908,996,796,892,170,748,605,590,856,748,477,952,135,980,143,992,852,820,371,908,964,196,988,892,988,748,811,956,748,908,177,952,828,818,880,748,748,852,872,59,748,979,748,748,568,748,748,443,748,924,565,964,705,852,748,525,996,748,748,748,748,748,920,748,945,397,279,204,283,908,992,748,928,904,594,872,748,748,362,694,629,972,796,748,748,748,748,526,748,776,824,815,892,584,748,748,916,748,924,403,122,944,748,876,748,916,498,774,748,944,920,852,748,266,748,956,972,748,852,916,996,988,956,748,1000,617,890,748,748,11,748,824,956,748,880,69,171,827,748,513,892,70,748,933,872,748,748,824,904,799,222,748,748,788,872,992,364,916,992,748,748,741,235,609,748,748,748,876,964,796,433,748,492,748,748,748,984,583,984,748,796,961,972,876,117,830,320,916,748,988,988,516,748,748,49,748,828,748,652,157,429,902,916,140,748,748,796,133,794,828,83,748,748,856,999,892,660,748,748,852,247,828,859,704,287,635,748,632,428,908,828,748,748,992,992,26,924,661,916,748,964,586,872,516,748,748,748,872,754,748,748,946,828,904,988,924,748,447,409,956,393,880,852,1000,68,238,796,683,748,569,748,382,508,748,956,956,748,748,748,748,824,908,844,748,748,748,748,936,821,531,1000,904,748,127,748,479,774,984,355,952,916,984,748,964,920,944,992,956,748,748,748,924,956,8,748,863,872,880,748,852,828,996,872,651,782,419,932,916,238,748,874,796,904,748,748,964,952,952,796,944,748,937,984,964,858,1000,748,688,748,748,138,582,828,80,886,892,315,810,748,904,748,952,748,748,245,833,996,765,941,790,748,844,776,122,154,748,748,952,52,956,735,972,748,996,748,908,748,916,748,956,748,810,679,852,860,776,748,748,594,632,964,748,330,964,796,956,748,984,49,828,896,816,872,330,748,748,748,952,748,984,641,748,892,748,1000,925,748,908,51,980,863,162,988,552,1000,748,971,748,920,748,748,459,796,952,920,905,57,748,979,748,748,254,920,876,210,792,237,920,796,996,904,972,880,972,673,924,748,378,916,453,748,748,466,920,140,748,748,980,308,872,748,789,796,748,876,748,984,748,748,286,892,731,852,748,186,303,748,768,748,748,748,694,713,185,748,635,204,417,964,852,748,984,290,904,1000,828,924,748,748,748,856,32,996,748,956,984,410,904,610,845,984,107,796,748,796,996,920,605,500,748,780,775,748,748,904,880,362,920,956,748,748,872,988,649,748,806,227,991,73,328,880,748,748,748,748,748,225,800,748,748,924,916,876,749,748,748,916,748,748,95,858,946,669,379,1000,748,892,247,872,924,828,748,972,748,1000,956,748,984,748,748,872,952,748,872,199,235,502,748,556,852,748,997,748,1000,537,828,330,748,844,944,221,892,980,748,920,748,828,361,892,920,309,972,748,748,748,748,748,660,508,899,319,852,500,686,920,16,535,872,748,968,824,748,748,844,98,748,876,880,315,748,748,988,588,748,748,520,776,748,748,161,68,182,972,748,844,813,748,748,844,748,920,824,517,528,924,904,984,89,748,924,856,748,665,513,892,748,748,908,748,876,872,964,748,791,196,473,748,748,748,856,952,828,1000,828,62,796,671,856,895,633,748,844,582,193,944,748,177,956,920,748,748,346,914,748,574,904,872,966,143,532,748,984]
print(ss.scoreOfStudents(s, answers))






