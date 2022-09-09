#BOJ_1337_silver4-올바른 배열

import sys
input = sys.stdin.readline

N = int(input())
lst = [0]*N
for i in range(N):
    lst[i] =int(input())
lst.sort()
temp = 0
for i in range(N):
    cnt = 0
    lst_cf = []
    for j in range(5):
        lst_cf.append(lst[i]+j)
    for j in lst_cf:
        if j in lst:
            cnt += 1
    if temp < cnt:
        temp = cnt
print(5 - temp)