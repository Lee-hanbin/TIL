#swea 2005 파스칼 삼각형
import sys
sys.stdin = open('input (2).txt')

#숏코딩
#펙토리얼 함수
def f(n):
    s = 1
    for i in range(n):
        s *= i+1
    return s
for t in range(int(input())):
    print(f'#{t+1}')
    for i in range(int(input())):
        print(*[int(f(i) / (f(i - j) * f(j))) for j in range(i+1)]) #콤비네이션 구현해서 리스트 생성 후 출력

# 스택이용
# global top
#
#
# # push
# def push(lst, num):
#     global top
#     top += 1
#     if top == len(lst):
#         #        print('가득참')
#         top -= 1
#         return False
#     else:
#         lst[top] = num
#
#
# # pop(top만 1 줄여줌)
# def pop():
#     global top
#     top -= 1
#     if top < 0:
#         #        print('바닥')
#         top += 1
#         return False
#     else:
#         print('빼기')
# # 펙토리얼 계산함수
# def fectorial(n):
#     sol = 1
#     for i in range(1, n + 1):
#         sol *= i
#     return sol
#
#
# # 콤비네이션 계산함수
# def combi(n):
#     lst = [1]
#     for i in range(1, n + 1):
#         lst.append(int(fectorial(n) / (fectorial(n - i) * fectorial(i))))  # 파스칼 삼각형의 각 요소들을 계산
#     return lst  # 파스칼 삼각형의 각 행을 lst로 반환
#
#
# t = int(input())
#
# for test_case in range(1, t + 1):
#     print(f'#{test_case}')
#     n = int(input())
#     top = -1
#     stack = [0] * n
#
#     # 파스칼 삼각형의 줄을 하나씩 push
#     for i in range(n):
#         push(stack, combi(i))
#     # 파스칼 삼각형의 줄을 하나씩 pop
#     for i in range(n):
#         print(*stack[i])
#         pop()