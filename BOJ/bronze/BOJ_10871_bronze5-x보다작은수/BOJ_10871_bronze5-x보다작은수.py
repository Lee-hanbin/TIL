#BOJ 10871 브론즈5 x보다 작은 수

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
for i in lst:
    if i < M:
        print(i,end=' ')

