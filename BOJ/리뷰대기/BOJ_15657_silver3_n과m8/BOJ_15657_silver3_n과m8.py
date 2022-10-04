# BOJ_15657_silver3_n과m8

'''
@문제
자연수 n과 m이 주어질 때, n개의 자연수 중에서 m개를 고른 수열
중복 수열
비내림차순
'''

def f(i,k,r):
    if i == r:
        print(*p)
    else:
        for j in range(k):
            p[i] = arr[j]
            if i>0 and p[i-1] > p[i]:
                continue
            f(i+1,k,r)

n, m = map(int,input().split())
arr = sorted(list(map(int,input().split())))

p = [0]*m

f(0, n, m)
