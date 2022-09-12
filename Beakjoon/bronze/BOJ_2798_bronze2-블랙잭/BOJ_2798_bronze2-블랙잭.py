#BOJ_2798_bronze2-블랙잭

import sys
input = sys.stdin.readline

N, sol = map(int, input().split())
lst = list(map(int, input().split()))
set_sol = set()
switch = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(i+2, N):
            if j == k:                          # 중복 패스
                break
            M = lst[i] + lst[j] + lst[k]
            if M <= sol:
                set_sol.add(M)
lst_sol = list(set_sol)
lst_sol.sort()
print(lst_sol[-1])