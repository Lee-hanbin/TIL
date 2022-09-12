#BOJ 2439 브론즈4 별찍기2

import sys
input = sys.stdin.readline

N = int(input())
for i in range(1, N+1):
    print(' '*(N-i) + '*'*i)