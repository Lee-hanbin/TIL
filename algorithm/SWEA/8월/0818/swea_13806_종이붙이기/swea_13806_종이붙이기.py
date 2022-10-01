# swea_13086 종이붙이기

import sys
sys.stdin = open('sample_input (1).txt')


def f(n):
    if n == 1:
        return 1
    return 2**n - f(n-1)

for t in range(int(input())):
    N = int(input())
    cnt = 0
    N = N//10

    cnt = f(N)
    print(f'#{t+1} {cnt}')

