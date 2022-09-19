#BOJ 11650 silver5 좌표정렬
import sys
input = sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
    x, y = map(int,input().split())
    lst.append((x, y))
lst.sort(key=lambda x: (x[0], x[1]))
for i in lst:
    print(i[0], i[1])