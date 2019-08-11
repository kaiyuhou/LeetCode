class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n > 1:
            n, b = divmod(n, 3)
            if b:
                return False
        return True


s = Solution()
print(s.isPowerOfThree(-3))