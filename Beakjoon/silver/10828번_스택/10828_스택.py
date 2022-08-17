# 10828 스택 silver 4

import sys
sys.stdin = open('input2.txt')

top = -1
stack = [0]*10000

t = int(input())
for test in range(t):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push':
        top += 1
        stack[top] = command[1]
    elif command[0] == 'top':
        if top == -1:
            print(-1)
        else:
            print(stack[top])
    elif command[0] == 'size':
        print(top+1)
    elif command[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif command[0] == 'pop':
        if top == -1:
            print(-1)
        else:
            top -= 1
            print(stack[top+1])
