#16926번 배열돌리기

############################################################
#함수#
# 프레임의 값을 정해서 각 프레임 크기를 리스트로 반환
def frame(N ,M, cnt):
    lst_frame = []  # 사각형의 크기
    lst_frame_nm = []   # 사각형의 가로, 세로 크기
    while cnt > 0:
        lst_frame_nm.append([N, M])
        lst_frame.append((N+M)*2-4) #사각형의 요소 개수 = (가로 + 세로) * 2 - 4
        N -= 2
        M -= 2
        cnt -= 1
    return lst_frame, lst_frame_nm

# 중복을 줄여주기 위해 R을 각 프레임마다 재설정
def new_R(lst_frame, R):
    lst_new_R = []
    for i in range(len(lst_frame)):
        lst_new_R.append(R % lst_frame[i])  # n 바퀴 돌리는 경우 제거
    return lst_new_R

# tuple로 list_idx만들기
def idx(cnt ,chk ,lst_frame_nm):
    list_index = []
    x, y = cnt, cnt
    max1_x = lst_frame_nm[cnt][0] +cnt -1   # 작은 사각형은 (1,1) => (2,2) => ..로 시작하기때문에
    max1_y = lst_frame_nm[cnt][1] +cnt -1

    for _ in range(chk):
        list_index.append((x ,y))
        if y == cnt and x != max1_x:
            x += 1
        elif x == max1_x and y != max1_y:
            y += 1
        elif y == max1_y and x != cnt:
            x -= 1
        else:
            y -= 1

    return list_index

# list를 돌리는 함수
def doladola(lst, lst_idx, lst_new_idx, lst_frame_nm):
    # 왼쪽으로 갈때는 j :-1    => 0나오면 아래로
    # 아래쪽으로 갈때는 i :+1   => N나오면 오른쪽으로
    # 오른쪽으로 갈때는 j :+1   => M나오면 위쪽으로
    # 위쪽으로 갈때는 i :-1    => 0나오면 왼쪽으로
    # 튜플로 list idx를 만들어서 바로 옮겨서 다시찍을까?
    lst_new = [[0]*lst_frame_nm[0][1] for _ in range(lst_frame_nm[0][0])]
    for i in range(len(lst_new_idx)):   # 사각형 개수만큼 돌리기
        for j in range(len(lst_new_idx[i])):    # 각 사각형의 크기만큼 돌리기
            x = lst_new_idx[i][j][0]
            y = lst_new_idx[i][j][1]
            N = lst_idx[i][j][0]
            M = lst_idx[i][j][1]
            lst_new[N][M] = lst[x][y]
            # print(f'({N,M}), ({x,y})')
    return lst_new


#############################################################
#메인#

N, M, R = map(int, input().split()) #N:행 M:열
lst = [list(map(int, input().split())) for _ in range(N)]


cnt = int(min(N ,M)/2)   #사각형의 개수= 짝수/2

lst_frame ,lst_frame_nm = frame(N, M, cnt)
lst_new_R =new_R(lst_frame, R)

# 튜플을 요소로 갖는 인덱스 리스트 생성
lst_idx = []
for i in range(cnt):
    lst_idx.append(idx(i ,lst_frame[i], lst_frame_nm))

lst_new_idx = []

# 사이클을 반시계방향으로 돌린 후, idx
for i in range(cnt):
    lst_cf = []
    for j in range(len(lst_idx[i])):
        # ((전체 - 실제 돌릴 횟수) + 해당 튜플번호) % 사각형 크기
        c = ((lst_frame[i] -lst_new_R[i]) + j) % lst_frame[i]
        lst_cf.append(lst_idx[i][c])   #새로운 idx 생성
    lst_new_idx.append(lst_cf)

# # 사이클을 시계방향으로 돌린 후, idx
# for i in range(len(lst_frame)):
#     lst_cf = []
#     for j in range(len(lst_idx[i])):
#         c = (lst_new_R[i] + j) % lst_frame[i]   #(실제 돌릴 횟수 + 해당 튜플번호) % 사각형 크기
#         lst_cf.append(lst_idx[i][c])   #새로운 idx 생성
#     lst_new_idx.append(lst_cf)

# 다 돌아간 리스트 출력
lst = doladola(lst, lst_idx, lst_new_idx, lst_frame_nm)
for i in range(len(lst)):
    print(*lst[i])