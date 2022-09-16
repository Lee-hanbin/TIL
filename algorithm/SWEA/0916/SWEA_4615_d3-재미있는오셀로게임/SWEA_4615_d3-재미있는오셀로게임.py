# swea_4615_d3-재미있는 오셀로 게임

import sys
sys.stdin =open('sample_input(1).txt')

for t in range(int(input())):
    N, M = map(int, input().split())
    black, white = 0, 0
    lst = [[-1]*(N+2)] + [[-1]+[0]*N + [-1] for _ in range(N)] + [[-1]*(N+2)]
    # 기본 오셀로 셋팅
    lst[N//2][N//2] = 2
    lst[N//2][N//2+1] = 1
    lst[N//2+1][N//2] = 1
    lst[N//2+1][N//2+1] = 2
    print(lst)
    dr = [-1, 1, 0, 0,-1, 1,-1, 1]  # 상, 하, 좌, 우, 좌상, 우하, 우상, 좌하
    dc = [ 0, 0,-1, 1,-1, 1, 1,-1]
    for i in range(M):
        c, r, chk = map(int, input().split())
        lst[r][c] = chk                                     # 해당 좌표에 흰 or 검 체크
        for j in range(8):                                  # 8방을 체크
            nr = r + dr[j]
            nc = c + dc[j]
            if lst[nr][nc] < 1 or lst[nr][nc] == chk:      # 같은 돌, 빈칸이나 벽이 나오면
                continue
            else:                                          # 다른 돌이 나오면
                if 0 < nr < N and 0 < nc < N:
                    nr = nr + dr[j]                            # 다음 칸도 확인해봐
                    nc = nc + dc[j]
                    # 다음 칸이 0이거나 벽이면 멈춰
                    if lst[nr][nc] < 1:
                        continue
                    cnt = 1
                    # 다음 칸이 같은색이면 멈추고 그 색 뺴고 멈춰
                    # 다른색이면 넘어가서 체크해봐
                    while 1:
                        if lst[nr][nc] > 0 and lst[nr][nc] != chk:                  # 다른 돌이면
                            nr = nr + dr[j]
                            nc = nc + dc[j]
                            lst[nr][nc] = chk
                            cnt += 1
                        else:
                            break
                    nr = r + dr[j]
                    nc = c + dc[j]
                    for _ in range(cnt):
                        lst[nr][nc] = chk
                        if chk == 1:
                            black += 1
                            white -= 1
                        else:
                            white += 1
                            black -= 1
                        nr = nr + dr[j]
                        nc = nc + dc[j]

    print(f'#{t+1} {black} {white}')

