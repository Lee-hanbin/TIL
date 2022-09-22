# SWEA_14176_d3-화물도크

import sys
sys.stdin =open('sample_input(3).txt')

T = int(input())
for t in range(1,T+1):
    N = int(input())
    lst = []
    lst_sol = []
    for i in range(N):
        lst.append(tuple(map(int,input().split())))
    lst_sol = sorted(lst,key= lambda x:(x[1],x[0]))
    print(lst_sol)
    cf = lst_sol[0][1]
    sol = 1
    for i in lst_sol:
        if cf <= i[0]:
            sol += 1
            cf = i[1]

    print(f'#{t} {sol}')