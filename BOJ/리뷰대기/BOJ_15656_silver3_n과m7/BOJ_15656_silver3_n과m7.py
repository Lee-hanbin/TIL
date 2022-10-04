# BOJ_15656_silver3_n과m7

'''
@문제
n과 m이 주어졌을때, 길이가 m인 수열을 구하시오.
n개의 자연수 중에서 m 개를 고른 수열
중복 수열
'''

def f(i,k,r):
    if i == r:
        print(*p)
    else:
        for j in range(k):
            p[i] = arr[j]
            f(i+1,k,r)

n, m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
p = [0] * m

f(0,n,m)