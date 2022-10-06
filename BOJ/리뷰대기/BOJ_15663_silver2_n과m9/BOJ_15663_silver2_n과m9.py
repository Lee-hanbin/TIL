# BOJ_15663_silver3_n과m9

'''
@문제
자연수 n과 m이 주어졌을 때, n개의 자연수 중에 m개를 고르는 조합
'''

import sys
input = sys.stdin.readline

def f(i,k,r):
    if i == r:
        chk = p[::]
        chk = tuple(chk)
        chk_set.add(chk)        # set 안에 값을 넣기 위해서는 list는 안됨! tuple로 넣기!!
    else:
        for j in range(k):
            if not used[j]:
                used[j] =True
                p[i] =arr[j]
                f(i+1,k,r)
                used[j] = False
n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr = sorted(arr)
chk_set = set()
p = [0] * m
used = [0] * n
f(0, n, m)
chk_set = sorted(list(chk_set))
for i in chk_set:
    print(*i)
