#BOJ_2581_sliver5-소수

import sys
input = sys.stdin.readline


# 에라토스테네스의 체
start = int(input())
end = int(input())
lst = [0] * (end+1)
lst_sol = []

for i in range(2, int(end**0.5)+1):               # 2부터 끝까지
    if lst[i] == 0:                     # 숫자가 초기화 되어 있을때
        for j in range(i*i, end+1, i):  # 배수가 되려면 적오도 2배가 필요
            lst[j] = 1
for i in range(start, end + 1):         # 소수만 출력
    if i != 1 and lst[i] == 0:          # 1은 제외
        lst_sol.append(i)
if lst_sol:
    print(sum(lst_sol))
    print(lst_sol[0])
else:
    print(-1)