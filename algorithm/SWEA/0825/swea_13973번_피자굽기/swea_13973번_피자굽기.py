# swea 13973 피자굽기
import sys
sys.stdin = open('sample_input(2).txt')

# 원형 큐 생성
def createQueue(M):
    global front, rear
    que = [-1]* (M+1)
    front, rear = 0, 0
    return que

# enQueue함수
def enQueue(item):
    global front, rear
    rear = rear % M + 1
    que[rear] = item

# 응용 deQueue함수
def deQueue(i):
    global front, rear, idx_cnt
    if len(lst) != 0:
        que[i] = [idx_cnt, lst.pop()]      # 피자를 빼고 그 자리에 피자 넣기
        idx_cnt += 1
        return 0
    else:
        return 1

for t in range(int(input())):
    M, N = list(map(int, input().split()))
    lst = list(map(int, input().split()))[::-1]
    sol = 0
    idx_cnt = 1
    print(lst[::-1])
    que = createQueue(M)                                # 원형 큐를 생성해
    print(lst)
    for i in range(M):
        enQueue([idx_cnt, lst.pop()])                  # 원형 큐에 값을 피자를 넣어
        idx_cnt += 1
    print(que)
    switch = 0
    while switch != 2:                                  # sol에 값이 들어올 때까지 계속 돌려라
        temp = 0
        i = 0
        while i < len(que):
            e = que[i]
            if e == - 1:                               # 큐의 공백이면 다음으로 넘기고
                i += 1
                continue
            temp = e[1] // 2                           # temp = 치즈양 // 2
            if temp == 0:                              # 피자가 다 구워지면
                switch = deQueue(i)                    # 응용 deQueue
                if switch == 1:                        # 남은 피자가가 없는 경우
                    if len(que) == 2:                  # 화덕에 피자가 하나 남은 경우
                        switch = 2
                        sol = e[0]                     # index값을 대입
                        break
                    else:                              # 화덕에 피자가 남은 경우
                        que.pop(i)
                        i -= 1
            else:                                      # 피자가 다 안 구워지는 경우
                que[i][1] = temp
            i += 1
    print(f'#{t+1} {sol}')
