# BOJ_10773_silver4-제로

import sys
input = sys.stdin.readline

N = int(input())
stack = []
for i in range(N):
    stack.append(int(input().strip()))
    if stack[-1] == 0:
        stack.pop()
        stack.pop()
if stack:
    print(sum(stack))
else:
    print(0)