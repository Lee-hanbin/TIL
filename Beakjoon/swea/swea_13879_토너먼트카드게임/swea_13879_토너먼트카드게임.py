# swea 13879 토너먼트카드게임

import sys
sys.stdin = open('sample_input(2).txt')


def low(lst, N):
    #list의 크기가 2가 되면 멈춰
    if stack == :
        return lst

    #N이 2가 될때까지 팀을 나눠
    stack.append([0, N//2])
    lst = low(lst, N//2)
    stack.append([[N//2 + 1, N - 1]])
    print(stack)
for t in range(int(input())):
    sol = 0
    N = int(input())
    lst = list(map(int, input().split()))
    stack = []
    print(lst)
    low(lst, N)
    # print(f'#{t+1} {sol}')