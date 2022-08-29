# swea 13624번 숫자카드 d2

import sys
sys.stdin = open('1.txt')

for t in range(int(input())):
    N = int(input())
    s = input()
    num, cnt = 0, 0
    dict1 = {}
    set1 = set()
    temp = 0
    for i in range(N):
        set1.add(s[i])
        if len(set1) > temp:
            temp = len(set1)
            dict1[s[i]] = 1
        else:
            dict1[s[i]] += 1
    cnt = max(dict1.values())
    for k, v in dict1.items():
        if v == cnt:
            if num < int(k):
                num = int(k)


    print(f'#{t+1} {num} {cnt}')