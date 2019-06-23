
#
# class Solution:
#     def kClosest(self, points, K):
#         """
#         :type points: List[List[int]]
#         :type K: int
#         :rtype: List[List[int]]
#         """
#         dp = []
#         for i, p in enumerate(points):
#             dp.append(((p[0] * p[0] + p[1] * p[1]), i))
#         dp.sort()
#         dp = dp[:K]
#         ans = []
#         for a in dp:
#             # print(a[1])
#             ans.append(points[a[1]])
#         return ans
#
#
#
#
#
# s = Solution()
# points = [[3,3],[5,-1],[-2,4]]
# K = 2
# print(s.kClosest(points, K))

# class Solution:
#     def largestPerimeter(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#         A.sort(reverse=True)
#         N = len(A)
#
#         for i in range(N - 2):
#             if A[i+1] + A[i+2] > A[i]:
#                 return A[i+1] + A[i+2] + A[i]
#         return 0
#
# s = Solution()
# A = [3,6,2,3]
# print(s.largestPerimeter(A))


class Solution:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        dp = [0 for i in range(K)]

        sum = 0
        for a in A:
            sum += a
            dp[sum % K] += 1

        ans = dp[0]
        for i in range(K):
            if (dp[i] > 1):
                ans += (dp[i] * (dp[i]-1)) // 2
        return ans
#
# s = Solution()
# A = [4,5,0,-2,-3,1]
# K = 5
# print(s.subarraysDivByK(A, K))

class Solution:
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        cnt_ok_odd = A[-1]
        cnt_not_ok_odd = -1

        cnt_ok_even = A[-1]
        cnt_not_ok_even = 100000 + 1

        ans = 1
        N = len(A)
        if N == 1:
            return ans

        for i in range(N-2, -1, -1):
            isOk = False
            ok_odd, not_ok_odd, ok_even, not_ok_even = cnt_ok_odd, cnt_not_ok_odd, cnt_ok_even, cnt_not_ok_even


            if A[i] > cnt_not_ok_odd and A[i] <= cnt_ok_odd:
                print("ok_odd")
                ans += 1

                if cnt_not_ok_even < A[i]:
                    not_ok_even = A[i] + 1
                if cnt_ok_even > A[i]:
                    ok_even = A[i]

            else:
                isOk = False
                if cnt_not_ok_even > A[i]:
                    not_ok_even = A[i]
                if cnt_ok_even < A[i]:
                    ok_even = A[i] + 1

            if A[i] < cnt_not_ok_even and A[i] >= cnt_ok_even:
                print("ok_even")
                isOk = True
                if cnt_ok_odd < A[i]:
                    ok_odd = A[i]
                if cnt_not_ok_odd > A[i]:
                    not_ok_odd = A[i] - 1
            else:
                if cnt_ok_odd > A[i]:
                    ok_odd = A[i] - 1
                if cnt_not_ok_odd < A[i]:
                    not_ok_odd = A[i]

            cnt_ok_odd, cnt_not_ok_odd, cnt_ok_even, cnt_not_ok_even = ok_odd, not_ok_odd, ok_even, not_ok_even

            print("i = %d, ok_odd = %d, not_ok_odd = %d, ok_even = %d, not ok_even = %d" % (A[i], ok_odd, not_ok_odd, ok_even, not_ok_even ))

        return ans

s = Solution()
A = [2,3,1,1,4]
print(s.oddEvenJumps(A))











