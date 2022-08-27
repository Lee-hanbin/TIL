# baekjoon 2536 색종이 bronze 1

import sys
sys.stdin = open('input.txt')
# input =sys.stdin.readline

lst = [[0] * 100 for _ in range(100)]   # 100 by 100

N = int(input())
color = [tuple(map(int, input().split())) for _ in range(N)]
cnt = 0
for k in range(N):
    x = color[k][0]                 # 좌측하단 x값
    y = color[k][1]                 # 좌측하단 y값
    for i in range(10):
        for j in range(10):
            if lst[x+i][y+j] == 0:  # 색종이가 체크 안 되어 있었으면  체크하고cnt
                lst[x+i][y+j] = ' '
                cnt += 1

print(cnt)
# for i in lst:
#     print(*i)

