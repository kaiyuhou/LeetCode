class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = []
        ans = -math.inf
        for x, y in points:
            while q and q[0][1] < x - k:
                heapq.heappop(q)
            if q:
                ans = max(ans, -q[0][0] + x + y)
            heapq.heappush(q, (x - y, x))
        return ans