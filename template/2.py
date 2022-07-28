class Node:

    def __init__(self, start, end, m):
        self.sum, self.m, self.max = m * (end - start), m, m
        self.start, self.end = start, end
        self.left, self.right = None, None
        self.leaf = end - start == 1

    def split(self):
        mid = (self.start+self.end)>>1
        self.left = Node(self.start, mid, self.m)
        self.right = Node(mid, self.end, self.m)

    def update(self):
        self.sum = self.left.sum + self.right.sum
        self.max = max(self.left.max, self.right.max)

    def query(self, end):
        if self.start >= end or self.sum == 0: return 0
        elif self.end <= end: return self.sum
        elif not self.left: return self.m * (end - self.start)
        else: return self.left.query(end) + self.right.query(end)

    def scatter(self, k):
        if k == 0 or self.sum == 0:
            return k
        elif self.leaf or self.sum <= k:
            delta = min(self.sum, k)
            self.max = self.sum = self.sum - delta
            return k - delta
        elif not self.left:
            self.split()

        k = self.left.scatter(k)
        k = self.right.scatter(k)
        self.update()
        return k

    def gather(self, end, k):
        if self.start >= end or self.max < k:
            return []
        elif self.leaf:
            self.max = self.sum = self.sum - k
            return [self.start, self.m - (self.sum + k)]
        elif not self.left:
            self.split()

        res = self.left.gather(end, k) or self.right.gather(end, k)
        self.update()
        return res



class BookMyShow:

    def __init__(self, n: int, m: int):
        self.root = Node(0, n, m)

    def gather(self, k: int, maxRow: int) -> List[int]:
        return self.root.gather(maxRow+1, k)

    def scatter(self, k: int, maxRow: int) -> bool:
        if self.root.query(maxRow+1) < k:
            return False
        else:
            self.root.scatter(k)
            return True