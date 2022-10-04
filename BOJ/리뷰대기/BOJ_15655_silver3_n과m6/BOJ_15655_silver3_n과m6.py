# BOJ_15655_silver3_n과m6

'''
#문제
자연수 n과 m이 주어졌을때, n개의 자연수 중에서 m개를 고른 수열
고른 수열은 오름차순
'''
def nCr(n,r,s):
    if r == 0:
        print(*comb[::-1])
    else:
        for i in range(s, n-r+1):
            comb[r-1] = arr[i]
            nCr(n, r-1, i+1)

n, m = map(int,input().split())

arr = sorted(list(map(int,input().split())))
comb = [0] * m

nCr(n,m,0)