# BOJ_15649_silver3-n과m1

'''
#문제
자연수 n과 m 이 주어짐
1~n까지의 중복 없이 m개를 고르기

'''

def f(i, k, r):
    if i == r:
        print(*p)
    else:
        for j in range(k):
            if not used[j]:
                used[j] = True
                p[i] = a[j]
                f(i+1,k,r)
                used[j] = False


n, m = map(int,input().split())

a = list(range(1,n+1))
used = [0] * n
p = [0] * m
f(0,n,m)