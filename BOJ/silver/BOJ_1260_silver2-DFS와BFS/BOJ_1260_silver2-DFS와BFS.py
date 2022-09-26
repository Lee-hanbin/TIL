# # BOJ_1260_silver2-DFS와BFS
#
from collections import deque, defaultdict

N, M, root = map(int,input().split())

graph = defaultdict(list)
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
for i in graph:
    graph[i].sort()
visited_dfs = [root]
def dfs(root):
    for node in graph[root]:
        if node not in visited_dfs:
            visited_dfs.append(node)
            dfs(node)
    return visited_dfs

# visited_bfs = set()
visited_bfs = list()
# visited_bfs.add(root)
visited_bfs.append(root)
def bfs(root):
    queue = deque()
    queue.append(root)
    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if node not in visited_bfs:
                queue.append(node)
                # visited_bfs.add(node)
                visited_bfs.append(node)
    return visited_bfs
print(*dfs(root))
print(*bfs(root))