import sys
import math

print('2')  # T
for x in [4, 1000000]:
    while True:
        s = input()
        if s[0] == '?':
            _, a, b = s.split()
            a = int(a)
            b = int(b)
            print(math.gcd(a + x, b + x))

        if s[0] == '!':
            _, ans = s.split()
            ans = int(ans)
            if ans == x:
                print('YES', file=sys.stderr)
                break
            else:
                print('NO', file=sys.stderr)
                break

# cd codeforces
# rm /tmp/fifo && mkfifo /tmp/fifo && (python3 1665/D.py < /tmp/fifo) | python3 tester.py > /tmp/fifo
# mkfifo /tmp/fifo && (python3 python3 1665/D.py < /tmp/fifo) | python3 tester.py > /tmp/fifo
