# 새로운 버스 노선

import sys
sys.stdin = open('sample_in.txt')

def general(A, B):
    nosun = []
    for i in range(A, B+1):
        nosun.append(i)
    return nosun

def ex(A, B):
    nosun = []
    if A % 2 == 0:                      # 짝수이면
        for i in range(A, B+1, 2):
            nosun.append(i)
    else:                               # 홀수이면
        for i in range(A, B+1, 2):
            nosun.append(i)
    if B not in nosun:
        nosun.append(B)
    return nosun

def sp(A, B):
    nosun = []
    if A % 2 == 0:                      # 짝수이면
        for i in range(A, B+1):
            if i % 4 == 0:
                nosun.append(i)
    else:                               # 홀수이면
        for i in range(A, B+1):
            if i % 3 == 0 and i % 10 != 0:
                nosun.append(i)
    if B not in nosun:
        nosun.append(B)
    if A not in nosun:
        nosun.append(A)
    return nosun

# 1
# 3
# 1 2 5
# 2 3 10
# 3 2 9


for t in range(int(input())):
    sol = 0
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    dict1 ={}
    set1 = set()
    # 버스 종류
    bus = []
    for i in lst:
        bus.append(i[0])
    i = 0

    while i<N:
        A = lst[i][1]                   # 버스 출발
        B = lst[i][2]                   # 버스 종점
        save = []
        if bus[i] == 1:
            save = general(A, B)
        elif bus[i] == 2:
            save = ex(A, B)
        else:
            save = sp(A, B)

        for j in save:
            temp = len(set1)
            set1.add(j)
            if len(set1) > temp:         # 새로운 key가 딕셔너리(set)에 들어오면
                dict1[j] = 1
            else:                       # key가 존재하면 갱신
                dict1[j] += 1
        i += 1


    # 겹치는 노선 최대 몇개
    sol = max(dict1.values())
    print(f'#{t+1} {sol}')