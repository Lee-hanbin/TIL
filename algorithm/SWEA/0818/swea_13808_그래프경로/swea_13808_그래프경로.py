#swea 13808 그래프 경로

import sys
sys.stdin = open('sample_input(2).txt')

for t in range(int(input())):
    k, v = map(int, input().split())
    lst = []
    dict1 = {}
    set_chk = set()
    temp = 0
    node = 0
    stack = []
    for _ in range(v):
        lst.append(list(map(int, input().split())))
    start , end = map(int, input().split())
    for i in lst:
       set_chk.add(i[0])
       if len(set_chk) > temp:
           temp = len(set_chk)
           dict1[i[0]] = [i[1]]
       else:
           dict1[i[0]].append(i[1])
    node = start
    chk = 0
    while 1:
        try:
            if len(dict1[node]) > 1:  # 갈림길이면 stack에 추가
                stack.append(node)
            node = dict1[node].pop()  # dictionary에서 자식 노드를 고릅니다.
        except:  # 노드에 자식이 없으면 stack에서 pop해온다
            try:
                node = stack.pop()
            except:  # stack이 비어있으면 while문을 나온다.
                break
        if node == end:
            chk = 1
            break

    print(f'#{t+1} {chk}')