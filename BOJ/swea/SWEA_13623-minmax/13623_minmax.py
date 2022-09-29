#SWEA 13623 minmax

import sys
sys.stdin = open('1.txt')

for t in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    print(f'#{t+1} {max(lst)-min(lst)}')