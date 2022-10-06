# BOJ_24447_silver2-알고리즘수업너비우선탐색4

import sys
input = sys.stdin.readline

from collections import deque, defaultdict
def bfs(root):
    queue = deque()
    queue.append((root,0))
    cnt = 1
    visited[root] = cnt
    depth_lst = [-1] * (n+1)
    while queue:
        v, d = queue.popleft()
        depth_lst[v] = d
        for node in graph[v]:
            if not visited[node]:
                queue.append([node,d+1])
                cnt += 1
                visited[node] = cnt
    return depth_lst
n, m, node = map(int,input().split())
graph = defaultdict(list)
for _ in range(m):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
for i in graph.values():
    i.sort()
visited = [0] * (n+1)
dep = bfs(node)
sol = 0
for i in range(1,n+1):
    sol += visited[i]*dep[i]
print(sol)