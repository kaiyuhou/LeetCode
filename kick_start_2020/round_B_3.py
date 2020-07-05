from math import *

def scan(start, STR, CNT):
    N, S, E, W = 0, 0, 0, 0
    X = 0
    if start >= CNT:
        return N, S, E, W
    i = start
    while i < CNT:
        if STR[i] == 'N':
            N += 1
            i += 1
        elif STR[i] == 'S':
            S += 1
            i += 1
        elif STR[i] == 'E':
            E += 1
            i += 1
        elif STR[i] == 'W':
            W += 1
            i += 1
        elif STR[i] == '(':
            nn, ss, ee, ww, i = scan(i + 1, STR, CNT)
            N += X * nn
            S += X * ss
            E += X * ee
            W += X * ww
        elif STR[i] == ')':
            return N, S, E, W, i + 1
        else:
            X = int(STR[i])
            i += 1
    return N, S, E, W, i + 1

t = int(input())
for T in range(1, t + 1):
    STR = input()
    CNT = len(STR)
    N, S, E, W, i = scan(0, STR, CNT)

    X = (E - W) % 1000000000 + 1
    Y = (S - N) % 1000000000 + 1

    print("Case #{}: {} {}".format(T, X, Y))