import bisect
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, n in enumerate(numbers):
            j = bisect.bisect_left(numbers, target - n, lo=i+1)
            if j != len(numbers) and numbers[j] == target - n:
                return [i + 1, j + 1]
        return [-1, -1]

s = Solution()
print(s.twoSum([2,7,11,15], 9))