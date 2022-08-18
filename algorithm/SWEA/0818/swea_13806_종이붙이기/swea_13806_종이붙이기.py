# swea_13086 종이붙이기
#
# import sys
# sys.stdin = open('sample_input (1).txt')

def fec(n):
    sol = 1
    for i in range(1, n + 1):
        sol *= i
    return sol

def combi(n, i):
    return int(fec(n)/(fec(n-i)*fec(i)))

def even_num(N):
    cnt = 0
    N = N // 2
    for i in range(N+1):
        cnt += (2**i)*combi(N, N - i)
    return cnt

def odd_num(N):
    cnt = 0

# print(combi(3,0), combi(3,1), combi(3,2), combi(3,3))
for t in range(int(input())):
    N = int(input())
    cnt = 0
    N = N//10
    if N % 2 == 0:
        cnt = even_num(N)
    else:
        cnt = odd_num(N)

    print(f'#{t+1} {cnt}')


    #10+4+2
    #32+48+24+4 =108-24 = 84
