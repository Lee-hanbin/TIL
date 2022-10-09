# BOJ_16166_silver2-서울의지하철
'''
55%에서 통과 못한 풀이..
아마 인풋을 받을 때, 모든 역에 대한 정보가 제대로 안 들어와서 그런 것 같다..
하지만, 해결 방법을 찾지 못했다.
'''

from collections import defaultdict, deque

def bfs(root):
    que = deque()
    if root == final:
        return 0

    for i in dict1[root]:
        que.append((i, 0))

    visited = set()
    # visited.add(root)
    while que:
        v, cnt = que.popleft()
        if v[0] == final:
            return cnt
        for i in dict1[v[0]]:
            if i not in visited:
                visited.add(i)           #역 방문표시
                if v[1] != i[1]:            #호선이 달라지면 카운팅
                    que.append((i,cnt+1))
                else:                       #호선이 같으면 카운팅 안함
                    que.append((i,cnt))
    return -1

dict1 = defaultdict(list)
n = int(input())
for i in range(1,n+1):
    size, *station = map(int, input().split())
    for j in range(size-1):
        dict1[station[j]].append((station[j+1],i))
    if size > 1 and station[0] != station[-1]:
        dict1[station[-1]] = []
final = int(input())
print(bfs(0))
