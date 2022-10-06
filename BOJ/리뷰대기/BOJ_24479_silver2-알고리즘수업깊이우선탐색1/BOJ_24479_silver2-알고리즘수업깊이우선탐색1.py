# BOJ 24479 silver2 알고리즘 수업- 깊이 우선 탐색1
from collections import defaultdict
import sys
input = sys.stdin.readline


def dfs(root):
#     if root not in visited:
#         visited.append(root)
#     for node in graph[root]:
#         if node not in visited:
#             visited.append(node)
#             dfs(node)
    cnt = 1
    stack = [root]
    visited = [0] * (n+1)
    visited[root] = cnt
    cnt += 1
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = cnt
            cnt += 1
        for node in graph[v]:
            if not visited[node]:
                stack.append(node)
    return visited
n, m, node = map(int,input().split())
graph = defaultdict(list)
for _ in range(m):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
for i in graph.values():
    i.sort(reverse=True)
visited = []
sol = dfs(node)
for i in sol[1:]:
    print(i)
