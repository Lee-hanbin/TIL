#swea 1224번 계산기3

import sys
sys.stdin = open('input.txt')

for t in range(10):
    sol = 0
    N = int(input())
    s = input()
    stack = []
    huwi = str()
    dict_cf = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    # 중위표기법 -> 후위표기법
    for i in s:
        if i.isdigit():                         # 숫자면 후위표기식에 추가
            huwi += i
        else:
            if len(stack) == 0:                     # 스택이 비어있으면 push
                stack.append(i)
            elif i == ')':  # 닫는괄호면
                while stack:  # 스택에 값이 있을때까지
                    if stack[-1] == '(':  # 여는 괄호가 나오면 pop하고 멈춤
                        stack.pop()
                        break
                    else:  # 아니면 모두 pop해서 후위표기식에 추가
                        huwi += stack.pop()
            elif i == '(':
                stack.append(i)
            elif dict_cf[i] > dict_cf[stack[-1]]:           # 나보다 작은거 만나면 쌓아
                stack.append(i)
            else:                                             # 나보다 큰 거나 같은거 만나면
                while 1:     # + <=
                    if stack:                               # ( + (  + *    , *       ( + ( +    ,  *
                        if stack[-1] == '(':
                            stack.append(i)
                            break
                        if dict_cf[i] > dict_cf[stack[-1]]:
                            stack.append(i)
                            break
                        else:
                            huwi += stack.pop()                 # ( + ( +  *    , *  =>   ( + ( +
                    else:
                        stack.append(i)
                        break
    while stack:
        huwi += stack.pop()
    # 후위연산자 -> 계산
    for i in huwi:
        temp1 = 0
        temp2 = 0
        temp_sol = 0
        if i.isdigit():
            stack.append(i)
        else:
            temp2 = int(stack.pop())
            temp1 = int(stack.pop())
            if i == '+':
                temp_sol = temp1 + temp2
            elif i == '-':
                temp_sol = temp1 - temp2
            elif i == '*':
                temp_sol = temp1 * temp2
            elif i == '/':
                temp_sol = temp1 / temp2
            stack.append(temp_sol)

    print(f'#{t+1} {temp_sol}')


