# baekjoon 2546번 경비원

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 10 5
# 3
# [(1, 4), (3, 2), (2, 8)]  북, 서, 남
# (2, 3)    남 3

garo, sero = map(int, input().split())
N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
dong = tuple(map(int, input().split()))

dong_st = dong[0]
dong_le = dong[1]

# 동, 서, 남, 북 = 4, 3, 2, 1
i = 0
temp = 0
while i < N:
    cf = dong_le - lst[i][1]
    le = lst[i][1]
    if dong_st == 3 or dong_st == 4:
        tt = (dong_le + lst[i][1]) - (2 * sero - dong_le - le)
    else:
        tt = (dong_le + lst[i][1]) - (2 * garo - dong_le - le)

    if dong_st == 4:                                # 동근이가 동쪽
        if lst[i][0] == 4:
             temp += abs(cf)
        elif lst[i][0] == 3:
            if tt > 0:
                temp += garo + 2 * sero - dong_le - le
            else:
                temp += garo + dong_le + lst[i][1]
        elif lst[i][0] == 2:
            temp += garo + sero - dong_le - le
        else:
            temp += dong_le + garo - le
    elif dong_st == 3:                              # 동근이가 서쪽
        if lst[i][0] == 4:
            if tt > 0:
                temp += garo + 2 * sero - dong_le - le
            else:
                temp += garo + dong_le + lst[i][1]
        elif lst[i][0] == 3:
            temp += abs(cf)
        elif lst[i][0] == 2:
            temp += sero - dong_le +le
        else:
            temp += dong_le + le
    elif dong_st == 2:                              # 동근이가 남쪽
        if lst[i][0] == 4:
            temp += garo + sero - dong_le  - le
        elif lst[i][0] == 3:
            temp += sero + dong_le - le
        elif lst[i][0] == 2:
            temp += abs(cf)
        else:
            if tt > 0:
                temp += sero + 2 * garo - dong_le - le
            else:
                temp += sero + dong_le + lst[i][1]
    else:
        if lst[i][0] == 4:
             temp += garo - dong_le + le
        elif lst[i][0] == 3:
            temp += dong_le + le
        elif lst[i][0] == 2:
            if tt > 0:
                temp += sero + 2 * garo - dong_le - le
            else:
                temp += sero + dong_le + lst[i][1]
        else:
            temp += abs(cf)
    i += 1

print(temp)