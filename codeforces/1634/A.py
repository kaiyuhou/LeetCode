# Problem: A. Reverse and Concatenate
# Contest: Codeforces - Codeforces Round #770 (Div. 2)
# URL: https://codeforces.com/contest/1634/problem/A
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    s = input()

    if k == 0:
        print(1)
        continue
    if s == s[::-1]:
        print(1)
        continue
    print(2)