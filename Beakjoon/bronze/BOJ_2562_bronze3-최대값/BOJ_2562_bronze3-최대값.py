#BOJ 2562번 브론즈3 최대값

import sys

max1 = 0
idx = 0
cnt = 0
for i in sys.stdin:
    cnt += 1
    if i == '\n':       # 마지막에 널값이 들어가므로
        break
    if max1 < int(i):
        max1 = int(i)
        idx = cnt
print(max1)
print(idx)
