import sys


def get_A():
    for i in range(9):
        for j in range(9):
            for k in range(9):
                for h in range(9):
                    for b in range(9):
                        if len({i, j, k, h, b}) != 5:
                            continue
                        if 0 not in [i, j, k, h, b]:
                            continue
                        yield [i, j, k, h, b]


print('10000')
for A in get_A():
    n = len(A)
    ans = A.index(0) + 1
    print(f'{n}')
    i = 0
    while i < 2 * (n - 2) + 1:
        s = input()
        if s[0] == '?':
            s = s[2:]
            a, b, c = map(int, s.split(' '))
            a, b, c = a - 1, b - 1, c - 1
            print(max(A[a], A[b], A[c]) - min(A[a], A[b], A[c]))
        elif s[0] == '!':
            s = s[2:]
            a, b = map(int, s.split(' '))
            if a == ans or b == ans:
                print('YES', file=sys.stderr)
                break
            else:
                print('NO', file=sys.stderr)
                break
        else:
            print(-1)
            sys.exit(10)


# rm /tmp/fifo && mkfifo /tmp/fifo && (python3 round_770_div2.py < /tmp/fifo) | python3 tester.py > /tmp/fifo
# mkfifo /tmp/fifo && (python3 round_770_div2.py < /tmp/fifo) | python3 tester.py > /tmp/fifo
