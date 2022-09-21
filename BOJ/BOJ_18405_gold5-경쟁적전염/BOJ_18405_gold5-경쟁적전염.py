#BOJ_18405_gold5-경쟁적전염


'''
@ 17) 경쟁적 전염 (BOJ 18405)

#문제
N * N 크기의 시험관 존재
특정한 위치에 바이러스 존재 가능
모든 바이러스는 1초마다 상, 하, 좌, 우 방향으로 증식
매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식
특정한 칸에 이미 어떠한 바이러스가 존재하면, 그 곳에는 다른 바이러스가 들어갈 수 없음
시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성

#입력 조건
첫째 줄: N(1~200), K(1~1000)
둘째 줄 ~ : 시험관 상태
N+2번째 줄 : S(시간), X, Y  (0<=S<=10,000 1 <= X,Y <= N)
#출력 조건
S초 뒤에 (X,Y)에 존재하는 바이러스의 종류를 출력
S초 뒤에 (X,Y)에 바이러스가 존재하지 않으면 0을 출력

#input
3 3
1 0 2
0 0 0
3 0 0
2 3 2
#output
3
'''
# # 그리디 방법..?
# from collections import defaultdict
#
# N, K = map(int, input().split())
# map1 = [list(map(int,input().split())) for _ in range(N)]
# S, X, Y = map(int,input().split())
# #     상 하 좌 우
# dr = [-1, 1, 0, 0]
# dc = [ 0, 0,-1, 1]
# idx = defaultdict(list)
#
# # 처음 감염위치를 dictionary에 담기
# for i in range(N):
#     for j in range(N):
#         if map1[i][j] != 0:
#             idx[map1[i][j]].append((i,j))
# # 딕셔너리의 key를 정렬하기
# idx_list = sorted(idx)
# # S초만큼 반목
# for _ in range(S):
#     idx_next = defaultdict(list)            # 한 바퀴 돌면 끝 값들을 담을 딕셔너리
#     for e in idx_list:                      # 1부터 순서대로 감염
#         for v in idx[e]:                    # 해당 감염이 시작될 좌표마다 0이 있으면 감염시킨다.
#             r, c = v
#             for i in range(4):              # 델타 탐색
#                 nr = r + dr[i]
#                 nc = c + dc[i]
#                 if nr < 0 or nc < 0 or nr >= N or nc >= N:      # 범위를 벗어나면 pass
#                     continue
#                 if map1[nr][nc] == 0:                       # 감염되어 있지 않은 지역을 감염시킴
#                     map1[nr][nc] = e
#                     idx_next[map1[nr][nc]].append((nr, nc))     # 해당 좌표를 idx에 넣음
#     idx = idx_next                          # 다음에 칠할 좌표가 담긴 딕셔너리를 갱신
# print(map1[X-1][Y-1])


# # bfs..?
# from collections import deque
#
# N, K = map(int, input().split())
#
# map1 = []
# idx = []
#
# for i in range(N):
#     map1.append(list(map(int,input().split())))
#     for j in range(N):
#         if map1[i][j] != 0:
#             idx.append((map1[i][j],0,i,j))
#
# idx.sort()
# que = deque(idx)
#
# S, X, Y = map(int,input().split())
#
# #     상 하 좌 우
# dr = [-1, 1, 0, 0]
# dc = [ 0, 0,-1, 1]
#
# # bfs
# while que:
#     virus, s, r, c = que.popleft()
#     if s == S:
#         break
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if nr < 0 or nc < 0 or nr >= N or nc >= N:  # 범위를 벗어나면 pass
#             continue
#         if map1[nr][nc] == 0:
#             map1[nr][nc] = virus
#             que.append((virus, s+1, nr, nc))
#
# print(map1[X-1][Y-1])

'''
#리뷰
책의 풀이와 본인의 풀이의 논리 자체는 크게 차이나지 않다.
하지만, 책은 튜플의 변수를 4개를 줘서 한번에 처리했기에 for문이 2개나 적었다.
본인은 튜플에 변수를 2개를 주고 나머지 2개의 변수를 각각 처리해줬기에 반복문이 2개 늘어서 비효율적인 코드가 되었다.
책   : 32440KB, 196ms
본인 : 32936KB, 2352ms
=> 메모리 차이가 나지 않았던 이유는 dictionary를 사용해서...
'''