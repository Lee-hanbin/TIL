# swea_4876 미로

import sys
sys.stdin = open('sample_input(4).txt')

def f(r, c):
    cnt = 0
    cf = ()
    map1[r][c] = ' '            # 영역 표시
    for i in range(4):          # 네 방향을 검사해서 갈림길 여부를 찾아
        nx = dx[i] + r
        ny = dy[i] + c
        if map1[nx][ny] == 0:   # 길을 찾으면 counting하고 다음에 이동할 좌표를 갱신해
            cnt += 1
            cf = (nx, ny)
        elif map1[nx][ny] == 3:
            return (nx, ny)
    if cnt > 1:                 # 갈림길이면 좌표를 튜플로 스택에 쌓아
        stack.append((r, c))
    elif cnt == 0:              # 막다른 길이면
        if stack:               # 막다른 길인데 스택이 쌓여 있으면 pop
            cf = stack.pop()
        else:                   # 막다른 길인데 스택이 비어 있으면 x
            cf = (0, 0)
    return cf

for t in range(int(input())):
    N = int(input())
    map1 = [[1] * (N+2)] + [[1] + list(map(int, input())) + [1] for _ in range(N)] + [[1] * (N+2)]
    stack = []
    tu = tuple()
    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    # 초기 미로 출력
    for i in map1:
        print(*i)

    # 1. 미로의 시작점을 튜플에 저장
    for i in range(1, N+1):
        for j in range(1, N+1):
            if map1[i][j] == 2:
                tu = (i, j)

    # 2. 미로의 도착점에 도달하거나 막다른길에 stack에 쌓인 갈림길도 없으면 나오는 반복문
    while tu != (0, 0):
        start_x = tu[0]
        start_y = tu[1]
        if map1[start_x][start_y] == 3:
            break
        else:
            tu = f(start_x, start_y)

    # 최종위치
    # 못 찾으면 (0, 0) 출력
    print(tu)

    # 길찾기를 마친 후, 미로 출력
    for i in map1:
        print(*i)

    if tu == (0, 0):
        print(f'#{t+1} 0')
    else:
        print(f'#{t+1} 1')


