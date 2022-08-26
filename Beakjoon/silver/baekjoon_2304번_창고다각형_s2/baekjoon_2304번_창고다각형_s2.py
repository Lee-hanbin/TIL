# baekjoon 2304번 창고 다각형

import sys
import copy
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 가장 높은 기둥을 만나면 멈추는 함수
def stick_func(max_stick, lst):
    i = 0
    while 1:
        stick = lst[i]                              # 왼쪽 기둥
        while 1:
            if stick[1] == max_stick[1]:            # 가장 높은 기둥을 만나면 ㅌㅌ
                return
            else:
                i += 1
                stick_next = lst[i]                 # 왼쪽의 다음 기둥
                if stick_next[1] < stick[1]:        # 왼쪽기둥의 길이가 그 다음 기둥의 길이보다 긴 경우
                    continue
                else:                               # 벽을 만나면 넓이를 구해서 리스트에 넣는다.
                    lst_s.append(stick[1] * (abs(stick_next[0] - stick[0])))
                    break

N = int(input())

lst_left = []
lst_right = []
for _ in range(N):                                  # 각 기둥의 번호와 크기를 리스트로 입력받는다.
    lst = list(map(int, input().split()))
    lst_left.append(lst)

lst_left.sort()                                     # 기둥의 번호를 key로 잡고 오름차순 정렬
lst_right = copy.deepcopy(lst_left)[::-1]           # 리스트를 카피해서 좌우로 뒤집는다.
# lst_right = lst_right[::-1]

for i in lst_right:                                 # right list는 상자의 가로 길이가 1이므로 더 해준다.
    i[0] += 1

# 가장 높은 기둥 구하기
max_stick = 0
temp = 0
for tu in lst_left:
    if temp < tu[1]:
        temp = tu[1]
        max_stick = tu


# 왼쪽에서의 최대값과 오른쪽에서의 최대값의 번호를 구해라
left_max = 0
right_max = 0
for i in range(len(lst_left)):
    if max_stick[1] == lst_left[i][1]:
        left_max = lst_left[i][0]
        break
for i in range(len(lst_right)):
    if max_stick[1] == lst_right[i][1]:
        right_max = lst_right[i][0]
        break

# 면적 구하기
lst_s = []
stick_func(max_stick, lst_left)                         # 왼쪽에서 시작해서 가장 높은 기둥이 나올때까지 넓이구하기
stick_func(max_stick, lst_right)                        # 오른쪽에서 시작해서 가장 높은 기둥이 나올때까지 넓이구하기
lst_s.append(max_stick[1] * abs(right_max - left_max))  # 가장 높은 지붕의 면적을 구해라
print(sum(lst_s))
