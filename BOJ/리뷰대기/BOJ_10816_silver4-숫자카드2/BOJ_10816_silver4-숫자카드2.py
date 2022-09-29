#BOJ_10816_silver4-숫자카드2

import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
lst = list(map(int, input().split()))
M = int(input())
lst2 = list(map(int, input().split()))
dict1 = defaultdict(int)
for i in lst:
    dict1[i] += 1
for i in lst2:
    print(dict1[i],end=' ')