from typing import *
import math

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        radians = []
        extra = 0

        for x, y in points:
            if x == location[0] and y == location[1]:
                extra = 1
                continue
            radians.append(math.atan2(y - location[1], x - location[0]))

        radians.sort()
        radians = radians + [r + 2.0 * math.pi for r in radians]
        angle = math.pi * angle / 180

        ans = 0
        left = 0
        for right in range(len(radians)):
            while radians[right] - radians[left] > angle:
                left += 1
            ans = max(ans, right - left + 1)
        return ans + extra

