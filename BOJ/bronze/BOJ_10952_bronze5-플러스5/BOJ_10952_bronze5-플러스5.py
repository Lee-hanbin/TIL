#BOJ 10952 브론즈5 A+B 5

import sys
input = sys.stdin.readline


while 1:
    N, M = map(int, input().split())
    if N == 0:
        break
    print(N+M)