# BOJ_10989_bronze1-수정렬하기3
# 메모리 8MB 이내 이므로 리스트 생성 x
# 따라서 heapq 도 못씀
import sys
from collections import defaultdict
input = sys.stdin.readline
dict1 = defaultdict(int)
for i in range(int(input())):
    dict1[int(input())] += 1
for i in sorted(dict1):
    for _ in range(dict1[i]):
        print(i)