#BOJ_10818_bronze3-최소,최대

import sys
input = sys.stdin.readline

N = int(input())
lst =list(map(int, input().split()))
print(min(lst), max(lst))