# baekjoon 1966번 silver3 프린터큐

import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


# tc = int(input())
#
# for _ in range(tc):
#     n, idx = map(int, input().split())
#     q = deque(map(int, input().split()))
#     idx_q = deque(range(n))
#
#     cnt = 0
#
#     while q:
#         if q[0] == max(q):
#             cnt += 1
#             q.popleft()
#             if idx_q.popleft() == idx:
#                 print(cnt)
#                 break
#         else:
#             q.rotate(-1)
#             idx_q.rotate(-1)

for T in range(int(input())):
    N, M = map(int, input().split())
    target = list(map(int, input().split()))
    cnt = 0
    i = 0
    while len(target) != 0:
        if target[i] == max(target):      # 우선순위가 같음
            cnt += 1                      # 카운팅
            if i == M:                    # 인덱스도 같으면 break
                break
            if i == len(target) - 1:      # 마지막 인덱스가 pop되면 index 0 으로
                target.pop(i)
                i = 0
            else:                         # 마지막 인덱스가 아니면 index 그대로
                target.pop(i)
                if i < M:                 # 찾는 인덱스보다 작은 인덱스의 값이 pop되면 찾는 인덱스 -1
                    M -= 1
            N -= 1                        # 최대값을 찾으면 큐의 크기 -1
        else:
            i = (i+1) % N                 # 못 찾으면 오른쪽으로 한칸

    print(cnt)
