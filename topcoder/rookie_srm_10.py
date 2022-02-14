
# class OddSum:
#     def getSum(self, x):
#         return sum([a for a in x if a % 2 == 1])

# import collections
#
# class EllysPronunciation:
#     def getGood(self, words):
#         ans = 0
#         for w in words:
#             C = collections.Counter(w)
#             n = len(w)
#             v = C['a'] + C['e'] + C['i'] + C['o'] + C['u']
#             if n % 2 == 0 and n // 2 == v:
#                 ans += 1
#         return ans


class DevuAndGoodPalindromicString:
    def isGoodPalindrome(self, s):
        n = len(s)
        if n < 2:
            return 'not good'
        for i in range(n - 1):
            for j in range(i + 2, n + 1):
                # print(i, j)
                # print(s[i:j], s[i:j][::-1])
                if s[i:j] == s[i:j][::-1]:
                    return 'good'
        return 'not good'

s = DevuAndGoodPalindromicString()
ss = 'aba'
print(s.isGoodPalindrome(ss))






