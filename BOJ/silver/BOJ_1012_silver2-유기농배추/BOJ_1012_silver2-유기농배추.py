# BOJ_1012_silver2-유기농배추

for i in range(int(input())):
    m, n, k = map(int, input().split())
    map1 = [[0]*m for _ in range(n)]
    visited = set()
    stack = []
    for i in range(k):
        c, r = map(int, input().split())
        map1[r][c] = 1                  # 모든 배추영역을 표시해주고
        visited.add((r,c))              # 셋에 모든 배추 인덱스를 담아준다.
    dr = [-1, 1, 0, 0]
    dc = [ 0, 0,-1, 1]
    cnt = 0
    while visited:                      # 배추 인덱스가 없을 때까지 반복복
        r,c = visited.pop()             # 배추 인덱스에서 좌표 값 받아서
        stack.apped((r,c))              # 스택에 쌓아주기
        while stack:
            tmp = []
            map1[r][c] = 0              # 배추 맵에 방문표시
            chk = 0                     # 스택에 쌓아주기
            for i in range(4):                  # 델타 탐색
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<= nr < n and 0<= nc <m:    # 네 방향 모두 체크해주기
                    if map1[nr][nc] == 1:       # 배추가 있으면 체크하고 임시 리스트에 담아주기
                        chk +=1
                        tmp.append((nr,nc))
            if chk > 1:                         # 경로가 여러 개면
                stack.append((r,c))             # 스택에 쌓아주기
            if chk == 0:                        # 길이 없으면
                r, c = stack.pop()              # 스택에서 pop
                continue
            else:                               # 경로가 한개 이상이면
                nr, nc = tmp.pop()              # 임시 리스트를 pop하고
                visited.discard((nr, nc))       # 배추 인덱스를 빼주기
                r = nr                          # 다음 경로로 이동
                c = nc
        cnt += 1
    print(cnt)