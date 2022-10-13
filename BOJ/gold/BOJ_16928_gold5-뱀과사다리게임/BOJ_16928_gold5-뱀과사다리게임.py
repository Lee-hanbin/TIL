# BOJ_16928_gold5-뱀과사다리게임

from collections import deque, defaultdict
import sys
input = sys.stdin.readline
def bfs(start):
    que = deque()
    que.append((start,0))                           # (위치, 주사위 굴린 횟수)
    visited = [0 for _ in range(101)]               # 1~100 까지 방문 표시
    visited[start] = 1                              # 시작지점 방문 표시
    while que:
        v, cnt = que.popleft()
        if v in trigger.keys():                     # 해당 위치에 사다리 or 뱀이 있는 경우
            v = trigger[v][0]                       # 위치 옮기기
        for i in [1, 2, 3, 4, 5, 6]:                # 주사위 굴리기
            if i+v < 101 and not visited[i+v]:      # 해당 위치가 100보다 크지 않고 방문한 이력이 없으면
                if v+i == 100:                      # 100 이면 counting 해주고 반환
                    return cnt +1
                visited[i+v] = 1                    # 아니면 방문 표시
                que.append((i+v, cnt+1))            # 해당 위치를 queue에 넣어줌

n, m = map(int, input().split())            # n : 뱀수, m : 사다리수
k = n + m                                   # k : 트리거 개수
trigger =defaultdict(list)
for i in range(k):
    s, e = map(int, input().split())
    trigger[s].append(e)                    # key : 뱀과 사다리의 위치 value : 이동지점
print(bfs(1))
