# BOJ_18352_silver2-특정거리의도시찾기

'''
@ 15 특정 거리의 도시 찾기(BOJ 18352)

#문제
어떠 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재
모든 도로의 거리는 1
특정한 도시 X에서 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력 하는 프로그램을 작성

#입력조건
첫째 줄: N: 도시의 개수, M: 도로의 개수, K: 거리 정보, X: 출발 도시의 번호
        (2 ~300,000)   (1~ 1,000,000) (1~ 300,000)
둘째 줄: M개의 줄에 걸쳐서 두 개의 자연수 A, B가 주어짐 ( 1~N)

#input1
4 4 2 1
1 2
1 3
2 3
2 4
#output2
4
#input1
4 3 2 1
1 2
1 3
1 4
#output2
-1
#input1
4 4 1 1
1 2
1 3
2 3
2 4
#output2
2
3
'''

# import sys
# input = sys.stdin.readline
#
# from collections import defaultdict , deque
#
#
# def bfs(graph, start, distance):
#     queue = deque([start])
#     while queue:
#         v = queue.popleft()
#         for i in graph[v]:
#             print(distance)
#             if distance[i] == -1:
#                 distance[i] = distance[v] + 1
#                 queue.append(i)
# N, M, K, X = map(int, input().split())
#
# dict1 = defaultdict(list)
#
# for i in range(M):
#     start, end = map(int, input().split())
#     dict1[start].append(end)
#
# distance = [-1] * (N+1)
# distance[X] = 0
#
# bfs(dict1, X, distance)
#
# chk = False
# for i in range(1, N+1):
#     if distance[i] == K:
#         print(i)
#         chk = True
# if chk == False:
#     print(-1)

'''
#리뷰
문제를 보자마자 bfs로 풀어야 겠다고 생각했으나... 구현이 안됐다.
아직 경험치가 부족한 것 같아요 ㅜㅡ