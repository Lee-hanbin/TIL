#BOJ_10814_silver5-나이순정렬

# 나이순으로 정렬
# 나이가 같으면 입력된 순서로 출력


import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
dict1 = defaultdict(list)

for i in range(N):
    age, name = input().split()
    dict1[int(age)].append(name)

for i in sorted(dict1.keys()):
    for j in dict1[i]:
        print(i, j)



