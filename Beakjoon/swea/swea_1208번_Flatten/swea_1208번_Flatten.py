# swea 1208번 Flatten d3

import sys
sys.stdin = open('input.txt')

def dump(lst):
    high, low = max(lst), min(lst)
    lst_idx = 0
    for i in range(len(lst)):
        if high == lst[i]:
            lst_idx = i
            break
    for i in range(len(lst)):
        if low == lst[i]:
            lst[lst_idx] -= 1
            lst[i] += 1
            break
    return max(lst) - min(lst)

for t in range(10):
    N = int(input())
    lst = list(map(int, input().split()))
    chk = 0
    for _ in range(N):
        chk = dump(lst)
        if chk == 0 or chk == 1:
            break

    print(f'#{t+1} {chk}')