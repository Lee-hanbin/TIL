# SWEA_14281_d3-최소신장트리
# kruskal 구현

from heapq import heapify, heappop, heappush
from collections import deque
import sys
sys.stdin = open('sample_input(2).txt')

# 상호배타집합과 key 초기화 시켜주는 함수
def make_set(x):
    parent[x] = x
    rank[x] = 0

# 현 상태의 root를 찾아서 저장해주는 함수
def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return parent[x]

# 두 트리를 연결시켜주는 함수
def union(x,y):
    link(find_set(x), find_set(y))

# 서로의 root를 비교해서 어떤 root를 최종 root로 해줄지 정하는 함수
def link(x,y):
    if rank[x] > rank[y]:       #rank를 최소로 하는 root를 골라줌
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1
def mst_kruskal():
    mst = []
    # 상호배타집합과 key 초기화
    for i in range(n+1):
        make_set(i)
    # print('rank= ' ,rank)
    # print('parent= ',parent)
    # 그래프를 가중치 기준으로 정렬
    graph = sorted(map1, key=lambda x:x[2])
    graph = deque(graph)
    # for i in graph:
    #     print(*i)

    # 각각의 트리들의 루트를 찾아 rank를 최소로 하도록 연결시켜줌
    while len(mst) < n and graph:
        s, e, w = graph.popleft()
        if find_set(s) != find_set(e):
            mst.append((w,s,e))
            union(s,e)
    # print(mst)
    return sum(map(lambda  x: x[0], mst))
def mst_kruskal2():
    mst = []
    for i in range(n+1):
        make_set(i)
    graph = [x[::-1] for x in map1]     # 가중치를 앞에 두기 위해 뒤집음
    heapify(graph)                      # 힙큐에 넣음
    while len(mst) < n and graph:
        w, e, s = heappop(graph)
        if find_set(s) != find_set(e):
            mst.append((w, s, e))
            union(s, e)
    # print(mst)
    return sum(map(lambda x: x[0], mst))
T = int(input())
for t in range(1,T+1):
    n, m = map(int, input().split())
    map1 = [list(map(int,input().split())) for _ in range(m)]
    # for i in map1:
    #     print(*i)

    rank = [-1]*(n+1)
    parent = [-1]*(n+1)
    # print(f'#{t} {mst_kruskal()}')
    print(f'#{t} {mst_kruskal2()}')
