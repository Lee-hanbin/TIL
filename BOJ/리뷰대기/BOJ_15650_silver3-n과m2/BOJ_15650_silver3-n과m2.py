# BOJ_15650_silver3-n과m2.py

'''
@문제
자연수 n과 m이 주어졌을 때, 1부터 n까지의 자연수 중 중복 없이 m개를 고른 수열
오름차순 정렬
'''

def nCr(n,r,s):
    if r == 0:
        print(*comb[::-1])
    else:
        for i in range(s, n-r+1):
            comb[r-1] = arr[i]
            nCr(n, r-1, i+1)

n, m = map(int, input().split())
arr = list(range(1,n+1))
comb = [0] * m
nCr(n,m,0)

