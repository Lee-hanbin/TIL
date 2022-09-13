#SWEA_1231_d4-중위순회

import sys
sys.stdin = open('input.txt')

def find_root(N):
    for i in range(1, N+1):
        if par[i] == 0:
            return i

def inorder(N):
    if N:
        inorder(ch1[N])
        print(lst_str[N-1], end='')
        inorder(ch2[N])

for t in range(10):
    N = int(input())
    lst_str = []
    arr = []
    for i in range(N):
        lst = list(input().split())
        lst_str.append(lst[1])
        for j in range(2, len(lst)):
            arr.append(int(lst[0]))
            arr.append(int(lst[j]))

    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    par = [0] * (N+1)
    for i in range(N-1):
        p, c = arr[i*2], arr[i*2+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
        par[c] = p
    print(f'#{t+1}',end=' ')
    root = find_root(N)
    inorder(root)
    print()
