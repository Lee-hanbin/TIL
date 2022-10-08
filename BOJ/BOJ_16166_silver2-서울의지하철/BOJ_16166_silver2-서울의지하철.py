# BOJ_16166_silver2-서울의지하철

from collections import defaultdict, deque
from pprint import pprint

def bfs(root):
    que = deque()
    if root == final:
        lst_sol.append(0)
        return
    for i in dict1[root]:
        que.append((i, 0))
    visited = set()
    while que:
        v, cnt = que.popleft()
        visited.add(v)
        if v[1] == final:
            lst_sol.append(cnt)
        for i in dict1[v[1]]:
            if i not in visited:
                if v[0] != i[0]:
                    que.append((i,cnt+1))
                else:
                    que.append((i,cnt))
dict1 = defaultdict(list)
n = int(input())
lst_sol = []
for i in range(1,n+1):
    dict1[i] = []
for i in range(1,n+1):
    cnt, *station = map(int, input().split())
    for j in range(len(station)-1):
        dict1[station[j]].append((i,station[j+1]))
final = int(input())
bfs(0)
if len(lst_sol) == 0:
    print(-1)
else:
    print(min(lst_sol))
