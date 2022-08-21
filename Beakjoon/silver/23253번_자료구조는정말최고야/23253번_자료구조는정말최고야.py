# baekjoon 23253번 자료구조는 정말 최고야
# 하노이의 탑이랑 비슷한 문제
# 아님. 그냥 단순 pop 문제

import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline

cnt_book, cnt_stack = map(int, input().split())
stack_dum = []
chk = 1

top_dum = []    #stack들의 top값을 저장

#스택(더미)에 책 쌓기
for t in range(cnt_stack):
    N = int(input())
    stack_dum.append(list(map(int, input().split())))
    top_dum.append(N-1)

i1 = 0
i2 = 0
while chk < cnt_book:
    # 더미들의 제일 위에 있는 값이 정렬하려는 값에 있으면 pop하고 다음 숫자
    # for i in range(cnt_stack):
    #     print(top_dum[i] ,stack_dum[i][top_dum[i]])
    #     if top_dum[i] != -1 and chk == stack_dum[i][top_dum[i]]:
    #         stack_dum[i].pop()
    #         top_dum[i] -= 1
    #         chk += 1
    #         break
    # else:
    #     break
if chk == cnt_book:
    print('Yes')
else:
    print('No')