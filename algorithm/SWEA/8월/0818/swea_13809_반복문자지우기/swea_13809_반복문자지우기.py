# swea 13809 반복문자 지우기

import sys
sys.stdin=open('sample_input(3).txt')

global top
# push 함수응용
# 스택이 비어있거나 스택의 가장 위의 값이
# 푸쉬하려는 값과 동일하면 pop
# 아니면 push
def push(stack, s):
    global top
    if isempty() == False and stack[top] == s:
        pop()
    else:
        top += 1
        stack[top] = s
# pop 함수
def pop():
    global top
    top -= 1
# empty 함수
def isempty():
    global top
    if top == -1:
        return True
    else:
        return False
#length 함수
def length():
    global top
    return top + 1
for t in range(int(input())):
    top = -1
    s = input()
    lst = [0]*len(s)
    for i in range(len(s)):
        push(lst, s[i])
    print(f'#{t+1} {length()}')