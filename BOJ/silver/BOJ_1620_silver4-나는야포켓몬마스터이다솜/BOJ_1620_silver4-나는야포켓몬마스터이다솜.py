# BOJ_1620_silver4-나는야포켓몬마스터이다솜

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
dict1 = dict()
for i in range(1,n+1):
    s = input().strip()
    dict1[str(i)] = s
    dict1[s] = str(i)

for _ in range(m):
    print(dict1[input().strip()])

