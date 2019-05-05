# import collections
import functools
import operator
class Solution:
    def singleNumber(self, nums) -> int:
        # a = collections.Counter(nums)
        # for k, v in a.items():
        #     if v == 1:
        #         return k
        # return reduce(lambda x, y: x ^ y, nums)
        return functools.reduce(operator.xor, nums)


s = Solution()
# A = [2, 2, 1]
A = [4, 1, 2, 1, 2]
print(s.singleNumber(A))