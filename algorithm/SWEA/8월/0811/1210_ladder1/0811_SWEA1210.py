# SWEA 1210 Ladder1

for test_case in range(1, 11):
    T = int(input())
    #사다리 받기
    lst = [list(map(int, input().split())) for _ in range(100)]
    #사다리 뒤집기 (얕은복사라서 x축으로 회전이동만 된다)
    lst = lst[::-1]
    chk = 0
    y = 1   # 도착점의 세로는 좌우 의미 없으므로 시작점의 다음 칸부터 시작

    #사다리 도착점 찾기
    for x in range(100):
        if lst[0][x] == 2:
            chk = x
            break

    # 마지막까지 가면 스탑
    while y < 100:
        lst[y][chk] = ' ' #지나간 길은 2로 표시
        # 우측이 벽이 아니고 우측에 길이 있으면 우측으로 이동
        if chk + 1 < 100 and lst[y][chk + 1] == 1:
            chk += 1
        # 좌측이 벽이 아니고 좌측에 길이 있으면 좌측으로 이동
        elif chk - 1 > 0 and lst[y][chk - 1] == 1:
            chk -= 1
        # 좌우에 길이 없으면 전진
        else:
            y += 1
    # 완성 사다리 출력
    # for i in range(100):
    #     for j in range(100):
    #         print(lst[i][j], end='')
    #     print()
    #사다리 출발점
    print(f'#{T} {chk}')

