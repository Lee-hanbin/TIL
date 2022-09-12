#BOJ_7894_gold3-큰수

import sys, math
input = sys.stdin.readline

lst = []
for _ in range(int(input())):
    N = int(input())
    sol = 0
    for i in range(1, N + 1):
        sol += math.log10(i)        # 상용로그를 통해 곱 대신 합으로 연산을 줄여준다.
    print(int(sol)+1)               # 상용로그에서 자릿수는 +1 한 값

