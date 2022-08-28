# swea 2805번 농작물수확하기

import sys
import copy
sys.stdin = open('input.txt')

for t in range(int(input())):
    N = int(input())
    lst = [input() for _ in range(N)]
    lst2 = copy.deepcopy(lst)[::-1]
    temp, i, cnt = 0, 0, 0

    while cnt < N//2 +1:
        cnt += 1
        if i < N//2 + 1:                                      # 0 ~ 2
            for j in range(N//2 - i, N//2 + i + 1):         # 2 - 0 ~ 2 + 0 + 1 ==> 2
                temp += int(lst[i][j])
        if i < N//2:                                        # 0 ~ 1
            for j in range(N//2 - i, N//2 + i + 1):         # 2 - 0 ~ 2 + 0 + 1 ==> 2
                temp += int(lst2[i][j])
        i += 1

    print(f'#{t+1} {temp}')