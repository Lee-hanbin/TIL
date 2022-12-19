# SWEA_14279_d3-연산_

from collections import deque

def bfs(n, m):
    que = deque()
    que.append([n,0])
    visited = set()
    visited.add(n)
    while que:
        v, cnt = que.popleft()
        cnt += 1
        for i in [v+1, v-1, v*2, v-10]:
            if i not in visited and 0<= v+1 <= 1000000:
                if i == m:
                    return cnt
                que.append([i,cnt])
                visited.add(i)
        # if v + 1 not in visited and 0<= v+1 <= m:
        #     que.append([v+1, cnt])
        #     visited.add(v+1)
        # if v - 1 not in visited and v - 1 >= 0:
        #     que.append([v -1 , cnt])
        #     visited.add(v-1)
        # if v*2 not in visited and 0 <= v + 1 <= 1000000:
        #     que.append([v*2, cnt])
        #     visited.add(v*2)
        # if v - 10 not in visited and v - 10 >= 0:
        #     que.append([v - 10, cnt])
        #     visited.add(v-10)

T= int(input())
for t in range(1,T+1):
    n, m = map(int, input().split())

    cnt = bfs(n, m)
    print(f'#{t} {cnt}')