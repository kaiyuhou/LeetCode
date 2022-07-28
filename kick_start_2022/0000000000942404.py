from sys import stdin, stdout, setrecursionlimit

input = stdin.readline
print = lambda s: stdout.write(str(s) + '\n')
# setrecursionlimit(100000)


def main(case):
    n, m = map(int, input().split())
    t = sum(list(map(int, input().split())))
    print(f'Case #{case + 1}: {t - m * (t // m) }')

    

T = int(input())
for t in range(T):
    main(t)