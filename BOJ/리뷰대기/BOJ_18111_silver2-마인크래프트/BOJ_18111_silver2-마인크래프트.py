# BOJ_18111_silver2-마인크래프트

import sys
input = sys.stdin.readline


n, m, b = map(int, input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
H = 0
T = float('inf')
for k in range(257):
    min1 = 0
    max1 = 0
    for i in range(n):
        for j in range(m):
            if lst[i][j] < k:
                min1 += (k - lst[i][j])
            else:
                max1 += (lst[i][j] - k)
    inven = max1 + b
    if inven < min1:
        continue
    sec = 2*max1 +min1
    if sec <= T:
        T = sec
        H = k
print(T, H)