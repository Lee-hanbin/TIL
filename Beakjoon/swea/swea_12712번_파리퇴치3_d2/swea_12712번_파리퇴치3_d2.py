# 파리잡기

import sys
sys.stdin = open('in1.txt')



for t in range(int(input())):
    N, M = map(int, input().split())
    lst = [[0] * (N+2*(M-1))] * (M-1) + [[0] * (M-1) + list(map(int, input().split())) + [0] * (M-1) for _ in range(N)] + [[0] * (N+2*(M-1))] * (M-1)
    sol = 0
    # print(N, M)
    # for i in lst:
    #     print(i)

    max1 = 0
    # 십자가
    for i in range(M-1, N+M-1):
        # print(i)
        for j in range(M-1, N+M-1):
            # print(j)
            temp = 0
            for k in range(1, M):                       # target의 좌우 1, 2 => 1만
                temp += lst[i-k][j] + lst[i+k][j]
            for k in range(1, M):                       # target의 상하 1, 2 => 1만
                temp += lst[i][j-k] + lst[i][j+k]
            temp += lst[i][j]                           # target 지점
            if temp > max1:
                max1 = temp

    # 크로스
    for i in range(M-1, N+M-1):
        print(i)
        for j in range(M-1, N+M-1):
            temp = 0
            for k in range(1, M):                       # target의 좌상 우하
                temp += lst[i-k][j-k] + lst[i+k][j+k]
            for k in range(1, M):                       # target의 우상 좌하
                temp += lst[i-k][j+k] + lst[i+k][j-k]
            temp += lst[i][j]                           # target 지점
            if temp > max1:
                max1 = temp


    print(f'#{t+1} {max1}')