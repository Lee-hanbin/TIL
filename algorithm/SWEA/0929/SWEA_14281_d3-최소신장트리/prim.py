# SWEA_14281_d3-최소신장트리
# prim 구현
from pprint import pprint
from collections import defaultdict
from heapq import heapify, heappop, heappush
import sys
sys.stdin = open('sample_input(2).txt')

def prim(node):
    visited = [0]*(V+1)             # 방문을 표시할 리스트
    key = [float('inf')]*(V+1)      # key 값에 큰 값 넣기
    key[node] = 0                   # 자기 자신은 0
    for _ in range(V+1):            # 전체 노드 순회
        min_v = float('inf')        # 최소값 초기화
        for i in range(V+1):                            # 노드 전체 순회
            if visited[i] == 0 and key[i] < min_v:      # 방문하지 않았고 가중치가 작으면
                s = i                                   # 다음 경로를 갱신
                min_v = key[i]                          # 그 값을 최소 경로로 잡아주기
        visited[s] = 1                                  # 최소 가중치에 해당하는 노드를 방문표시
        #인접리스트
        # for e in range(V+1):                            # 열결된 노드 모두 확인
        #     if visited[e] == 0 and map_lst[s][e] > 0:   # 방문하지 않았고 경로가 연결되어 있으면
        #         if key[e] > map_lst[s][e]:              # 최소값을 찾아서 갱신
        #             key[e] = map_lst[s][e]
        #딕셔너리
        for node in map_dict[s]:                            # 열결된 노드 모두 확인
            w, e = node
            if visited[e] == 0 and w > 0:   # 방문하지 않았고 경로가 연결되어 있으면
                if key[e] > w:              # 최소값을 찾아서 갱신
                    key[e] = w

    return sum(key)

#힙큐 구현
def prim2(node):
    mst = []
    visited = {node}
    candidate = map_dict[node]
    heapify(candidate)
    s = node
    while len(visited) < V+1 and candidate:
        w, e = heappop(candidate)

        if e not in visited:
            visited.add(e)
            mst.append((w, s, e))
            for route in map_dict[e]:
                if route not in visited:
                    heappush(candidate, route)
                    s = e
    # print(mst)
    return sum(map(lambda x: x[0], mst))

T = int(input())
for t in range(1,T+1):
    V, E = map(int, input().split())
    map_lst = [[0]*(V+1) for _ in range(V+1)]
    map_dict = defaultdict(list)
    for _ in range(E):
        s, e, w = map(int, input().split())
        map_lst[s][e] = w
        map_lst[e][s] = w

        map_dict[s].append((w, e))
        map_dict[e].append((w, s))
    # pprint(map_dict)
    # print(f'#{t} {mst_kruskal()}')
    print(f'#{t} {prim2(0)}')