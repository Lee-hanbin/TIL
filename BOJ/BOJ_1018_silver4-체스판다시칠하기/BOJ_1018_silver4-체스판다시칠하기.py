#BOJ_1018_silver4-체스판다시칠하기

import sys, copy
input = sys.stdin.readline

N, M = map(int, input().split())

lst2 = [list(input().strip()) for _ in range(N)]
lst_cnt = []
for n in range(N-7):
    for m in range(M-7):
        for k in range(2):                  # 첫 칸을 바꾸거나 안바꾸거나
            lst = copy.deepcopy(lst2)
            start = lst[n][m]
            if k == 0:                      # 바꾸면 카운트 1로 시작
                cnt = 1
                if start == "B":
                    lst[n][m] = "W"
                    start = "W"
                else:
                    lst[n][m] = "B"
                    start = "B"
            else:                           # 안 바꾸면 카운트 0으로 시작
                cnt = 0
            for i in range(n, 8+n):
                if n % 2 == i % 2:                          # 첫 행과 같은 행일때
                    if start == "B" and lst[i][m] == "W":   # 시작점과 다르면
                        cnt += 1                            # 바꾸고 카운팅
                        lst[i][m] = "B"
                    elif start == "W" and lst[i][m] == "B":
                        cnt += 1
                        lst[i][m] = "W"
                else:                                       # 첫 행과 다른 행일때
                    if start == "B" and lst[i][m] == "B":   # 시작점과 같으면
                        cnt += 1                            # 바꾸고 카운팅
                        lst[i][m] = "W"
                    elif start == "W" and lst[i][m] == "W":
                        cnt += 1
                        lst[i][m] = "B"

                for j in range(m, 8+m):
                    if j == m:                              # 첫 값 할당
                        tmp = lst[i][j]
                        continue
                    if tmp == lst[i][j]:                    # 연속되는 값이 같으면
                        cnt += 1                            # 카운팅하고 수정
                        if tmp == 'B':
                            tmp = 'W'
                            lst[i][j] = 'W'
                        else:
                            tmp = 'B'
                            lst[i][j] = 'B'
                    else:                                   # 다르면 다음 칸으로
                        tmp = lst[i][j]
            lst_cnt.append(cnt)                             # 카운팅들 수정
print(min(lst_cnt))