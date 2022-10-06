# BOJ_16166_silver2-서울의지하철

from collections import defaultdict, deque
from pprint import pprint

def bfs(start):
    que = deque()
    que.append(station[start][0])
    visited = set()
    visited.add(start)
    while que:
        v, hosun, trans = que.popleft()
        visited.add(v)
        if v == T:
            sol.append(trans)
        for i in station[v]:
            if i[0] not in visited:
                if i[1] != hosun:
                    trans += 1
                que.append((i[0], i[1], trans))
    if not sol:
        sol.append(-1)
    return sol

N = int(input())
station = defaultdict(list)
ho = defaultdict(list)
sol = []

for i in range(1, N+1):
    tmp_lst = list(map(int,input().split()))
    ho[i] = tmp_lst[1:]
    for j, e in enumerate(tmp_lst):
        if j == 0:
            continue
        elif j == 1 and len(tmp_lst) > 2:
            station[tmp_lst[j]].append((tmp_lst[j+1],i,0))
        elif j == len(tmp_lst)-1:
            station[tmp_lst[j]].append((tmp_lst[j-1],i,0))
        else:
            station[tmp_lst[j]].append((tmp_lst[j-1],i,0))
            station[tmp_lst[j]].append((tmp_lst[j+1],i,0))
chk = 0
T = int(input())

print(min(bfs(0)))
