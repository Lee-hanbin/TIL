#BOJ_1085_bronze3-직사각형에서탈출

import sys
input = sys.stdin.read


x, y, w, h = map(int,input().split())
lst = []
lst.append(abs(x-w))
lst.append(abs(x-0))
lst.append(abs(y-h))
lst.append(abs(y-0))
print(min(lst))