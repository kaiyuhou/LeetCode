class SegTree:
    def __init__(self, l, r, m):
        self.sum = m * (r - l)
        self.m = m
        self.max = m

        self.l, self.r = l, r
        self.left, self.right = None, None,
        self.is_split = r - l == 1

    def query_sum(self, end):
        if self.l >= end or self.sum == 0:
            return 0

        if self.r <= end or (not self.is_split):  # not split means no child nodes
            return self.sum * (end - self.l) // (self.r - self.l)

        return self.left.query_sum(end) + self.right.query_sum(end)

    def split(self):  # faster with this function than inline
        mid = (self.l + self.r) // 2
        self.left = SegTree(self.l, mid, self.m)
        self.right = SegTree(mid, self.r, self.m)
        self.is_split = True

    def update(self):  # slower with this function than inline
        self.sum = self.left.sum + self.right.sum
        self.max = max(self.left.max, self.right.max)

    def update_scater(self, rest):
        if rest == 0:
            return 0
        if self.sum == 0:
            return rest

        if not self.left:  # not split
            if self.is_split or self.sum <= rest:  # leaf or remove all
                delta = min(self.sum, rest)
                self.max = self.sum = self.sum - delta
                return rest - delta
            self.split()

        rest = self.left.update_scater(rest)
        rest = self.right.update_scater(rest)
        self.update()
        return rest

    def update_gather(self, end, k):
        if self.l >= end or self.max < k:
            return []

        if not self.left:  # not split
            if self.is_split:  # leaf:
                self.max = self.sum = self.sum - k
                return [self.l, self.m - self.sum - k]
            self.split()

        ans = self.left.update_gather(end, k) or self.right.update_gather(end, k)
        self.update()
        return ans


class BookMyShow:
    def __init__(self, n, m):
        self.seg_tree = SegTree(0, n, m)

    def gather(self, k, maxRow):
        return self.seg_tree.update_gather(maxRow + 1, k)

    def scatter(self, k, maxRow):
        if self.seg_tree.query_sum(maxRow + 1) < k:
            return False
        self.seg_tree.update_scater(k)
        return True
