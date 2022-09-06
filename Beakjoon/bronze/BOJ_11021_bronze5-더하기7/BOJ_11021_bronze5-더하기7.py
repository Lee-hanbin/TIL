#BOJ 11021 브론즈5 A+B 7

import sys
input = sys.stdin.readline

for i in range(int(input())):
    N, M = map(int, input().split())
    print(f'Case #{i+1}: {N+M}')