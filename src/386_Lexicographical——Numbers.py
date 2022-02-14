from typing import *

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [1]
        cur = 1
        while len(ans) < n:
            if cur * 10 <= n:
                cur *= 10
                ans.append(cur)
            else:
                cur += 1

                while cur % 10 == 0:
                    cur //= 10

                if cur > n:
                    cur = cur // 10 + 1
                    while cur % 10 == 0:
                        cur //= 10

                ans.append(cur)
        return ans

s = Solution()
n = 192
print(s.lexicalOrder(199))

