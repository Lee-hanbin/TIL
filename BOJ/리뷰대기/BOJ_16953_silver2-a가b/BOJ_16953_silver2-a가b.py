# BOJ_16953_silver2-a가b

from collections import deque

def bfs(n,m):
    cnt = 0
    que = deque()
    que.append((n,cnt))
    visited = set()
    visited.add(n)
    while que:
        v, chk = que.popleft()
        if v > m:
            continue
        if v == m:
            return chk
        k = int(str(v) + '1')
        if 2*v not in visited and 0 < 2*v < 10**9:
            que.append([2*v,chk+1])
        if k not in visited and 0 < k < 10**9:
            que.append([k,chk+1])
    return -2
n, m = map(int, input().split())

print(bfs(n,m)+1)
