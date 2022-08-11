#1954번-달팽이 숫자

N = int(input())
for test_cnt in range(N):
    M = int(input())                    # 정사각행렬의 한 행의 크기
    lst = [[0]*M for _ in range(M)]     # 정사각행렬 정의
    tmp1, tmp2 = 0, M-1                 # tmp1 : 달팽이가 지나갈 수 있는 최소값
    i, j = 0, 0                         # tmp2 : 달팽이가 지나갈 수 있는 최대값
    cnt = 1                             # 행렬에 찍힐 숫자
    lst[0][0] = 1                       # 첫 값 정의
    while cnt < M * M:                  # 행렬의 마지막 값까지 반복
        if i == tmp1 and j < tmp2:      # 행이 최소값일 때 열이 최대가 될때까지 우측이동
            j += 1
        elif i < tmp2 and j == tmp2:    # 열이 최대값일 때 행이 최대가 될때까지 하방이동
            i += 1
        elif i == tmp2 and j > tmp1:    # 행이 최대값일 때 열이 최소가 될때까지 좌측이동
            j -= 1
        elif i > tmp1 and j == tmp1:    # 열이 최소값일 때 행이 최소가 될때까지 상방이동
            i -= 1
            if i == tmp1:               # 달팽이가 올라가다가 벽에 닿으면 우측으로 틀어주고
                i += 1                  # 오른쪽으로 가다가 벽에 닿으면 좌측으로 틀어준다.
                j += 1
                tmp1 += 1
                tmp2 -= 1
        cnt += 1
        lst[i][j] = cnt
    print(f'#{test_cnt+1}')
    for k in range(M):
        for l in range(M):
            print(lst[k][l], end=' ')
        print()
