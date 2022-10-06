# BOJ_11725_silver2-트리의부모찾기
from pprint import pprint
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# bfs
def bfs(root):
    que = deque()
    que.append(root)
    visited[root] = 1               # 방문 표시
    while que:
        v = que.popleft()
        for i in graph[v]:
            if not visited[i]:
                parents[i] = v      # 부모 노드를 입력
                que.append(i)
                visited[i] = 1      # 방문 표시
n = int(input())
root = 1
graph = defaultdict(list)
for _ in range(n-1):
    s, e = map(int, input().split())        # 무방향 그래프 입력 받기
    graph[s].append(e)
    graph[e].append(s)
visited = [0] * (n+1)
parents = [0] * (n+1)

bfs(root)

for i in parents[2:]:           # 2번 노드부터 출력
    print(i)


