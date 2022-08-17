#swea1979 어디에 단어가 들어갈 수 있을까?

# 빈칸을 카운팅하는 함수
def word_counting(lst, dict1):
    for r in lst:
        cnt = 0 #cnt : 빈칸 길이를 구하기 위해 카운팅
        for j, l in enumerate(r):
            length = 0  #빈칸의 길이
            switch = 0  #append 스위치 off
            if l == 0 and cnt != 0: #벽에 부딪힘
                length = cnt    #길이 할당
                cnt = 0         #count 리셋
                switch = 1      #스위치 on
            elif l == 1:        #빈칸이 계속 됨
                cnt += 1
                if j == len(r)-1:   #마지막 칸이 빈칸인 경우
                    length = cnt    #길이 할당
                    switch = 1      #스위치 on
            if switch == 1: #스위치가 켜지면
                if length not in dict1: # 해당 길이가 key에 없으면
                    dict1[length] = 1
                else:                   # 해당 길이가 key에 있으면
                    dict1[length] += 1
    return dict1

T = int(input())

for test_case in range(1,T+1):
    N, K = map(int, input().split())

    map1 = [list(map(int, input().split())) for _ in range(N)]
    map2 = []
    dict1 = {}
    dict1[K] = 0

    # list 반시계 방향으로 90도 회전이동
    for i in zip(*map1):
        map2.append(list(i))    #zip하면 tuple로 저장되므로 list 처리
    dict1 = word_counting(map1, dict1)
    dict1 = word_counting(map2, dict1)

    print(f'#{test_case} {dict1.get(K)}')
