# SWEA 1216 회문2

import sys
sys.stdin = open('input (2).txt')

T = int(input())

for test_case in range(T):
    lst = [input() for _ in range(100)]
    set1 = set()
    for s in lst:
        for i in range(100):
            for j in range((100 - i - 1)//2):
                if s[i+j] != s[(100 - i - 1) -j] and ((99 - j) // 2 + 1) != j:
                    break
                else:




