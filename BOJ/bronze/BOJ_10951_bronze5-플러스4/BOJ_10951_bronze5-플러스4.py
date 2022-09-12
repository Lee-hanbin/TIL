#BOJ 10951 브론즈5 A+B 4

import sys
input = sys.stdin.readline


while 1:
    try:
        N, M = map(int, input().split())
        print(N+M)
    except:
        break