#BOJ_11651_silver5-좌표정렬하기2
N = int(input())
lst = []
for i in range(N):
    x, y = map(int,input().split())
    lst.append((x, y))
lst.sort(key=lambda x: (x[1], x[0]))
for i in lst:
    print(i[0], i[1])