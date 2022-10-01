# swea 13807 괄호검사

import sys
sys.stdin = open('sample_input(1).txt')

global top

#push함수
def push(stack, s):
    global top
    if top != -1 and s == ')' and stack[top] == '(':
        pop(stack)
    elif top != -1 and s == '}' and stack[top] == '{':
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
    s = input()
    stack = []
    top = -1
    for i in s:
        if i == '{' or i == '(' or i == '}' or i == ')':
            push(stack, i)
            print(stack)
    if top == -1:
        print(f'#{t + 1} 1')
    else:
        print(f'#{t + 1} 0')

