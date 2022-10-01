# BOJ_1916_gold5_최소비용구하기

from collections import defaultdict
import sys
input = sys.stdin.readline
from heapq import heappop,heappush
def dijkstra(node):
    distance = [float('inf') for _ in range(V+1)]       # 최단 거리를 담을 리스트
    distance[node] = 0                                  # 시작점은 거리가 0
    hq = []                             # 합큐를 담을 리스트
    heappush(hq, (0, node))             # 힙큐에 (가중치, 도착점)을 넣어줌
    while hq:                           # 힙큐가 빌 때까지 반복
        nw, ne = heappop(hq)            # 현재 가중치, 현재 도착점

        for w, e in graph_dict[ne]:     # 현재 도착점의 간선과 가중치를 받아서
            w += nw                     # 더한 가중치가
            if w < distance[e]:         # 기존의 경로보다 짧으면
                distance[e] = w         # 갱신
                heappush(hq,(w,e))      # 힙큐에 넣기
    return distance
V = int(input())
E = int(input())

graph_dict = defaultdict(list)
for i in range(E):
    s, e, w = map(int, input().split())
    graph_dict[s].append((w, e))
A, B = map(int, input().split())
sol = dijkstra(A)
print(sol[B])

