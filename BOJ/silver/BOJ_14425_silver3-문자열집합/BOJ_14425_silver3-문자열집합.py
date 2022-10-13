# BOJ_14425_silver3-문자열집합

import sys
input = sys.stdin.readline

n, m = map(int,input().split())

s1 = set()
cnt = 0
for _ in range(n):
    s1.add(input().strip())

for _ in range(m):
    s2 = input().strip()
    if s2 in s1:
        cnt +=1

print(cnt)