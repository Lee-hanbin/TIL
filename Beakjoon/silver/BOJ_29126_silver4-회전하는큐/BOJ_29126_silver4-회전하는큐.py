import sys
input = sys.stdin.readline

# 좌측이동 함수
def r2(sol):
    global cnt, cf
    if que[cf] == sol:          # 같으면 그만
        return
    else:
        cnt += 1                # 카운트
        if cf == 0:             # 비교하는 값이 0이면 cf 끝으로
            cf = len(que)-1
        else:                   # 아니면 왼쪽으로 이동
            cf -= 1
        r2(sol)                 # 반복

# 우측이동 함수
def r3(sol):
    global cnt, cf
    if que[cf] == sol:          # 같으면 그만
        return
    else:
        cnt += 1                    # 카운트
        cf = (cf + 1) % len(que)    # 계속 우측이동
        r3(sol)                     # 반복

N, M = map(int, input().split())

lst = list(map(int, input().split()))

que = list(range(N))
for i, e in enumerate(lst):
    lst[i] -= 1

cnt, cf = 0, 0
for sol in lst:
    while 1:
        if len(que) == 1:               # 큐가 하나 남으면 break
            break
        if que[cf] == sol:              # 현재 위치와 원하는 값의 위치가 같으면
            if que[cf] == que[-1]:      # 만약 마지막 값이 빠졌을 경우, cf = 0으로 셋팅
                cf = 0
            que.remove(sol)             # 해당 값을 remove하고
            N -= 1                      # 리스트의 요소가 하나 줄었음
            break
        elif que[cf] < sol:             # 찾는 값이 비교 값보다 클 때
            if que.index(sol) - cf <= N//2: # 갱신 없이 길이가 절반보다 작거나 같으면
                r3(sol)                     # 우측이동
            else:
                r2(sol)
        else:                               # 찾는 값이 비교 값보다 작을 때
            if cf - que.index(sol) <= N//2: # 갱신 없이 길이가 절반보다 작거나 같으면
                r2(sol)                     # 좌측이동
            else:
                r3(sol)
print(cnt)

# 0 1 2
#