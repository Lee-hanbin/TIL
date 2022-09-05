# BOJ_18258_silver4-큐2

import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline


def create_que():
    global front, rear
    que = [0] * 2000000         # 최대 2000000개 들어오기 때문에
    front, rear = -1, -1        # 초기화
    return que

def enQueue(que, x):
    global front, rear
    if isFull(que):             # 가득차면 -1 반환
        return -1
    else:                       # 아니면 큐에 넣고 rear를 1올림
        rear += 1
        que[rear] = x

def deQueue(que):
    global front, rear
    if isempty():               # 비어있으면 -1 반환
        return -1
    else:                       # 아니면 큐에서 빼고 front 1 올림
        front += 1
        return que[front]

def countQueue():               # 큐 안의 개수를 출력
    global front, rear          # rear - front
    return rear - front

def isempty():
    global front, rear
    if front == rear:           # 비어있으면 1
        return 1
    else:                       # 아니면 0
        return 0

def isFull(que):
    global front, rear
    if rear == len(que) - 1:    # 전체 큐의 길이와 rear이 같으면 1
        return 1
    else:                       # 아니면 0
        return 0

def Qpeek(que):
    global front
    if isempty():               # 비어있으면 -1
        return -1
    else:                       # 아니면 가장 앞에 있는 큐 요소 반환
        return que[front+1]

def Qtail(que):
    global rear
    if isempty():               # 비어있으면 -1
        return -1
    else:                       # 아니면 가장 뒤에 있는 큐 요소 반환
        return que[rear]


N = int(input())
que = create_que()
chk = []
for i in range(N):
    chk = input().split()
    cnd = chk[0]
    if len(chk) == 2:           # 입력된 숫자가 하나 더 있으면 푸쉬
        enQueue(que, chk[1])
    elif cnd == 'pop':
        print(deQueue(que))
    elif cnd == 'size':
        print(countQueue())
    elif cnd == 'empty':
        print(isempty())
    elif cnd == 'front':
        print(Qpeek(que))
    else:
        print(Qtail(que))
