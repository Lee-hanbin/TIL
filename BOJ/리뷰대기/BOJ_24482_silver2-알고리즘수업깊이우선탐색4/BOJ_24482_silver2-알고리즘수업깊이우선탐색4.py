# BOJ_24482_silver2-알고리즘수업깊이우선탐색4

from collections import defaultdict
import sys
input = sys.stdin.readline


def dfs(root):
    stack = [(root,0)]
    visited = [0] * (n+1)
    chk = [-1] * (n+1)
    chk[root] = 0
    visited[root] = 1
    while stack:
        v,d = stack.pop()
        if not visited[v]:
            visited[v] = 1
            chk[v] = d
        for node in graph[v]:
            if not visited[node]:
                stack.append((node,d+1))
    return chk
n, m, node = map(int,input().split())
graph = defaultdict(list)
for _ in range(m):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
for i in graph.values():
    i.sort()
sol = dfs(node)
for i in sol[1:]:
    print(i)
