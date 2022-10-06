# BOJ_15652_silver3_n과m4
'''
@문제

자연수 n과 m이 주어졌을 때, 1부터 n까지 자연수 중에 m객를 고르는 수열
같은 수를 여러 번 골라도 됨
고른 수열은 비내림차순
'''

def f(i,k,r):
    if i == r:
        print(*p)
    else:
        for j in range(k):
            p[i] = arr[j]
            if i > 0 and p[i-1] > p[i]:
                continue
            f(i+1,k,r)
n, m = map(int,input().split())

arr = list(range(1,n+1))
p = [0] * m
used = [0] * n

f(0,n,m)