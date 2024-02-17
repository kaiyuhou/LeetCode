class Node:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        return self.a > other.a

    def __str__(self):
        return str(self.a)

    def __repr__(self):
        return str(self.a)


A = []
for i in range(10):
    A.append(Node(i))

print(A)

A.sort()
print(A)


