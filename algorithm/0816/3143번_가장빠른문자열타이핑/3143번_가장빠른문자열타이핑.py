# SWEA 3143번 가장 빠른 문자열 타이핑

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    str1, str2 = input().split()
    idx = []
    total = len(str1)
    total_auto = len(str2)
    cnt = 0
    chk = 0
    while chk < total:
        if str2[0] == str1[chk]:
            idx.append(chk)
        chk += 1
    print(idx)
    for i in range(len(idx)):
        if idx[i] + total_auto > total:
            break
        for j in range(total_auto):
            if str1[idx[i]+j] != str2[j]:
                break
        else:
            cnt += 1

    print(cnt)
    print(f'#{test_case} {total - cnt*(total_auto-1)}')
#하고 싶은거