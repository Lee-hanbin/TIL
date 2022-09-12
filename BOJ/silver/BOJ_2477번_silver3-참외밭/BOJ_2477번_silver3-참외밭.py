# baekjoon 2477번 참외밭

import sys
sys.stdin = open('참외밭_input.txt')
input =sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(6)]
max_garo, max_sero = 0, 0

min_squ = 0
# 최소 직사각형
i = 0
while 1:
    j = (i + 1) % 6
    if lst[i][0] == 1 and lst[j][0] == 3:             # '동' 다음 '남'이 나오는 경우
        min_squ = lst[i][1] * lst[j][1]
        break
    elif lst[i][0] == 2 and lst[j][0] == 4:           # '서' 다음 '북'이 나오는 경우
        min_squ = lst[i][1] * lst[j][1]
        break
    elif lst[i][0] == 4 and lst[j][0] == 1:           # '북' 다음 '동'이 나오는 경우
        min_squ = lst[i][1] * lst[j][1]
        break
    elif lst[i][0] == 3 and lst[j][0] == 2:           # '남' 다음 '서'가 나오는 경우
        min_squ = lst[i][1] * lst[j][1]
        break
    i += 1

# 최대 직사각형
for j in lst:
    if j[0] == 1 or j[0] == 2:          # '동'이나 '서'인 경우
        if max_garo < j[1]:
            max_garo = j[1]
    else:                               # '남'이나 '북'인 경우
        if max_sero < j[1]:
            max_sero = j[1]

max_squ = max_garo * max_sero           # 큰 직사각형의 크기
s = max_squ - min_squ                   # 큰 직사각형 - 작은 직사각형

print(s*N)