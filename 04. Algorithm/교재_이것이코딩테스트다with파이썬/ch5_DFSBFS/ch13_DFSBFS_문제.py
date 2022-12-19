#ch13 DFS BFS 문제

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
'''

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

'''
@ 19) 연산자 끼워 넣기 (BOJ 14888)

#문제
1. N개의 수로 이루어진 수열 A1,A2,...,AN
2. 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어짐
3. 연산자는 +,-,*,//
4. 주어진 수의 순서는 그대로 유지
5. 연산자 우선순위의 법칙은 무시하고 앞에부터 연산
6. 나눗셈은 정수 나눗셈 몫만 취한다.
7. 음수를 양수로 나눌 때는 C++14의 기준을 따름
    - 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꿈
8. 이때, 연산자의 경우에 따른 식의 최대값과 최소값을 구하여라

#입력조건
첫째 줄: 수열의 크기
둘째 줄: 수열의 값
셋째 줄: 연산자 ( 덧셈, 뺄셀, 곱하기, 나눗셈 ) 각각의 개수

#출력조건
첫째 줄: 최대값
둘째 줄: 최솟값

'''

# # 순열 풀이
# import sys
# input = sys.stdin.readline
#
# # 연산 함수
# def operator(s, num1, num2):
#     if 'a' in s:
#         return num1 + num2
#     elif 's' in s:
#         return num1 - num2
#     elif 'm' in s:
#         return num1 * num2
#     elif 'd' in s:
#         if num1 <0 and num2 >0:
#             num1 = -num1
#             return -(num1//num2)
#         return num1 // num2
#
# # 순열 함수
# def pmt(lst_operator, result):
#     if len(result) == len(lst_operator):
#         lst_operator_pmt.append(result[:])  # 위와 같으나 shallow copy 고려해서 deep copy로 해줘야함.
#         return
#     for i in lst_operator:
#         if i not in result:
#             result.append(i)
#             pmt(lst_operator, result)
#             result.pop()
#
# N = int(input())
# lst = list(map(int,input().split()))
# a, s, m, d = map(int, input().split())
# M = a + s + m + d
# lst_operator = []
# lst_operator_pmt = []
# lst_sol = []
# # 중복순열 대신 각 부호에 번호를 매겨서 순열로 활용
# for i in range(a):
#     lst_operator.append('a'+str(i))
# for i in range(s):
#     lst_operator.append('s'+str(i))
# for i in range(m):
#     lst_operator.append('m'+str(i))
# for i in range(d):
#     lst_operator.append('d'+str(i))
#
# # 순열 리스트 생성
# pmt(lst_operator, [])
#
# # 연산 반복문
# for i in lst_operator_pmt:
#     cnt = 0
#     tmp = lst[0]                            # 첫 값 넣어주고
#     for j in i:                             # 경우의 수 중에 하나인 연산자 리스트 i
#         tmp = operator(j, tmp, lst[cnt+1])  # tmp는 순서대로 연산
#         cnt +=1                             # 다음 숫자
#     lst_sol.append(tmp)                     # 결과를 리스트에 담기
#
# print(max(lst_sol))     # 최대값
# print(min(lst_sol))     # 최소값

# #dfs 풀이
#
# N = int(input())
# lst = list(map(int,input().split()))
# a, s, m, d = map(int, input().split())
#
# max_value = -1e9
# min_value = 1e9
#
# def dfs(i, now):
#     global min_value, max_value, a, s, m, d
#     if i == N:
#         min_value = min(min_value, now)
#         max_value = max(max_value, now)
#     else:
#         if a > 0:
#             a -= 1
#             dfs(i+1, now+lst[i])
#             a += 1
#         if s > 0:
#             s -= 1
#             dfs(i+1, now-lst[i])
#             s += 1
#         if m > 0:
#             m -= 1
#             dfs(i+1, now*lst[i])
#             m += 1
#         if d > 0:
#             d -= 1
#             dfs(i+1, int(now/lst[i]))
#             d += 1
#
# dfs(1, lst[0])
#
# print(max_value)
# print(min_value)

'''
#리뷰
처음 생각난 풀이는 순열이었고... dfs로 어떻게 풀어야 할지 감도 잡히지 않았다.
순열도 중복순열을 생각하였으나, 구현할 자신이 없어서 연산자에 숫자를 붙여서 순열로 풀었다.
분명 dfs, bfs 파트인데 제대로 사용해서 풀지를 못하니.. 연습이 많이 필요할 것 같다.
'''


'''
@ 21) 인구 이동

#문제
1. 땅의 크기 : N * N 
2. 각각의 땅에는 나라가 하나씩 존재하며, A[r][c]명이 살고 있음
3. 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하이면, 두 나라가 공유하는 국경선을 하루 연다.
4. 국경선이 열리면 인구 이동 시작
5. 연합을 이루고 있는 각 칸의 인구수는 int((연합의 인구수) / (연합을 이루고 있는 칸의 개수))
6. 연합으 해체하고, 모든 국경선을 닫는다.
7. 각 나라의 인구수가 주어졌으 때, 인구 이동이 며칠 동안 발생하는지 구하여라

#입력조건 
첫째 줄: N, L, R 주어짐 (1 <= N <= 50, 1 <= L <= R <= 100)
둘째 줄 ~ : 각 나라의 인구수가 주어짐
'''

