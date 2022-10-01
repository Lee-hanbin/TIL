# BOJ_1753_gold4-최단경로

import sys
input = sys.stdin.readline
from collections import defaultdict
from heapq import heappop,heappush,heapify

def dijkstra(node):
    # U = {node}
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
    # for w ,e in graph_dict[node]:
    #     distance[e] = w
    #
    # for _ in range(V+1):
    #     min_v = float('inf')
    #     for i in range(V+1):
    #         if i not in U and min_v > distance[i]:
    #             min_v = distance[i]
    #             idx = i
    #     U.add(idx)
    #     for w, e in graph_dict[idx]:
    #         distance[e] = min(distance[e], distance[idx] + w)
    # return distance

V, E = map(int,input().split())
node = int(input())
graph_dict = defaultdict(list)          # 그래프 생성
for _ in range(E):                      # 그래프 연결
    s, e, w = map(int,input().split())
    graph_dict[s].append((w,e))
if V == 1:                              # V = 1은 특수한 경우
    print(0)
else:
    sol = dijkstra(node)                # dijkstra를 통해 각 정점까지의 최단거리 구하기
    for i in range(1,V+1):              # 정점을 들리지 않았다면 INF 출력
        if sol[i] == float('inf'):
            print('INF')
        else:
            print(sol[i])