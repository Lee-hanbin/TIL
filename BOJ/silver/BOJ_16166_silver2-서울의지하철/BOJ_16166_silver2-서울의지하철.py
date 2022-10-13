# BOJ_16166_silver2-서울의지하철

from collections import defaultdict, deque

def bfs(root):
    que = deque()
    if root == final:                # 도착역이 서울역이면 0 반환
        return 0
    que.append((root,0))             # 초기값 넣어주기
    visited = set()
    while que:
        v, cnt = que.popleft()
        if v in visited:             # 방문 했으면 pass
            continue
        visited.add(v)               # 방문 안했으면 방문 표시
        for i in dict2[v]:           # 해당 역에 이어져 있는 호선들
            for j in dict1[i]:       # 해당 호선의 역들을 순회
                if j == final:       # 해당 호선에 도착역이 있으면 환승 횟수 반환
                    return cnt
                elif j not in visited:      # 아니고 방문하지 않았으면 큐에 넣기
                    que.append((j,cnt+1))
    return -1
dict1 = defaultdict(list)
dict2 = defaultdict(list)
n = int(input())
lst_sol = []
for i in range(1,n+1):
    size, *station = map(int, input().split())
    dict1[i] = station                              # dict1에는 key :호선, value :역
    for j in range(size):                           # dict2에는 key :역  , value :호선
        dict2[station[j]].append(i)
final = int(input())
print(bfs(0))


