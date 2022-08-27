# baekjoon 2578번 빙고

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

garo = [list(map(int, input().split())) for _ in range(5)]      # 가로 빙고 리스트
speak = list(map(int, input().split()))                         # 사회자가 부르는 번호의 순서
for _ in range(4):                                              # 사회자가 부르는 번호의 순서를 1차원 list로
    speak += list(map(int, input().split()))

sero = []
for i in zip(*garo):                    # 세로 빙고 리스트
    sero.append(list(i))
cross1 = []
cross2 = []
for i in range(5):                      # 대각선 빙고 리스트
    cross1.append(garo[i][i])
    cross2.append(garo[i][4 - i])


chk = garo + sero + [cross1] + [cross2] # 모든 빙고 리스트 하나의 2차원 배열로 저장

tell = []
for i in range(11):                     # 3빙고가 나오려면 최소 12개 필요하지만, while문을 깔끔하게 하기 위해 11개만 받음
    tell.append(speak[i])
nxt = 11                                # 사회자가 말할 번호의 숫자
bingo = 0
while nxt < 25 and bingo < 3:           # 25 개 모두 나오거나 빙고가 3개 나올 때까지 반복
    bingo = 0                           # bingo 카운트
    tell.append(speak[nxt])             # 부른 숫자 담기
    nxt += 1
    for i in chk:                       # chk는 모든 bingo의 경우의 수를 list로 생성한 것
        for j in i:                     # bingo가 될 수 있는 5숫자 모두 맞으면 bingo + 1, 아니면 pass
            if j not in tell:
                break
        else:
            bingo += 1
        if bingo == 3:                  # bingo가 3개 되면 나오기
            break

print(nxt)

