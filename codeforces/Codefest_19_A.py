import math

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        a, b, n = map(int, input().split(" "))
        A = [a, b, a ^ b]
        print(A[n % 3])



