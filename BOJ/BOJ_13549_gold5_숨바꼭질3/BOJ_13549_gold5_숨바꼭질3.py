# BOJ_13549_gold5_숨바꼭질3

import sys
input = sys.stdin.readline
from collections import deque

def bfs(n, m):
    queue = deque()
    queue.append([n,0])             # [수빈이 위치, second]
    visited = set()
    while queue:
        v, sec = queue.popleft()    # v: 수빈이 위치 , sec : 걸린 시간
        visited.add(v)              # 방문 표시
        if v == m:                  # 수빈이가 동생에게 도착하면 끝
            return sec
        sec += 1
        if 2*v not in visited and 0 <= 2*v <= 100000:    # 2*v 에 방문한 적이 없고 max값보다 작을때
            queue.append([2*v,sec-1])               # 순간이동을 할때는 시간이 안 걸리므로
            visited.add(2*v)
        if v-1 not in visited and v-1 >= 0:         # v-1 에 방문한 적이 없고 0보다 클때
            queue.append([v-1,sec])
            visited.add(v-1)
        if v+1 not in visited and 0<= v+1 <= m:    # v+1 에 방문한 적이 없고 max값보다 작을때
            queue.append([v+1,sec])
            visited.add(v+1)


n, m = map(int, input().split())


print(bfs(n,m))