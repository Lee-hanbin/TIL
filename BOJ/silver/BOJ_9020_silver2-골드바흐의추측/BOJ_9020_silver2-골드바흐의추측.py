# BOJ_9020_silver2-골드바흐의추측
import sys
input = sys.stdin.readline

T = int(input())
lst_q = []
for _ in range(T):
    lst_q.append(int(input()))
max1 = max(lst_q)

lst = [0] * (max1+1)
lst_prime = []

for i in range(2, int(max1**0.5)+1):               # 2부터 n개의 값들 중에 가장 큰 값까지
    if lst[i] == 0:                     # 숫자가 초기화 되어 있을때
        for j in range(i*i, max1+1, i):  # 배수가 되려면 적오도 제곱배가 필요
            lst[j] = 1
for i in range(max1 + 1):         # 소수만 출력
    if i != 1 and lst[i] == 0:          # 1은 제외
        lst_prime.append(i)

for t in lst_q:
    lst_sol = []
    n = t
    set_prime = set(lst_prime)      # in을 효율적으로 사용하기 위해 set 하나 복제
    for i in lst_prime:
        if i*2 > n:                 # i의 2배가 n보다 커지면 값이 존재 x
            break
        if n-i in set_prime:        # n-i 도 소수이면 해당 값들을 append
            lst_sol.append((i, n-i))
    print(*lst_sol[-1])             # 제일 마지막에 들어간 값이 최소차이
