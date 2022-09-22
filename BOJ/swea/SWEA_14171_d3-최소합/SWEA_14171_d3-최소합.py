# SWEA_14171_d3-최소합

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1,T+1):
    N = int(input())

    map_a = [list(map(int,input().split())) for _ in range(N)]

    stack = [(0,0)]
    lst_sol = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if r == 0:                                              # 첫 행일 경우
                lst_sol[r][c] = lst_sol[r][c - 1] + map_a[r][c]     # 첫 행의 이전 값들만 더해줘
            elif c == 0:                                            # 첫 열일 경우
                lst_sol[r][c] = lst_sol[r - 1][c] + map_a[r][c]     # 첫 열의 이전 값들만 더해줘
            elif lst_sol[r-1][c] > lst_sol[r][c-1]:                 # 좌측이 더 작으면 좌측을 더해
                lst_sol[r][c] = lst_sol[r][c-1] + map_a[r][c]
            else:                                                   # 상측이 더 작으면 상측을 더해
                lst_sol[r][c] = lst_sol[r-1][c] + map_a[r][c]

    print(f'#{t} {lst_sol[N-1][N-1]}')