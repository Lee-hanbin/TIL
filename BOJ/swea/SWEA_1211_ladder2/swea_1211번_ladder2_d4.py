# swea 1211번 ladder2

import sys
import copy
sys.stdin = open('input.txt')

def search(map1, start, cf):
    start_x = 1
    start_y = start
    switch = 0
    map1[start_x][start_y] = ' '
    cnt = 0
    while switch == 0:
        for i in range(3):
            x = start_x + dx[i]
            y = start_y + dy[i]
            if map1[x][y] == 1:
                map1[x][y] = ' '
                if y != start_y:
                    cnt += 1
                start_x = x
                start_y = y
                break
            elif map1[x][y] == 3:
                switch = 1
                break
        if cf < cnt:                # 만약 이전 값보다 커지면
            return cf               # 이전 값을 반환해라
    return cnt                      # 아니면 현재 값을 반환해라
for _ in range(10):
    test_case = int(input())
    map1 =[[0] * 102] + [[0] +list(map(int, input().split())) + [0] for _ in range(100)] + [[3] * 102]
    sol = 0
    # 좌우하
    dx = [0, 0, 1]
    dy = [-1, 1, 0]
    start = []                          # 좌,우, 하단에 리스트의 요소를 추가했으므로 인덱스에 유의
    for i, e in enumerate(map1[1]):
        if e == 1:
            start.append(i)
    map2 = copy.deepcopy(map1)
    temp = 0
    for i in range(len(start)):
        if i == 0:
            cnt = search(map2, start[0], 100000)
        else:
            map2 = copy.deepcopy(map1)
            temp = cnt
            cnt = search(map2, start[i], cnt)
        if temp != cnt:
            sol = start[i]
    print(f'#{test_case} {sol-1}')

        # for i in map2:                # 길을 잘 가나 확인
        #     print(*i)


# swea 1211번 ladder2

# def search(map1, start):
#     start_x = 1
#     start_y = start
#     switch = 0
#     map1[start_x][start_y] = ' '
#     cnt = 0
#     while switch == 0:
#         for i in range(3):
#             x = start_x + dx[i]
#             y = start_y + dy[i]
#             if map1[x][y] == 1:
#                 map1[x][y] = ' '
#                 if y != start_y:
#                     cnt += 1
#                 start_x = x
#                 start_y = y
#                 break
#             elif map1[x][y] == 3:
#                 switch = 1
#                 break
#     return cnt                      # 아니면 현재 값을 반환해라
# for _ in range(10):
#     test_case = int(input())
#     map1 =[[0] * 102] + [[0] +list(map(int, input().split())) + [0] for _ in range(100)] + [[3] * 102]
#     sol = 0
#     # 좌우하
#     dx = [0, 0, 1]
#     dy = [-1, 1, 0]
#     start = []                          # 좌,우, 하단에 리스트의 요소를 추가했으므로 인덱스에 유의
#     for i, e in enumerate(map1[1]):
#         if e == 1:
#             start.append(i)
#     lst_sol = []
#     for i in range(len(start)):
#         map2 = copy.deepcopy(map1)
#         lst_sol.append(search(map2, start[i]))
#     sol = lst_sol.index(min(lst_sol))
#     print(f'#{test_case} {start[sol]-1}')
#
#         # for i in map2:                # 길을 잘 가나 확인
#         #     print(*i)
#
#
