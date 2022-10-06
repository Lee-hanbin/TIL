# BOJ_15654_silver3_n과m5

'''
자연수 n과m이 주어졌을때, n개의 자연수 중에 m개를 고르는 수열
수열의 요소에 해당하는 값들이 주어진다.
사전순
'''

def f(i,k,r):
    if i == r:
        print(*p)
    else:
        for j in range(k):
            if not used[j]:
                used[j] = True
                p[i] = arr[j]
                f(i+1, k, r)
                used[j] = False


n, m = map(int, input().split())
arr = sorted(list(map(int,input().split())))

p = [0] * m
used = [0] * n

f(0,n,m)