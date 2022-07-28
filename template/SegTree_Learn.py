class SegmentTree:
    def __init__(self, l, r):
        self.l, self.r = l, r

        self.val = 0
        self.max = 0
        self.sum = 0

        if l != r:
            self.mid = (l + r) // 2
            self.left = SegmentTree(l, self.mid)
            self.right = SegmentTree(self.mid + 1, r)

    def update(self, l, r, val=1):
        if self.l > r or self.r < l:  # LR sL-sR LR
            return

        if self.l >= l and self.r <= r:  # L-sL-sR-R
            self.val += val
            self.max += val
            self.sum += val * (self.r - self.l + 1)
            return

        self.left.update(l, r, val)
        self.right.update(l, r, val)
        self.max = self.val + max(self.left.max, self.right.max)
        self.sum = self.val * (self.r - self.l + 1) \
                   + self.left.sum \
                   + self.right.sum

    def query(self, i):
        if i < self.l or i > self.r:  # LR sL-sR LR
            return 0
        if self.l == self.r:  # is leaf
            return self.val
        if i <= self.mid:
            return self.val + self.left.query(i)
        return self.val + self.right.query(i)

    def querySum(self, l, r):
        if self.l > r or self.r < l:  # LR sL-sR LR
            return 0
        if self.l >= l and self.r <= r:   # L-sL-sR-R
            return self.sum
        return self.val * (min(r, self.r) - max(l, self.l) + 1) \
               + self.left.querySum(l, r) + self.right.querySum(l, r)

    def queryLowestGreater(self, v):
        if self.max < v:
            return -1
        if self.l == self.r:
            if self.max < v:
                return -1
            else:
                return self.l
        if self.left.max >= v - self.val:
            return self.left.queryLowestGreater(v - self.val)
        return self.right.queryLowestGreater(v - self.val)


class BookMyShow:

    def __init__(self, n, m):
        self.st = SegmentTree(0, n - 1)
        self.st.update(0, n - 1, m)
        self.n = n
        self.m = m
        self.k = 0

    def gather(self, k, maxRow):
        i = self.st.queryLowestGreater(k)
        if i < 0 or i > maxRow:
            return []
        v = self.st.query(i)
        self.st.update(i, i, -k)
        return [i, self.m - v]

    def scatter(self, k, maxRow):
        if self.st.querySum(0, maxRow) >= k:
            while self.k < self.n and k > 0:
                v = self.st.query(self.k)
                self.st.update(self.k, self.k, -min(v, k))
                if v <= k:
                    self.k += 1
                k -= min(v, k)
            return True
        return False


bms = BookMyShow(2, 5)
print(bms.gather(4, 0))
print(bms.gather(2, 0))
print(bms.scatter(5, 1))
print(bms.scatter(5, 1))