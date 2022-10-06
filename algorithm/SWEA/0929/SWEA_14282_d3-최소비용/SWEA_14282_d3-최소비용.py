# SWEA_14282_d3-최소비용

from collections import deque
import sys
sys.stdin = open('sample_input(3).txt')

<<<<<<< HEAD
=======
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

>>>>>>> dd450b790df1b48e224e9a4c04e5571b8b916b85
def bfs():
    queue = deque()
    queue.append((0,0,0))
    visited[0][0] = 0
    while queue:
        w, r, c = queue.popleft()
        h = lst[r][c]                       # 현재 높이
<<<<<<< HEAD
        dr = [-1, 0, 1, 0]
        dc = [ 0, 1, 0,-1]
=======
>>>>>>> dd450b790df1b48e224e9a4c04e5571b8b916b85
        for i in range(4):
            tmp = w
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<=n-1 and 0<=nc<=n-1:
<<<<<<< HEAD
                if h < lst[nr][nc]:
                    tmp += 1 + (lst[nr][nc] - h)
                else:
                    tmp += 1
            else:
                continue
            if visited[nr][nc] > tmp:
                visited[nr][nc] = tmp
                queue.append((tmp, nr, nc))
=======
                tmp += 1
                if h < lst[nr][nc]:
                    tmp += lst[nr][nc] - h
                if visited[nr][nc] > tmp:
                    visited[nr][nc] = tmp
                    queue.append((tmp, nr, nc))
>>>>>>> dd450b790df1b48e224e9a4c04e5571b8b916b85

for t in range(int(input())):
    n = int(input())
    lst = [list(map(int, input().split())) for i in range(n)]
<<<<<<< HEAD

=======
>>>>>>> dd450b790df1b48e224e9a4c04e5571b8b916b85
    visited = [[float('inf')] * n for _ in range(n)]
    bfs()
    print(f'#{t+1} {visited[n-1][n-1]}')