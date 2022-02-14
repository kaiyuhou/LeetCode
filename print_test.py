import sys, os
import time

# def print_line(a, b):
#     sys.stdout.write("\rABC %s/%s" % (a, b))
#     sys.stdout.flush()
#
#
# for i in range(10):
#     print_line(i, 10)
#     time.sleep(1)



import sys
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))

n = 16
a = [0 for _ in range(n)]
a.append(1)


while True:
    try:
        a, b = map(int, input().strip().split())
        print (a+b)
    except EOFError:
        break

def print_a(iter):
    print(f'{iter}:', end='\t')
    for i, n in enumerate(a):
        print(f'{i}:{n}', end='\t')
    print()

for i in range(16, -1, -1):
    for j in range(i):
        a[j // 2] += a[i]
    print_a(i)