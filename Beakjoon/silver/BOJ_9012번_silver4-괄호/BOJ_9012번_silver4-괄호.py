# baekjoon 9012 괄호

import sys
input = sys.stdin.readline
global top

#push함수
def push(stack, s):
    global top
    if top != -1 and s == ')' and stack[top] == '(':
        pop(stack)
    else:
        top += 1
        stack.append(s)
#pop함수
def pop(stack):
    global top
    top -= 1
    stack.pop()

for t in range(int(input())):
    s = list(input())
    s = s[:len(s)-1]
    stack = []
    top = -1
    for i in range(len(s)):
        push(stack, s[i])
    if top == -1:
        print('YES')
    else:
        print('NO')

