class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r * r > x:
            r = (r + x//r) // 2
            # print(r)
        return r

s = Solution()
x = 1042430000000
print(s.mySqrt(x))