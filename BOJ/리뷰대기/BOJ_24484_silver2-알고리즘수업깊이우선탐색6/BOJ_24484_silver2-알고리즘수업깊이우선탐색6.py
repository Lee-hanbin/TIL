# BOJ_24484_silver2-알고리즘수업깊이우선탐색6

from collections import defaultdict
import sys
input = sys.stdin.readline


def dfs(root):
    cnt = 1
    stack = [(root,0)]
    visited = [0] * (n+1)
    visited[root] = cnt
    chk = [-1] * (n+1)
    chk[root] = 0
    cnt += 1
    while stack:
        v,d = stack.pop()
        if not visited[v]:
            visited[v] = cnt
            cnt += 1
            chk[v] = d
        for node in graph[v]:
            if not visited[node]:
                stack.append((node,d+1))
    return visited, chk
n, m, node = map(int,input().split())
graph = defaultdict(list)
for _ in range(m):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
for i in graph.values():
    i.sort()
sol_1, sol_2 = dfs(node)
sol = 0
for i in range(1,n+1):
    sol += sol_1[i]*sol_2[i]

print(sol)