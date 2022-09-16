#BOJ_18870_silver2-좌표압축

import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
dict1 = defaultdict(list)
lst_sol = [0]*N                     # x'을 담을 리스트

for i in range(N):                  # 딕셔너리에 key = x좌표값, value = index값
    dict1[lst[i]].append(i)

lst_key = sorted(dict1.keys())      # key 값을 정렬

for i, e in enumerate(lst_key):     # 정렬된 키 값이 x' 좌표와 같음
    for j in dict1[e]:              # value인 list를 순회 하여 해당 인덱스에 x' 좌표 갱신
        lst_sol[j] = i
print(*lst_sol)
