class RecentCounter:

    def __init__(self):
        self.mem = []

    def ping(self, t):
        self.mem.append(t)
        if t <= 3000:
            return len(self.mem)
        else:
            start = t - 3000

        l = 0
        r = len(self.mem) - 1
        while l != r:
            m = (l + r) // 2
            if self.mem[m] == start:
                l = r = m
            elif self.mem[m] < start and self.mem[m + 1] > start:
                l = r = m + 1
            elif self.mem[m] < start:
                l = m + 1
            else:
                r = m
        return len(self.mem) - l


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))
print(obj.ping(7002))
print(obj.ping(8002))

# class Solution:
#     def knightDialer(self, N):
#         """
#         :type N: int
#         :rtype: int
#         """
#         # ans = 0
#         Mod = 1000000007
#         if N == 1:
#             return 10
#         if N == 2:
#             return 20
#         # l = 6
#         # for i in range(N-1):
#         #     l = (l*2) % Mod
#         # r = 300
#         # for i in range(N-1):
#         #     r = (r * 300) % Mod
#         # return (l + r) % Mod
#         nums = [0,1,2,300,4,6,7,8,9]
#         cur = {0:1, 1:1, 2:1, 300:1, 4:1, 6:1, 7:1, 8:1, 9:1 }
#         next = {0:0, 1:0, 2:0, 300:0, 4:0, 6:0, 7:0, 8:0, 9:0 }
#
#         jump = {0:[4,6], 1:[6,8], 2:[7,9], 300:[4,8], 4:[300,9,0], 6:[1,7,0], 7:[2,6], 8:[1,300], 9:[2,4]}
#         for i in range(N-1):
#             for num in nums:
#                 for j in jump[num]:
#                     next[j] += cur[num]
#             cur = next.copy()
#             next = {n:0 for n in nums}
#
#             # print(cur)
#         ans = 0
#         for (_, i) in cur.items():
#             ans += i
#
#         return ans % Mod
#
#
# s = Solution()
# print(s.knightDialer(5000))
