# BOJ_15651_silver3_n과m3

'''
자연수 n과 m이 주어졌을 때, 1 부터 n까지 중에서 m개를 고른 수열
중복 가능
'''

def f(i,k,r):
    if i == r:
        print(*p)
    else:
        for j in range(k):
            p[i] = arr[j]
            f(i+1,k,r)

n, m = map(int,input().split())

arr = list(range(1,n+1))
p = [0] * m
used = [0] * n

f(0,n,m)