# BOJ_2667_silver1-단지번호붙이기

n=int(input())
map1 = [list(map(int,input().strip())) for _ in range(n)]

visited = set()
stack = []
lst_sol = []
for r in range(n):                  # 아파트가 존재하는 모든 좌표를 visited에 답는다.
    for c in range(n):
        if map1[r][c] == 1:
            visited.add((r,c))
dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]
cnt = 0
while visited:                      # 모든 좌표가 다 소진될 때까지 반복
    size = len(visited)             # 단지 안의 아파트 개수를 파악하기 위해 현재 visited의 크기를 할당
    r,c = visited.pop()             # 좌표 r, c에 반환
    stack.append((r,c))             # 스택에 좌표 넣기
    while stack:
        tmp = []                    #
        # map1[r][c] = 0              # 맵 체크
        chk = 0
        for i in range(4):          # 델타탐색으로 인접 아파트의 개수를 세어 주고 tmp에 해당 좌표를 넣는다.
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<= nr < n and 0<= nc <n:
                if map1[nr][nc] == 1:
                    chk +=1
                    tmp.append((nr,nc))
        if chk > 1:                 # 아파트의 개수가 두 개 이상이면, r,c 좌표를 다시 스택에 넣는다.
            stack.append((r,c))
        if chk == 0:                # 스택에서 좌표를 하나 꺼낸다.
            r, c = stack.pop()
            continue
        else:                       # 아파트의 개수가 하나 이상이면, 좌표를 갱신하고
            nr, nc = tmp.pop()      # 해당 좌표를 visited에서 지워준다.
            visited.discard((nr, nc))
            r = nr
            c = nc
    lst_sol.append(size-len(visited))   # 단지를 한 바퀴 돌기 전, 사이즈와 현재 사이즈의 차이 = 단지 크기
print(len(lst_sol))         # 단지의 개수
lst_sol.sort()
for i in lst_sol:
    print(i)