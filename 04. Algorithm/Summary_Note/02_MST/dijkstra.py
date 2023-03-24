

'''
5 11
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6
'''
from collections import defaultdict
V, E = map(int,input().split())
graph_di = defaultdict(list)
for _ in range(E):
    s, e, weight = map(int,input().split())
    graph_di[s].append((weight, e))
    # graph_di[e].append((weight, s))
    

#1. 구현
def dijkstra(s):
    U = {s}
    distance = [float('inf') for _ in range(V+1)]
    distance[s] = 0

    for weight, e in graph_di[s]:
        distance[e] = weight
    
    for _ in range(V+1):

        min_val = float('inf')

        # idx = -1
        
        for i in range(V+1):
            if i not in U and min_val > distance[i]:
                min_val = distance[i]
                idx = i
        U.add(idx)

        for weight, e in graph_di[idx]:
            distance[e] = min(distance[e], distance[idx] + weight)
    print(distance)
dijkstra(1)


#2. heapq 이용

import heapq

def dijkstra(node):
    dist = [float('inf')] * (V+1)
    dist[node] = 0
    hq = []
    heapq.heappush(hq, [0, node])

    while hq:
        now_w, now_v = heapq.heappop(hq)
        for w, v in graph_di[now_v]:
            w += now_w
            if w < dist[v]:
                dist[v] = w
                heapq.heappush(hq, [w, v])
    return dist
