# baekjoon 2116번 주사위 쌓기

import sys
import copy
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 윗면 넣으면 아랫면 내보내고 해당 순서쌍을 pop하는 함수
def f(tar, pair_1):                     # 아랫면 tar : 2
    for j, e in enumerate(pair_1):      # e : (2, 4) (3, 5) (1, 6)
        temp = 0                        # temp는 윗면
        if tar == e[0]:                 # target은 아랫면
            temp = e[1]                 # temp = 4
            pair_1.pop(j)               # 해당 순서쌍을 팝
            break
        elif tar == e[1]:
            temp = e[0]
            pair_1.pop(j)
            break
    return temp


# a[0] : 아랫면 a[1] : 윗면
# (0, 5), (1, 3), (2, 4)

N = int(input())
squ = [list(map(int, input().split())) for _ in range(N)]
pair = []

# 1. 모든 정육면체의 순서쌍 만들기
for i, e in enumerate(squ):
    lst = []
    for j in range(3):                   # N = 6
        if j == 0:
            lst.append([e[0],e[5]])
        elif j == 1:
            lst.append([e[1], e[3]])
        else:
            lst.append([e[2],e[4]])
    pair.append(lst)

# 2. 첫 번째 주사위의 윗면 정해서
cf_lst = []
for j in range(1,7):                # 1~6까지 아랫면으로 하는 경우
    temp = 0
    pair_copy = copy.deepcopy(pair) # deepcopy
    tar = j
    for i in pair_copy:
        tar = f(tar, i)             # 윗면을 반환 => 다음 주사위의 아랫면을 뜻함
    for i in pair_copy:             # i는 한 정육면체의 옆면을 뜻함
        if max(i[0]) > max(i[1]):   # 순서쌍으로 정의 해놨으므로 두 순서쌍중 큰게 해당 주사위의 max값
            temp += max(i[0])
        else:
            temp += max(i[1])

    cf_lst.append(temp)             # 첫번째 주사위의 모든 경우의 수의 최대값들을 담은 리스트
print(max(cf_lst))                  # 최대값들 중 최대값
