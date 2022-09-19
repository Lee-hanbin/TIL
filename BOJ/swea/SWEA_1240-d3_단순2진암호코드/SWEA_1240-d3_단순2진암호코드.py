#SWEA_1240-d3_단순2진암호코드

import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    dict1 = {
        '[0, 0, 0, 1, 1, 0, 1]': 0,
        '[0, 0, 1, 1, 0, 0, 1]': 1,
        '[0, 0, 1, 0, 0, 1, 1]': 2,
        '[0, 1, 1, 1, 1, 0, 1]': 3,
        '[0, 1, 0, 0, 0, 1, 1]': 4,
        '[0, 1, 1, 0, 0, 0, 1]': 5,
        '[0, 1, 0, 1, 1, 1, 1]': 6,
        '[0, 1, 1, 1, 0, 1, 1]': 7,
        '[0, 1, 1, 0, 1, 1, 1]': 8,
        '[0, 0, 0, 1, 0, 1, 1]': 9,
    }
    sol = []
    N, M = map(int, input().split())
    lst = [list(map(int,input())) for _ in range(N)]

    # switch = 0
    # for i in range(N):
    #     for j in range(0,M,56):
    #         if lst[i][j:56+j] == [0]*56:               #56개 연속 0 이면 다음 줄
    #             break
    #         if lst[i][j:56+j] == lst[i+1][j:56+j]:     #첫 줄이랑 두번째 줄이 같으면 긁어오기
    #             sol = lst[i]
    #             switch = 1
    #             break
    #     if switch == 1:
    #         break

    for i in range(N):              # 1이 있는 줄이 암호가 존재하므로
        if 1 in lst[i]:
            sol = lst[i]


    for i,e in enumerate(sol[::-1]):                   # 마지막이 1로 끝나므로 슬라이싱해서 끝 값 찾기
        if e == 1:
            idx = i
            break
    sol = sol[M-idx-56:M-idx]                          # 끝 값을 기준으로 슬라이싱
    lst_sol = []
    for i in range(0, 56, 7):                          # 7개씩 끊어서 딕셔너리의 key값과 비교하여 value값출력
        lst_sol.append(dict1[str(sol[i:7+i])])

    tmp_odd = 0
    tmp_even = 0
    for i in range(0, 8, 2):                    # 홀수 합
        tmp_odd += lst_sol[i]
    for i in range(1, 8, 2):                    # 짝수 합
        tmp_even += lst_sol[i]
    if (tmp_odd*3 + tmp_even) % 10 == 0:        # (홀수 합*3) + 짝수 합이 10의 배수 여부
        print(f'#{t} {sum(lst_sol)}')
    else:
        print(f'#{t} {0}')