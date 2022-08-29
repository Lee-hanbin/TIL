# 고대 유적
import sys
sys.stdin = open('input1.txt')

for t in range(int(input())):
    N, M = map(int, input().split())  # N by M
    map_ori = [list(map(int, input().split())) for _ in range(N)]  # 원래 입력 배열

    map1 = []
    for i in map_ori:  # 배열 끝에 테두리 생성
        map1.append(i + [0])
    lst = []

    max1 = 0
    for i in range(N):
        cnt = 0
        for j in range(M + 1):
            if map1[i][j] == 1:
                cnt += 1
            else:
                lst.append(cnt)
                cnt = 0

    map2 = []
    for i in zip(*map_ori):  # 전치하고 배열 끝에 테두리 생성
        map2.append(list(i) + [0])

    for i in range(M):
        cnt = 0
        for j in range(N + 1):
            if map2[i][j] == 1:
                cnt += 1
            else:
                lst.append(cnt)
                cnt = 0
    max1 = max(lst)

    print(f'#{t + 1} {max1}')
