# BOJ_1303_silver1_전쟁-전투

import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

def operation(lst):
    rst = 0
    for i in lst:
        rst += i**2
    return rst

def dfs(visited, color):
    stack = []
    dum = []
    while visited:
        size = len(visited)
        r, c = visited.pop()
        stack.append((r,c))
        while stack:
            tmp = []
            map1[r][c] = ' '
            cnt = 0
            for i in range(4):
                nr = dr[i] + r
                nc = dc[i] + c
                if 0 <= nr < m and 0 <= nc < n:
                    if map1[nr][nc] == color:
                        tmp.append((nr, nc))
                        cnt += 1
            if cnt > 1:
                stack.append((r,c))
            if cnt == 0:
                r, c = stack.pop()
                continue
            else:
                nr, nc = tmp.pop()
                visited.discard((nr, nc))
                r = nr
                c = nc
        dum.append(size-len(visited))
    return operation(dum)

n, m = map(int, input().split())

map1 = [list(input().strip()) for _ in range(m)]

set_W = set()
set_B = set()
sol = []

for i,e in enumerate(map1):
    for j, e2 in enumerate(e):
        if e2 == 'W':
            set_W.add((i,j))
        else:
            set_B.add((i,j))

for i in [(set_W,'W'), (set_B,'B')]:
    sol.append(dfs(i[0],i[1]))
print(*sol)