# BOJ_12851_gold4-숨바꼭질2
import sys
input = sys.stdin.readline
from collections import deque

def bfs(n, m):
    if n == m:
        return 0, 1
    queue = deque()
    queue.append([n,0])             # [수빈이 위치, second]
    visited = set()
    cnt, chk = 0, 0
    while queue:
        v, sec = queue.popleft()    # v: 수빈이 위치 , sec : 걸린 시간
        visited.add(v)              # 방문 표시
        if v == m and chk == 0:                  # 수빈이가 동생에게 도착하면 끝
            chk = sec
            cnt += 1
        elif v==m and sec == chk:
            cnt += 1
        if chk and sec > chk:
            return chk, cnt
        sec += 1
        if 2*v not in visited and 0 <= 2*v <= 100000:    # 2*v 에 방문한 적이 없고 max값보다 작을때
            queue.append([2*v,sec])
        if v-1 not in visited and v-1 >= 0:         # v-1 에 방문한 적이 없고 0보다 클때
            queue.append([v-1,sec])
        if v+1 not in visited and 0<= v+1 <= m:    # v+1 에 방문한 적이 없고 max값보다 작을때
            queue.append([v+1,sec])
    return chk, cnt
n, m = map(int, input().split())

s1, cnt = bfs(n, m)

print(s1)
print(cnt)