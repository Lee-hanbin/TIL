#BOJ_1874_silver2-스택수열

import sys
input = sys.stdin.readline

N = int(input())
stack = [1]                     # 미리 1을 넣어줌
lst_print = []                  # push, pop 표시 담는 리스트
lst = []                        # 원하는 모양을 입력받는 리스트
for i in range(N):
    lst.append(int(input()))
lst = lst[::-1]                 # 후입선출이므로 뒤집는다.
M = lst.pop()                   # 하나씩 pop해서 비교
lst_print.append('+')
i = 2                           # 이미 1이 들어가 있으므로 2부터
while 1:
    if stack and stack[-1] == M:    # 스택에 값이 있고 스택의 가장 윗 값이 원하는 값과 같으면
        stack.pop()                 # 스택에서 팝하고
        lst_print.append('-')       # '-' 선정
        if len(lst) == 0:           # 끝까지 lst를 다 읽었으면 반복문 끝
            break
        M = lst.pop()               # 아니면 lst안에 마지막 값을 반환
    else:                           # 다르면 스택에 다음 값을 넣는다
        stack.append(i)
        lst_print.append('+')       # '+' 선정
        i += 1
    if N + 1 in stack:              # 스택에 지정된 숫자 이상의 값이 푸쉬되면 실패
        lst_print.append('NO')
        break

if lst_print[-1] == 'NO':
    print('NO')
else:
    for i in lst_print:
        print(i)

#    4 3 6 8 7 5 2 1
#    1 2 3 4 5 6 7 8

#    1 2 5 7 8

#    4 3 6 8 7 6 5 2 1