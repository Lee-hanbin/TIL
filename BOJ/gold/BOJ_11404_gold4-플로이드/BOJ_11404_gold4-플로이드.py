# BOJ_11404_gold4-플로이드

from collections import defaultdict
import sys
input = sys.stdin.readline
def dijkstra(s):
    U = set()
    U.add(s)
    distance = [float('inf') for _ in range(n+1)]
    distance[s] = 0
    idx = s############추가############
    for e, w in graph[s]:
        distance[e] = w
    for _ in range(n+1):
        min_V = float('inf')
        for i in range(n+1):
            if i not in U and min_V > distance[i]:
                min_V = distance[i]
                idx = i
        U.add(idx)
        for e, w in graph[idx]:
            distance[e] = min(distance[e], distance[idx]+w)
    return distance


n = int(input())
m = int(input())
graph = defaultdict(list)
for i in range(m):
    s, e, w = map(int, input().split())
    for i, v in enumerate(graph[s]):
        if v[0] == e:                       # 같은 경로 다른 비용이 들어오는 인풋이 존재!
            if v[1] < w:                    # 따라서 인풋을 받을 때, 비교하면서 작은 비용만 받기
                graph[s][i][1] = v[1]
                break
    else:                                   # 같은 경로 아니면 그냥 추가
        graph[s].append([e, w])

for i in range(1, n+1):
    s = dijkstra(i)[1:]
    for j in s:
        if j == float('inf'):               # 경로가 존재하지 않는 경우, 0으로 바꿔주기
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()