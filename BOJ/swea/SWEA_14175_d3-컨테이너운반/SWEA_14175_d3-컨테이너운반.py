# SWEA_14175_d3-컨테이너운반

import sys
sys.stdin = open('sample_input(2).txt')

T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    # 내림차순 정렬
    # 필요한 개수만큼 슬라이싱
    # pop을 활용하기 위해 다시 오름차순 정렬
    if N > M:
        # lst_N = sorted(list(map(int,input().split())))[::-1][:M][::-1]
        lst_N = sorted(list(map(int,input().split())))
        lst_M = sorted(list(map(int,input().split())))
    else:
        # lst_N = sorted(list(map(int,input().split())))[::-1][:N][::-1]
        lst_N = sorted(list(map(int,input().split())))
        lst_M = sorted(list(map(int,input().split())))[::-1][:N][::-1]
    sol = 0
    # 트럭의 적재용량이 컨테이너의 무게보다 큰 경우에만 더해줌
    while lst_M and lst_N:
        tmp = lst_M[-1]
        if tmp < lst_N[-1]:
            lst_N.pop()
        else:
            sol += lst_N.pop()
            lst_M.pop()
    print(f'#{t} {sol}')