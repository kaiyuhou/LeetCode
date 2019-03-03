


# class Solution:
#     def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
#         N = len(A)
#         plus = 0
#         for i in range(N-1, -1, -1):
#             if K == 0 and plus == 0:
#                 break
#             k = K % 10
#             K //= 10
#             plus, A[i] = (A[i] + k + plus) // 10, (A[i] + k + plus) % 10
#         while plus > 0 or K > 0:
#             k = K % 10
#             K //= 10
#             plus, new_a = (k + plus) // 10, (k + plus) % 10
#
#             A = [new_a] + A
#         return A
#
#
# s = Solution()
# # A = [2,7,4]
# # K = 181
# # A = [2,1,5]
# # K = 806
# # A = [9,9,9,9,9,9,9,9,9,9]
# # K = 1
# A = [1]
# K = 239
# print(s.addToArrayForm(A, K))

# class Solution:
#     def find(self, a):
#         while self.father[a] != a:
#             a = self.father[a]
#         return a
#
#     def union(self, a, b):
#         f_a = self.find(a)
#         f_b = self.find(b)
#         self.father[f_b] = f_a
#
#     def equationsPossible(self, equations: 'List[str]') -> 'bool':
#         self.father = [i for i in range(26)]
#         for eq in equations:
#             a, b, q = ord(eq[0]) - 97, ord(eq[3]) - 97, eq[1]
#
#             if q == '=':
#                 self.union(a, b)
#
#         for eq in equations:
#             a, b, q = ord(eq[0]) - 97, ord(eq[3]) - 97, eq[1]
#
#             if q == '!':
#                 if self.find(a) == self.find(b):
#                     return False
#
#         return True
#
# s = Solution()
# # eq = ["a==b","b!=a"]
# eq = ["c==c","b==d","x!=z"]
# print(s.equationsPossible(eq))



# class Solution:
#
#     def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
#         if Y <= X:
#             return X - Y
#
#         X, Y = bin(X), bin(Y)
#         self.ans = 0
#         while len(X) < len(Y):
#             # print('before', Y)
#
#             if Y[-1] == '0':
#                 # print("Y -1: ", Y[-1])
#                 Y = Y[:-1]
#                 self.ans += 1
#             else:
#                 Y = bin(int(Y, 2) + 1)
#                 self.ans += 1
#             # print(Y)
#             # input()
#
#
#         X = int(X, 2)
#         Y = int(Y, 2)
#
#
#
#         if X > Y:
#             self.ans += X - Y
#         if X < Y:
#             ans_1 = 1 + (2 * X - Y)
#             ans_2 = 0
#             while X < Y:
#                 if Y % 2 == 0:
#                     Y //= 2
#                     ans_2 += 1
#                 else:
#                     Y += 1
#                     Y //= 2
#                     ans_2 += 2
#             ans_2 += X - Y
#             self.ans += min(ans_1, ans_2)
#         return self.ans
#
# s = Solution()
# X = 5
# Y = 8
# print(s.brokenCalc(X, Y))


class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':



        ans = 0
        p = 0
        q = 1
        N = len(A)
        mem = [[] for i in range(20005)]
        dp = [0 for i in range(20005)]
        cnt = 1
        nums = set()
        nums.add(A[0])
        dp[0] = 0
        mem[A[0]].append(0)

        if N == 1:
            if K == 1:
                return 1
            else:
                return 0

        if K == 1:
            return N

        while q < N:
            if A[q] == A[q-1]:
                dp[q] = dp[q-1]
                ans += dp[q]
                mem[A[q]].append(q)
            else:
                if cnt < K:
                    if A[q] in nums:
                        mem[A[q]].append(q)
                    else:
                        cnt += 1
                        nums.add(A[q])
                        mem[A[q]] = [q]

                if cnt == K:
                    while len(nums) == K:
                        mem[A[p]] = mem[A[p]][1:]

                        if A[p] == A[p + 1]:
                            p += 1
                            dp[q] += 1

                        else:
                            if mem[A[p]] != []:
                                p += 1
                                dp[q] += 1
                            else:
                                nums.remove(A[p])
                                cnt -= 1
                    ans  += dp[q]
        return ans

s = Solution()
A = [1,2,1,2,3]
K = 2
print(s.subarraysWithKDistinct(A, K))



















