# 파리잡기

import sys
sys.stdin = open('in1.txt')

for t in range(int(input())):
    N, M = map(int, input().split())
    lst = [[0] * (N + 2 * (M - 1))] * (M - 1) + [[0] * (M - 1) + list(map(int, input().split())) + [0] * (M - 1) for _ in range(N)] + [[0] * (N + 2 * (M - 1))] * (M - 1)
    sol = 0

    max1 = 0
    # 십자가
    for i in range(M - 1, N + M - 1):
        # print(i)
        for j in range(M - 1, N + M - 1):
            temp = 0
            temp1 = 0
            temp2 = 0
            for k in range(1, M):
                temp1 += lst[i - k][j] + lst[i + k][j]          # 좌우
                temp1 += lst[i][j - k] + lst[i][j + k]          # 상하
                temp2 += lst[i - k][j - k] + lst[i + k][j + k]  # 좌상우하
                temp2 += lst[i - k][j + k] + lst[i + k][j - k]  # 우상좌하
            temp1 += lst[i][j]                                  # target 지점
            temp2 += lst[i][j]                                  # target 지점

            if temp1 > temp2:
                temp = temp1
            else:
                temp = temp2
            if temp > max1:
                max1 = temp

    print(f'#{t + 1} {max1}')

