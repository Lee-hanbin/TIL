# BOJ_15666_silver2_n과m12

'''
자연수 n과 m이 주어질 때, n개의 자연수 중에 m개를 고르는 수열
중복 순열
비내림차순
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
            if i > 0 and p[i - 1] > arr[j]:     # 체크 표시 되기 전부터 되는 값만 넣기
                continue
            p[i] = arr[j]
            f(i+1,k,r)
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