# BOJ_9742_silver3-순열

'''
@문제
서로 다른 숫자와 문자로 이루어진 집합과 위치가 주어졌을 때,
순열을 구하여라

@리뷰
출력하는 것이 ... 너무 어려웠다

'''

import sys
input = sys.stdin.readline


def f(i,k,r,num):
    global cnt
    if i == r:
        cnt = cnt + 1
        if cnt == num:
            sol = str()
            for i in p:
                sol += i
            print(f'{line[0]} {line[1]} =', sol)
    else:
        for j in range(k):
            if not used[j]:
                used[j] = True
                p[i] = s[j]
                f(i+1, k, r,num)
                used[j] = False

while 1:
    line = input().rstrip().split()
    if len(line) != 2:
        break
    cnt = 0
    s, num = line
    num = int(num)
    n = len(s)
    s = list(s)
    p = [0] * n
    used = [0] * n

    f(0,n,n,num)
    if cnt < num:
        print(f'{line[0]} {line[1]} = No permutation')