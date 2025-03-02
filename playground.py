class Node:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        return self.a > other.a

    def __str__(self):
        return str(self.a)

    def __repr__(self):
        return str(self.a)


a = [1,2,3,4,5]
print(a[1:-1])

