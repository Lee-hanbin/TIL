#BOJ_1337_silver4-올바른 배열

import sys
# input = sys.stdin.readline

N = int(input())
lst = [0]*N
for i in range(N):
    lst[i] =int(input())
lst.sort()
lst.append(-1)
temp = 0
cnt = 0
for i in range(N):
    if temp == 0:
        temp = 1
        continue
    if lst[i+1] == lst[i] + 1:
        temp += 1
    else:
        if cnt < temp:
            cnt = temp
        temp = 0

print(5 - cnt)