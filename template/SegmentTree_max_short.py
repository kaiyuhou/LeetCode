class SEG:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * 2 * self.n
    
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1])

    def query(self, l, r):
        l += self.n
        r += self.n
        ans = 0
        while l < r:
            # If l, the left interval border, is odd 
            # (which is equivalent to l&1) 
            # then l is the right child of its parent. 
            # Then our interval includes node l but doesn't include it's parent.
            # So we check tree[l] and move to the right of l's parent 
            # by setting l = (l + 1) / 2. 
            # If l is even, it is the left child, 
            # and the interval includes its parent as well
            # (unless the right border interferes), 
            # so we just move to it by setting l = l / 2.
            if l & 1:
                ans = max(ans, self.tree[l])
                l += 1
            if r & 1: 
                r -= 1
                ans = max(ans, self.tree[r])
            l >>= 1
            r >>= 1
        return ans

class Solution:
    def lengthOfLIS(self, A: List[int], k: int) -> int:
        n, ans = max(A), 1
        seg = SEG(n)
        for a in A:
            a -= 1
            premax = seg.query(max(0, a - k), a)
            ans = max(ans, premax + 1)
            seg.update(a, premax + 1)
        return ans