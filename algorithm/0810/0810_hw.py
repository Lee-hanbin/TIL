#SWea1209번-220810_list2 (2)

for k in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    lst_r_sum = [0]*100
    lst_c_sum = [0]*100
    lst_l_sum = [0]*2

    for i in range(100):    # 행 순회
        for j in range(100):    # 열 순회
            lst_r_sum[i] += arr[i][j]   # 같은 행의 값을 리스트에 저장
            lst_c_sum[j] += arr[i][j]   # 같은 열의 값을 리스트에 저장
            if i == j:  # 우하향 대각선의 합
                lst_l_sum[0] += arr[i][j]
            if i == 100-j-1:    # 좌하향 대각선의 합
                lst_l_sum[1] += arr[i][j]

    lst_chk = lst_l_sum +lst_c_sum +lst_r_sum   # 행,열,대각선의 최대값 리스트

    chk_max = 0
    for i in lst_chk:   # 최종 리스트를 순회하여 최대값 추출
        if chk_max < i:
            chk_max = i
    print(f'#{k+1} {chk_max}')