# swea 1959 두개의 숫자열

import sys
sys.stdin = open('두개의숫자열.txt')

for t in range(int(input())):
    sol = 0
    N, M = list(map(int, input().split()))
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    sol = 0
    if N > M:                               # lst1 의 길이가 lst2의 길이보다 클때
        for i in range(len(lst1)-len(lst2) + 1):
            temp = 0
            for j, e in enumerate(lst2):
                temp += lst1[i+j] * lst2[j]
            if sol < temp:
                sol = temp
    else:
        for i in range(len(lst2)-len(lst1) + 1):
            temp = 0
            for j, e in enumerate(lst1):
                temp += lst2[i+j] * lst1[j]
            if sol < temp:
                sol = temp
    print(lst1, lst2)
    print(f'#{t+1} {sol}')