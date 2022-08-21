# swea 13626번 구간합 D3

import sys
sys.stdin = open('sample_input(1).txt')

for t in range(int(input())):
    N, M = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    set1 =set()
    for i in range(N-M +1):
        temp = 0
        for j in range(M):
            temp += lst[i+j]
        set1.add(temp)
    print(f'#{t+1} {max(set1) - min(set1)}')