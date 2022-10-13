# BOJ_11047_silver4-동전0

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
lst = []

for i in range(n):
    tmp = int(input().strip())
    if tmp > k:
        continue
    else:
        lst.append(tmp)
sol = k
tmp = lst.pop()
cnt = 0
while sol > 0:

    if sol >= tmp:
        b = sol // tmp
        sol = sol % tmp
        cnt += b
    else:
        tmp = lst.pop()
print(cnt)