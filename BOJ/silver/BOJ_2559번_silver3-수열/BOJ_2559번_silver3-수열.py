# BJO 2559 수열 silver 3

import sys
# sys.stdin = open('input.txt')
sys.stdin = open('input2.txt')
input = sys.stdin.readline

# 1개인 경우

# 10 2
# [3, -2, -4, -9, 0, 3, 7, 13, 8, -3]
# 획기적으로 줄여야함

N, K = map(int, input().split())
lst = list(map(int, input().split()))

temp = sum(lst[0:K])
sol = sum(lst[0:K])
i = 0
while i + K < N:
    temp = temp - lst[i] + lst[i+K]
    i += 1
    if sol < temp:
        sol = temp
print(sol)

# temp = sum(lst[0:K])
# sol = temp
# i = 0
# while i + K < N:
#     if lst[i] <= lst[i+K]:
#         temp = sum(lst[i+1:K+i+1])
#         i += 1
#     else:
#         i += 1
#         continue
#     if sol < temp:
#         sol = temp
# print(sol)