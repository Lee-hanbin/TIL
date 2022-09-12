# swea 13877 forth

import sys
sys.stdin = open('sample_input.txt')

for t in range(int(input())):
    stack = list(input().split())
    stack2 = []
    sol = 0
    temp1 = 0
    temp2 = 0
    for i in stack:
        if i == '.':
            break
        elif i.isdigit():
            stack2.append(i)
        else:
            try:
                temp2 = int(stack2.pop())
                temp1 = int(stack2.pop())
            except:
                sol = 'error'
                break
            if i == '+':
                sol = temp1 + temp2
            elif i == '-':
                sol = temp1 - temp2
            elif i == '*':
                sol = temp1 * temp2
            elif i == '/':
                sol = temp1 // temp2
            else:
                sol = 'error'
                break
            stack2.append(sol)
    if len(stack2) != 1:
        sol = 'error'

    print(f'#{t+1} {sol}')