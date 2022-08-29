# SWEA 1216 회문2

import sys
sys.stdin = open('input (2).txt')

def pal(str1, max_len, N):
    for i in range(N - max_len):
        if N - i == max_len:
            break
        for k in range(N - max_len - i):
            for j in range((N - i - k) // 2):
                if str1[i + j] != str1[N - 1 - k - j]:
                    break
            else:
                if max_len < N - i - k:
                    max_len = N - i - k
    return max_len
for _ in range(10):
    T = int(input())
    N = 100
    lst = [input() for _ in range(N)]
    lst2 = []
    max_len = 1
    for s in lst:
        max_len = pal(s, max_len, N)
    for i in zip(*lst):
        lst2.append(''.join(i))
    for s in lst2:
        max_len = pal(s, max_len, N)
    print(f'#{T} {max_len}')