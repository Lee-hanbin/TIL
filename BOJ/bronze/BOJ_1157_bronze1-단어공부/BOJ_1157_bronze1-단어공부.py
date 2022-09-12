#BOJ 1157 브론즈1 단어공부

import sys
input = sys.stdin.readline

s = input().strip()         # strip은 Null/ space 제거 split은 list형태로 묶어버림
dict1 = {}
set1 = set()
for i in s:
    i = i.upper()           # 모든 문자는 대문자
    chk = len(set1)
    set1.add(i)
    if chk == len(set1):    # set의 크기가 같으면 key값이 존재하므로 갱신
        dict1[i] += 1
    else:                   # set의 크기가 변하면 key값이 없으므로 생성
        dict1[i] = 1

cf = max(dict1.values())    # dictionary의 values 값중 최대값 구하기
cnt = 0

for k, i in dict1.items():  # 딕셔너리에서 최대 value 값이 두 개 이상이면 '?' 출력
    if cf == i:             # 유일하면 유일한 값 출력
        sol = k
        cnt += 1
    if cnt > 1:
        print('?')
        break
else:
    print(sol)