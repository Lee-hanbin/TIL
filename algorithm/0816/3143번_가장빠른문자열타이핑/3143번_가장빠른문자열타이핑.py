# SWEA 3143번 가장 빠른 문자열 타이핑

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    str1, str2 = input().split()
    print(f'#{test_case} {len(str1.replace(str2, str(1)))}')

