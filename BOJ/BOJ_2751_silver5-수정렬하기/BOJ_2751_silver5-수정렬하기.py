#BOJ_2751_silver5-수정렬하기

import sys
input = sys.stdin.readline

stack = []
for i in range(int(input())):
    stack.append(int(input()))
stack.sort(reverse=True)
for j in range(len(stack)):
    print(stack.pop())