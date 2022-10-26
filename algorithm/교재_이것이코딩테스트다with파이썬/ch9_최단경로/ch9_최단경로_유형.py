#ch9_최단경로

'''
@ 최단 경로 (길 찾기)
 - 다익스트라 최단 경로 (그리디)
 - 플로이드 워셜 (DP)
 - 벨만 포드 알고리즘

@ 다익스트라 최단 경로 알고리즘
 - 여러 개의 노드가 있을 때, 특정한 노드에서 풀발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
 - '음의 간선`이 없는 경우, 올바르게 작동
 - 실제 GPS 소프트웨에의 기본 알고리즘으로 채택

@ 다익스트라 과정
1. 출발 노드 선택
2. 최단 거리  테이블을 초기화
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신

@ 다익스트라 특징
 - 최단 거리 정보를 항상 1차원 리스트에 저장하며 리스트를 계속 갱신
 - 매번 현재 처리하고 있는 노드를 기준으로 주변 간선을 확인
 - 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾을 수 있음

@ 다익스트라 구현 방법
방법1. 구현하기 쉽지만 느리게 동작하는 코드
시간 복잡도 : O(v^2) (V = 노드의 개수)
############################################################
INF = float('inf')

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_V = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_V and not visited[i]:
            miv_V = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
#############################################################

방법2. 구현하기에 조금 더 까다롭지만 빠르게 동작하는 코드
시간 복잡도 : O(ElogV) (V = 노드의 개수, E = 간선의 개수)

#############################################################
import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

n, m = map(int, input().split())    # 노드 개수, 간선 개수
start = int(input())    # 시작 노드 번호 입력받기
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 다익스트라 알고리즘 수행
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])

#############################################################


2. 플로이드 워셜 알고리즘
'''
