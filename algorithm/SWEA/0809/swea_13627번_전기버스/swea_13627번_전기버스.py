# swea_ 13627 전기버스

import sys
sys.stdin = open('sample_input(2).txt')

for t in range(int(input())):
    K, N, M = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    map1 = [0]*N
    cnt = 0

    for i in range(M):              # 노선에 충전소를 맵핑
        map1[lst[i]] = 1
    i = 0
    while 1:
        cf, temp = 0, 0
        for j in range(i, K+i+1):   #K만큼 이동하면서 마지막 충전소 위치 반환
            if K+i > N:             #마지막 정류장을 넘어가면 break
                break
            elif map1[j] == 1:
                temp = j

        for da in range(temp+1, N): #다음 충전소의 위치 찾기
            if map1[da] == 1:
                cf = da
                break

        if temp + K < cf:           # 충전을 해도 다음 정류장을 찾지 못하면 실패
            cnt = 0
            break

        i = temp                    # 충전을 하고 출발할 버스 위치
        cnt += 1                    # 충전하면 +1

        if temp + K > N - 1 or temp == N - 1:   # idx를 넘어가거나 마지막 충전소와 종점이 같으면 break
            break


    print(f'#{t+1} {cnt}')