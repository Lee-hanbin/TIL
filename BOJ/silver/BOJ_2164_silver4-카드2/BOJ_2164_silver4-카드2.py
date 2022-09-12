#Baekjoon 2164번 silver4 카드2

import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

dq = deque(i for i in range(1, N+1))            # deque에 값 넣기

while len(dq) != 1:         # deque에 숫자가 하나 남을 때까지 반복
    dq.popleft()            # 첫번째 숫자 버리고
    dq.rotate(-1)           # 두번째 숫자 끝으로
print(dq.pop())             # 마지막 남은 숫자 pop