#swea 13808 그래프 경로

import sys
sys.stdin = open('sample_input(2).txt')

for t in range(int(input())):
    chk = 0
    top = -1
    stack1 = []         #stack
    stack2 = []         #index stack
    dict1 = {}          #그래프를 만들 dictionary
    set_chk = set()     #노드가 이미 존재하는 여부를 확인하는 set
    temp = 0            #set의 크기가 커지는 지 확인하는 변수
    #모든 노드와 간선을 그래프화
    while 1:
        try:
            k, v = map(int, input().split())
        except:                     #input하는데 에러가 발생하면
            break                   #빠져나와
        set_chk.add(k)              #set에 노드를 key를 추가
        if len(set_chk) > temp:     #set에 새로운 요소가 들어오면
            temp = len(set_chk)     #temp를 갱신
            dict1[k] = {v}          #간선을 set으로 저장
            # print('생성', dict1)
        else:
            dict1[k].add(v)         #노드가 이미 있는 경우
            # print('추가', dict1)
    set_chk = list(set_chk)         #set으로 만든 node를 list로 변환
    chk = set_chk[0]
    #첫번째 노드를 기준으로 연결된 노드 확인
    while 1:
        if len(dict1[chk]) > 1:
            push(stack1, chk)
            push(stack2, chk)
        elif dict1[chk] == None:
            try:
                chk = pop(stack2)
            except:
                break
        else:
            push(stack1, chk)
        chk = dict1[chk].pop()
        dict1[chk].pop()

    if length(stack1) == 0:
        print(f'#{t+1} 0')
    else:
        print(f'#{t+1} 1')