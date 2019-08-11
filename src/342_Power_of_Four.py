from math import *
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False

        return 4 ** int(log2(num) / log2(4)) == num

s = Solution()
print(s.isPowerOfFour(1))