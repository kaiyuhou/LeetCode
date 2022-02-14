from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()

        for i, a in enumerate(nums[:-2]):
            if i > 0 and a == nums[i - 1]:
                continue
            b_set = set()
            for c in nums[i + 1:]:
                if (0 - a - c) in b_set:
                    ans.add((a, 0 - a - c, c))
                else:
                    b_set.add(c)

                    # return [list(triple) for triple in ans]
        return [*map(list, ans)]

