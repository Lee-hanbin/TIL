# BOJ_24446_silver2-알고리즘수업너비우선탐색3

import sys
input = sys.stdin.readline

from collections import deque, defaultdict
def bfs(root):
    queue = deque()
    queue.append((root,0))
    visited[root] = 1
    depth_lst = [-1] * (n+1)
    while queue:
        v, d = queue.popleft()
        depth_lst[v] = d
        for node in graph[v]:
            if not visited[node]:
                queue.append([node,d+1])
                visited[node] = 1
    return depth_lst
n, m, node = map(int,input().split())
graph = defaultdict(list)
for _ in range(m):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [0] * (n+1)
sol = bfs(node)
for i in sol[1:]:
    print(i)