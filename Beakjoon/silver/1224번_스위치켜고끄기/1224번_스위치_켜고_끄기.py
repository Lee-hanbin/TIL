#1224번_스위치_켜고_끄지

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def change(element):
    if element == 0:
        return 1
    else:
        return 0
def man(n):
    for i in range(n-1, N, n):          # n == 1 이면
        switch[i] = change(switch[i])
    return
def woman(n):
    d, cnt = 1, 0
    switch[n-1] = change(switch[n-1])                   #무조건 n번째는 바꿔
    if n - 1 == 0 or n - 1 == N - 1:
        pass
    elif switch[n-1 - d] == switch[n-1 + d]:    #팰린드롬이면
        cnt += 1
        while 1:
            cnt += 1
            d += 1
            if n-1 - d < 0 or n-1 + d > N - 1:
                cnt -= 1
                break
            if switch[n-1 - d] != switch[n-1 + d]:
                cnt -= 1
                break
        for i in range(1, cnt+1):
            switch[n-1 -i] = change(switch[n-1 -i])
            switch[n-1 +i] = change(switch[n-1 +i])
        return switch
    return switch

N = int(input())
switch = list(map(int, input().split()))
M = int(input())
si = [list(map(int, input().split())) for _ in range(M)]
for i in si:
    if i[0] == 1:           # 남학생인 경우
        man(i[1])
    else:                   # 여학생인 경우
        woman(i[1])

for i, e in enumerate(switch):
    print(e ,end=' ')
    if i % 20 == 19:
        print()
