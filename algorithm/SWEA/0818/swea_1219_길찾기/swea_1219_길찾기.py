#swea 1219 길찾기

#출발점은 0 도착점은 99


import sys
sys.stdin = open('input.txt')


for _ in range(10):
    t, n = map(int, input().split())
    lst = list(map(int, input().split()))
    stack = []         #index stack
    dict1 = {}          #그래프를 만들 dictionary
    set_chk = set()     #노드가 이미 존재하는 여부를 확인하는 set
    temp = 0            #set의 크기가 커지는 지 확인하는 변수

    #모든 노드와 간선을 그래프화
    for k in range(0, n*2, 2):
        set_chk.add(lst[k])                 # set에 노드를 key를 추가
        if len(set_chk) > temp:             # set에 새로운 요소가 들어오면
            temp = len(set_chk)             # temp를 갱신
            dict1[lst[k]] = [lst[k+1]]      # 간선을 set으로 저장
            # print('생성', dict1)
        else:
            dict1[lst[k]].append(lst[k+1])  # 노드가 이미 있는 경우
            # print('추가', dict1)

    lst_chk = list(set_chk)                 #set을 list로 생성


    chk = 0  # 길을 찾았는 지 여부를 확인할 변수
    node = 0  # 첫 시작은 0에서 합니다.
    # 검색
    while 1:
        try:
            if len(dict1[node]) > 1:    # 갈림길이면 stack에 추가
                stack.append(node)
            node = dict1[node].pop()  # dictionary에서 자식 노드를 고릅니다.
        except:  # 노드에 자식이 없으면 stact2에서 pop해온다
            try:
                node = stack.pop()
            except:  # stack2가 비어있으면 while문을 나온다.
                break
        if node == 99:
            chk = 1
            break
    print(f'#{t} {chk}')
