# BaekJoon 1158 silver 4 요세푸스문제

import sys
from collections import deque
sys.stdin =open('input.txt')


N, M = map(int, input().split())
dq = deque(i for i in range(1, N+1))            # deque에 값 넣기
sol_lst = []
while len(sol_lst) < N:                         # rotate 한 값 list에 넣기
    for _ in range(M-1):
        dq.rotate(-1)                           # 오른쪽으로 한칸 씩 이동(= 왼쪽으로 한칸씩 밀기)
    sol_lst.append(dq.popleft())
sol = str(sol_lst).replace('[', '<')            # 출력형식 맞춰주기
sol = sol.replace(']', '>')
print(sol)
