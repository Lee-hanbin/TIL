# BOJ_24444_silver2-알고리즘수업너비우선탐색1

import sys
input = sys.stdin.readline

from collections import deque, defaultdict
def bfs(root):
    queue = deque()
    queue.append(root)
    cnt = 1
    visited[root] = cnt
    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if not visited[node]:
                queue.append(node)
                cnt +=1
                visited[node] = cnt
n, m, node = map(int,input().split())
graph = defaultdict(list)
for _ in range(m):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
for i in graph.values():
    i.sort()

visited = [0] * (n+1)
bfs(node)
for i in visited[1:]:
    print(i)