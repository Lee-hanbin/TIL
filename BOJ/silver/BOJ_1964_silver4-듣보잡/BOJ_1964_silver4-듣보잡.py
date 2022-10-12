# BOJ_1964_silver4-듣보잡
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
set1 = set()
set2 = set()
set3 = set()

for i in range(n+m):
    if i < n:
        set1.add(input().strip())
    else:
        set2.add(input().strip())

# for i in range(n):
#     s = set1.pop()
#     if s in set2:
#         set3.add(s)
set3 = sorted(list(set1&set2))
print(len(set3))
for i in set3:
    print(i)

