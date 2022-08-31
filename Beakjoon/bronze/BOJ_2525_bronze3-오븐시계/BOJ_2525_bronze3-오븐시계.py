#BOJ 2525번 브론즈 3 오븐시계

import sys
input = sys.stdin.readline

A, B = map(int, input().split())
C = int(input())

if B + C % 60 >= 60:
    print(f'{(A + C//60 + 1)%24} {B + C % 60 - 60}')
else:
    print(f'{(A + C//60)%24} {B + C % 60}')