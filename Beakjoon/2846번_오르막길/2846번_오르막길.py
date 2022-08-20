# baekjoon 2846번 오르막길

import sys
sys.stdin = open('input3.txt')
input = sys.stdin.readline

global top
def pop(stack):
    global top
    top -= 1
    return stack.pop()

N = int(input())
stack = list(map(int, input().split()))
stack2 = []
set_chk = set()
top = N - 1
while 1:
    switch = 0
    try:
        temp = pop(stack)
        if temp > stack[top]:
            stack2.append(temp)
            if top == 0:
                stack2.append(pop(stack))
                switch = 1
        else:
            stack2.append(temp)
            switch = 1
        if switch == 1:
            set_chk.add(max(stack2) - min(stack2))
            stack2 = []
    except:
        break
print(max(list(set_chk)))

