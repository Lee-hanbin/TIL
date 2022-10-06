#swea 1223번 계산기2


import sys
sys.stdin = open('input.txt')

for t in range(10):
    N = int(input())
    s = input()
    stack = []
    s2 = str()
    top = -1

    # 중위표기법 -> 후위표기법
    for i in s:
        if i.isdigit():                         # 숫자이면 반복해
            s2 += i
        elif i == '+':                          # '+'이면 다 pop해 <-- 우선순위가 가장 낮으니까
            while top > -1:
                if stack[top] == '+' or '*':
                    s2 += stack.pop()
                    top -= 1
            stack.append(i)                     # 다 pop했으면 '+'를 스택에 넣어
            top += 1
        elif i == '*':                          # '*'이면 스택 꼭대기에 '*'가 나오면 pop해
            while top > -1:
                if stack[top] == '*':
                    s2 += stack.pop()
                    top -= 1
                else:                           # '+'이면 멈춰
                    break
            stack.append(i)
            top += 1
    while top > -1:                             # 스택에 남은 거 다 꺼내
        s2 += stack.pop()
        top -= 1

    #후위표기법 -> 계산
    for i in s2:
        temp1 = 0
        temp2 = 0
        if i.isdigit():                         # 숫자면 push
            stack.append(i)
            top += 1
        else:                                   # 숫자가 아니면(연산기호) temp1 + temp2 or temp1 * temp2
            temp2 = int(stack.pop())            # -와 /가 있으면 temp1과 temp2의 순서가 중요
            temp1 = int(stack.pop())            # *연산자는 문자로 된 숫자 연산 불가능 하므로 정수화
            top -= 2
            temp_sol = 0
            if i == '+':
                temp_sol = temp1 + temp2
            else:
                temp_sol = temp1 * temp2

            stack.append(temp_sol)
            top += 1
    print(f'#{t+1} {stack[0]}')
