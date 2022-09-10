#SWEA_1961_d2-숫자배열회전

import sys
sys.stdin =open('input.txt')

for t in range(int(input())):
    N = int(input())
    lst = []
    lst2 = []
    lst3 = []
    lst4 = []
    for j in range(N):
        lst.append(list(input().split()))
    for i in range(N):
        sol = str()
        sol2 = str()
        for j in range(N):
            sol += lst[j][i]
            sol2 += lst[N-i-1][N-j-1]
        lst2.append(sol[::-1])
        lst3.append(sol2)
    for i in zip(*lst):
        lst4.append(list(i))
    lst = []
    for i in range(N):
        sol2 = str()
        for j in range(N):
            sol2 += lst4[N-i-1][j]
        lst.append(sol2)
    print(f'#{t+1}')
    for i in range(N):
        print(lst2[i] ,end=' ')
        print(lst3[i] ,end=' ')
        print(lst[i])
