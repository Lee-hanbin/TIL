# ch 5 DFS/BFS

'''
@ 탐색
 - 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
 - DFS와 BFS를 활용
 - DFS : 스택이용
   BFS :   큐이용

@ 자료구조
 - 데이터를 표현하고 관리하고 처리하기 위한 구조

@ 스택
 - 박스 쌓기
 - 선입후출 or 후입선출

@ 큐
 - 놀이공원의 줄
 - 선입선출
 - from collections import deque 활용
 - 코딩테스트에서 허용되니까 마음껏 사용해도 된다.

@ 재귀 함수
 - DFS와 BFS를 구현하는데 필수적인 이론
 - 자기 자신을 다시 호출하는 함수
 - RecursionError: maximum recursion depth exceeded while pickling an object
   => 재귀의 최대 깊이를 초과

@ 재귀 함수 종료 조건
 - 재귀 함수 문제 풀이에서는 재귀 함수가 언제 끝날지 종료 조건을 꼭 명시!
 - 보통 재귀 함수 초반에 나오는 if문이 종료 조건이다.

@ DFS
 - 깊이 우선 탐색
 - 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
1. 인접 행렬 방식
 - 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식.
2. 인접 리스트 방식
 - 특정한 노드와 연결된 모든 인접 노드를 순회해야 하는 경우, 인접 행렬 방식에 비해
  메모리 공간의 낭비가 크다.
3. 방법
 - 탐색 시작 노드를 스택에 삽입하고 방문 처리
 - 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고
  방문 처리, 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드 꺼내기
 - 위의 과정을 반복
Tip
 - 코딩 테스트에서는 번호가 낮은 순서부터 처리하도록 명시하는 경우가 종종 있음.
  따라서 번호가 낮은 순서부터 구현하도록 연습하자.

ex)
    def dfs(graph, v, vsited):
        # 현재 노드를 방문 처리
        visited[v] = True
        print(v, end=' ')
        # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for i in graph[v]:
            if not visited[i]:
                dfs(graph, i, visited)

    # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
    graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7],
    ]

    # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
    visited = [False] * 9

    # 정의된 DFS 함수 호출
    dfs(graph, 1, visited)


@ BFS
 - 너비 우선 탐색
 - 가까운 노드부터 탐색하는 알고리즘
1. 방법
 - 탐색 시작 노드를 큐에 삽입하고 방문 처리
 - 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
 - 위의 과정을 반복

Tip
- 재귀 함수로 DFS를 구현하면서 컴퓨터 시스템의 동작 특성상 실제 프로그램의 수행 시간은 느려질 수 있다.
 따라서 스택 라이브러리를 이용해 시간 복잡도를 완화하는 테크닉이 필요할 때도 있다. 다만, 이 부분은 교재의 범위를 넘어감
 => DFS보다는 BFS 구현이 조금 더 빠르게 동작한다는 정도로 기억!

ex)
    from collections import deque

    #BFS 메서드 정의
    def bfs(graph, start, visited):
        #큐(Queue) 구현을 위해 deque 라이브러리 사용
        queue = deque([start])
        #현재 노드를 방문 처리
        visited[start] = True
        #큐가 빌 때까지 반복
        while queue:
            #큐에서 하나의 원소를 뽑아 출력
            v = queue.popleft()
            print(v, end=' ')
            #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
    graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7],
    ]
    # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
    visited = [False] * 9

    # 정의된 DFS 함수 호출
    bfs(graph, 1, visited)
'''


'''
@ 실전 1) 음료수 얼려 먹기

# 문제
N * M 크기의 얼음 틀 존재
구멍이 뚤려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결된 것으로 간주
얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하여라.

# 입력조건
첫째 줄: 얼음 틀의 세로 길이 N, 가로 길이 M이 주어짐 ( 1 ~ 1000)
둘째 줄~ : 얼음 틀의 현태가 주어짐

#input
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

#output
8
'''

# n, m = map(int, input().split())
#
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# def dfs(x,y):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
#     return False
#
# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             result += 1
#
# print(result)
#

'''
#리뷰
아직 미로 문제를 제외한 dfs, bfs문제의 응용력이 약해서 바로 풀이를 참고했다.
아무래도 재귀부분이 약하다 보니, 실제적으로 구현할 수 있을지에 대한 의문이 든다.
그래도 계속 공부해서 익숙해져야 겠다.
'''

'''
@ 실전 2) 미로 탈출

#문제
N * M 직사각형 형태의 미로
동빈이의 위치는 (1,1) 미로의 출구는 (N,M)
괴물이 있으면 0 괴물이 없으면 1

#입력 조건
첫째 줄: N, M (4 ~200) 

#출력 조건
최소 이동 칸의 개수

#input
5 6
101010
111111
000001
111111
111111
#output
10
'''

from collections import deque

n, m = map(int, input().split())
lst = []
lst = [list(map(int,input())) for _ in range(n)]

#     상  하  좌  우
dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

def bfs(r, c):
    que = deque()
    que.append((r, c))
    while que:
        r, c = que.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nc < 0 or nr >= n or nc >= m:
                continue
            if lst[nr][nc] == 0:
                continue
            if lst[nr][nc] == 1:
                lst[nr][nc] = lst[r][c] + 1
                que.append((nr, nc))
    return lst[n-1][m-1]

print(bfs(0,0))
'''
#리뷰
이 문제도 읽자마자 bfs로 풀어야 함을 인지했지만, 구현이 쉽지 않았다.
뒤에 문제 풀면서 친해져 보자!
'''













