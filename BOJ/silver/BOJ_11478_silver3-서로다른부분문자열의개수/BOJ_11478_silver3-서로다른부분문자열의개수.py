# BOJ_11478_silver3-서로다른부분문자열의개수

import sys
input = sys.stdin.readline

s = input().strip()
set1 = set()
length = len(s)
for i in range(length+1):
    for j in range(i+1,length+1):
        set1.add(s[i:j])
print(len(set1))