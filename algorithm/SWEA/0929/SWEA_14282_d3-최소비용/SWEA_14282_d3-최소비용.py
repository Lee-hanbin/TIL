# SWEA_14282_d3-최소비용

from collections import deque
import sys
sys.stdin = open('sample_input(3).txt')

def bfs():
    queue = deque()
    queue.append((0,0,0))
    visited[0][0] = 0
    while queue:
        w, r, c = queue.popleft()
        h = lst[r][c]                       # 현재 높이
        dr = [-1, 0, 1, 0]
        dc = [ 0, 1, 0,-1]
        for i in range(4):
            tmp = w
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<=n-1 and 0<=nc<=n-1:
                if h < lst[nr][nc]:
                    tmp += 1 + (lst[nr][nc] - h)
                else:
                    tmp += 1
            else:
                continue
            if visited[nr][nc] > tmp:
                visited[nr][nc] = tmp
                queue.append((tmp, nr, nc))

for t in range(int(input())):
    n = int(input())
    lst = [list(map(int, input().split())) for i in range(n)]

    visited = [[float('inf')] * n for _ in range(n)]
    bfs()
    print(f'#{t+1} {visited[n-1][n-1]}')