# swea 14074 d2 이진힙


for t in range(int(input())):
    E = int(input())
    # arr = [0] + list(map(int, input().split()))

    ch1 = [0] * (E+1)
    ch2 = [0] * (E+1)
    value = [0] * (E+1)
    par = [0] * (E+1)

    k = 0
    point = 1

    for i, e in enumerate(list(map(int,input().split()))):
        # 노드를 생성해서 값을 넣어주고 연결하는 조건문
        if i == 0:
            value[1] = e
            continue
        if value[point*2] == 0:        # 현재 노드의 왼쪽 자식이 없으면
            value[point*2] = e           # 노드를 추가해서 값을 넣어줘라
            ch1[point] = point*2        # 현재 노드에 자식 노드를 연결
            par[point*2] = point          # 자식 노드에 부모 노드를 연결
            p = point
            while p > 0:
                if e < value[par[p*2]]:  # 넣은 값이 부모 노드의 값보다 작으면
                    tmp = value[p]       # 부모 노드의 값을 저장해두고
                    value[p] = e         # 부모 노드에 새로 넣은 값을 넣고
                    value[p*2] = tmp     # 부모 노드의 값은 새로 생성된 노드에 넣는다.
                    p = p//2           # 그 위의 부모를 호출한다.
                else:                      # 넣은 값이 부모 노드의 값보다 크면 납둬라
                    break
        elif ch2[point*2+1] == 0:            # 현재 노드의 오른쪽 자식이 없으면
            value[point*2+1] = e         # 노드를 추가해서 값을 넣어줘라
            ch2[point] = point*2+1    # 현재 노드에 자식 노드를 연결
            par[point*2+1] = point        # 자식 노드에 부모 노드를 연결
            p = point
            while p > 0:
                if e < value[par[p*2+1]]:  # 넣은 값이 부모 노드의 값보다 작으면
                    tmp = value[p]         # 부모 노드의 값을 저장해두고
                    value[p] = e           # 부모 노드에 새로 넣은 값을 넣고
                    value[p*2+1] = tmp     # 부모 노드의 값은 새로 생성된 노드에 넣는다.
                    p = p//2             # 그 위의 부모를 호출한다.
                else:                        # 넣은 값이 부모 노드의 값보다 크면 납둬라
                    break
            point += 1                   # 오른쪽 노드에 자식이 생기면 다음 노드로 넘어가
    print(value)
    sol = 0
    while E > 0:
        E = E//2
        sol += value[E]
    print(f'#{t+1} {sol}')

# for i in range(1, E+1):
#     if i * 2 <= E:
#         ch1[i] = 2 * i
#         par[2*i] = i
#     if 2 * i + 1 <= E:
#         ch2[i] = 2*i+1
#         par[2*i+1] = i
#
# print(ch1)
# print(ch2)
# print(par)
# root = 1
# for i in range(E):
#     tmp = arr[i]                    # tmp: 새로 들어올 값
#     while 1:
#         tmp2 = value[root]          # tmp2 : 현재 노드에 들어있는 값
#         if value[root] > tmp:       # 넣으려는 값이 현재 노드의 값보다 작으면
#             value[root] = tmp       # 현재 노드에 값을 넣고
#             tmp = tmp2              # 현재 노드에 들어있던 값을 내리기
#         else:                       # 넣으려는 값이 현재 노드보다 크면
#             if ch1[root]:
#                 root = ch1[root]
#             elif ch2[root]:
#                 root = ch2[root]

# 해야하는 것
# root 갱신해야 함
# 만약 넣으려는 값이 현재 노드의 값보다 크면 원래 가려던 곳으로 한 칸 움직여야함
#
