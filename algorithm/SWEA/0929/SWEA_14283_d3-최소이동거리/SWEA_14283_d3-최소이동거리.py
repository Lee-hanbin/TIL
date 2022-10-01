# SWEA_14283_d3-최소이동거리

import sys
sys.stdin = open('sample_input(4).txt')
from collections import defaultdict
from pprint import pprint

def dijkstra():
    U = {0}
    distance = [float('inf') for _ in range(n+1)]
    distance[0] = 0

    for w, e in graph_dict[0]:
        distance[e] = w

    for _ in range(n+1):
        min_v = float('inf')
        for i in range(n+1):
            if i not in U and min_v > distance[i]:
                min_v = distance[i]
                idx = i
        U.add(idx)
        for w, e in graph_dict[idx]:
            distance[e] = min(distance[e], distance[idx] + w)
    return distance

T = int(input())
for t in range(1,T+1):
    n, m = map(int, input().split())
    graph_dict = defaultdict(list)
    for i in range(m):
        s, e, w = map(int, input().split())
        graph_dict[s].append((w,e))
    # pprint(graph_dict)
    sol = dijkstra()[-1]
    print(f'#{t} {sol}')