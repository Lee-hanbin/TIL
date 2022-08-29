#SWEA13630번 색칠하기

T = int(input())

for test_case in range(1, T+1):

    N = int(input())    #입력받을 횟수
    map1 = [[0]*10 for _ in range(10)]  #10x10 배열 생성
    cnt, chk = 0, 0 #cnt: 색칠횟수 chk: 보라색 개수

    #N번 돌리기
    while cnt < N:
        x1, y1, x2, y2, case = map(int, input().split())    #두 좌표 입력받기
        if case == 1:   #case 1이면 r(red) 방망이로 0 혼내주고 r이 있으면 pass b(blue) 있으면 p 방망이로 혼내주기
            for i in range(x1 - 1, x2):
                for j in range(y1 - 1, y2):
                    if map1[i][j] == 0:
                        map1[i][j] = 'r'
                    elif map1[i][j] == 'b':
                        map1[i][j] = 'p'
                        chk += 1
                    else:
                        continue
        else:   #case 2이면 b(blue) 방망이로 0 혼내주고 b가 있으면 pass r일 경우에는 p(purple) 방망이로 혼내주기
            for i in range(x1 - 1, x2):
                for j in range(y1 - 1, y2):
                    if map1[i][j] == 0:
                        map1[i][j] = 'b'
                    elif map1[i][j] == 'r':
                        map1[i][j] = 'p'
                        chk += 1
                    else:
                        continue
        cnt += 1

    print(f'#{test_case} {chk}')







# N = int(input())
# lst = [list(map(int, input().split())) for _ in range(N)]
# lst_sol = [0, 0, 10, 10]
# sol = 0
#
# for i in range(4):
#     for j in range(N):
#         if i < 2:
#             if lst_sol[i] < lst[j][i]:
#                 lst_sol[i] = lst[j][i]
#         else:
#             if lst_sol[i] > lst[j][i]:
#                 lst_sol[i] = lst[j][i]
# print(lst_sol)
# sol = (lst_sol[2] - lst_sol[0] + 1) * (lst_sol[3] - lst_sol[1] + 1)
