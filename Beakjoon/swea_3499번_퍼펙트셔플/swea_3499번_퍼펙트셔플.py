# swea 3499번 퍼펙트 셔플

global top1, top2
def pop(stack, idx):
    global top1, top2
    if idx == 1:
        top1 -= 1
    else:
        top2 -= 1
    return stack.pop()

for t in range(int(input())):
    N = int(input())
    string = input().split()
    stack1 = []
    stack2 = []
    s = str()
    if N == 1:
        stack1.append(string)
    elif N % 2 == 1:                          #홀수이면
        stack1 = string[0:N//2 +1]          #stack1에 한 개 더 쌓는다.
        stack2 = string[N//2 +1:]
    else:                                   #짝수이면
        stack1 = string[0:N//2]
        stack2 = string[N//2:]              #stack1과 stack2에 동일하게 쌓는다

    # if N % 2 == 1:                          #홀수이면
    #     for i in range(N):                  #stack1에 한 개 더 쌓는다.
    #         if i < N//2 + 1:
    #             stack1.append(string[i])
    #         else:
    #             stack2.append(string[i])
    # else:                                   #짝수이면
    #     for i in range(N):                  #stack1과 stack2에 동일하게 쌓는다.
    #         if i < N//2:
    #             stack1.append(string[i])
    #         else:
    #             stack2.append(string[i])
    stack1, stack2 = stack1[::-1], stack2[::-1]
    top1, top2 = len(stack1) - 1, len(stack2) -1
    while top1 != -1:
        if top2 != -1:
            s += pop(stack1, 1) + ' ' + pop(stack2, 2)
            if top2 != -1:
                s += ' '
        else:
            s += pop(stack1, 1)
    # cnt = 0
    # i = 0
    # while cnt < N:
    #     if cnt % 2 == 0:
    #         s += stack1[i]
    #     else:
    #         s += stack2[i]
    #         i += 1
    #     cnt += 1
    #     if cnt != N:
    #         s += ' '
    print(f'#{t+1} {s}')