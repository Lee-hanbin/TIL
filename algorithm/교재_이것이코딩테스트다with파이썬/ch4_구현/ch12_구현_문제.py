#ch12 구현 문제

'''
#7 럭키 스트레이트 (BOJ 18406)
@문제
아웃복서 캐릭터는 필살기인 '럭키 스트레이트' 기술이 있다.
특정 조건에서만 사용 가능
조건 1. 현재 캐릭터의 점수(N) 자릿수 기준으로 점수를 N으로 나누어 왼쪽과 오른쪽의 각 자릿수 합이 동일하면 필살기 사용가능

@입력조건
첫째 줄: 점수 N이 주어짐 (10 ~ 99,999,999), 단, N의 자릿수는 항상 짝수

@출력조건
필살기 사용 가능 : LUCKY
필상기 사용 불가 : READY

@input
123402
@output
LUCKY
'''

# import sys
# input = sys.stdin.readline
#
# lst = list(map(int,input().strip()))    # N자리 숫자를 각 자리 리스트로 받기. 한자리씩 받으므로 strip을 통해 널값 제거
# length = len(lst)
# left, right = 0, 0
# for i in range(length//2):              # 투 포인트
#     left += lst[i]                      # 왼쪽만 더하고
#     right += lst[length-1-i]            # 오른쪽만 더하고
# if left == right:                       # 같으면 LUCKY
#     print("LUCKY")
# else:                                   # 다르면 READY
#     print("READY")

'''
@리뷰
1.문제가 간단하여 구상한 것 처럼 바로 구현 가능했다.
2.lst를 한 자씩 입력 받을 떄는 반드시 strip을 통해 '\n'을 지워줘야 함을 잊지 말자.
3.투포인트로 하나의 for문을 통해 돌린 것 보다 for문 2개로 돌린 것이 실행시간이 적게 나왔다.. 왜 그럴까?
=> 아마도 length-1-i라는 연산을 지속적으로 해줘서 그런 것 같다.
=> for문을 2개 돌리면 그래봤자 O(n) 인데, for문이 돌아갈때마다 연산이 들어가면 O(n^2)이 되지 않을까?
'''


'''
#8 문자열 재정렬 
@문제
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주짐
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤, 모든 숫자를 더한 값을 이어서 출력

@입력조건
첫째 줄: 문자열 S가 주어짐 ( 1 ~ 10000) 

@input1
K1KA5CB7

@input2
AJDLSI412K4JSJ9D

@output1
ABCKK13

@output2
ADDIJJJKKLSS20

'''

# s = list(input().strip())   # 문자열읜 sort 메서드 사용 불가
# s = input().strip()
# s = sorted(s)                 # 문자열은 sorted만 가능 sort 메서드는 리스트의 메서드!! => sorted로 해도 sort로 받음
# sol = 0
# chk = ''
# for i,e in enumerate(s):
#     if e.isdigit():
#         sol += int(e)
#     else:
#         chk += e
# s = chk
# print(f'{s}{sol}')

'''
@리뷰
1. .sort 메서드는 리스트를 위한 메서드이기 떄문에 문자열에 사용 불가
2. sorted 함수를 사용하면 list => sort 하여 list로 생성되어 정렬됨 
'''

'''
#9. 문자열 압축
@문제
데이터 처리 전문가가 되고 싶은 '어피치'는 문자열을 압축하는 방법에 대해 공부를 하고 있다.
최근에는 문자열에서 같은 패턴이 연속으로 나오는 것을 문자열 앞에 숫자가 나오도록 하여 문자열을 줄여서 표현하는 알고리즘으 공부
문자열의 길이를 최소로 만들도록 줄이고 그 길이를 출력
ex) aabbaccc => 2a2ba3c
    ababcdcdababcdcd => 2ab2cd2ab2cd 
                     => 2ababcdcd 

@제한사항
1.s의 길이는 1~1000
2.s는 소문자

@input                          @output
aabbacc                         7
ababcdcdababcdcd                9
abcabcdede                      8
abcabcabcabcdededededede        14
xababcdcdababcdcd               17
'''



# s = input().strip()
#
# lst = []
# for i in range(len(s)//2):                       # 문자열 한칸씩 옆으로 가는 for문
#     for j in range(2+i,len(s)-2-i):                  # 슬라이싱 할 for문 최소 2개
#         s2 = s
#         find_s = s2[i:j]
#         print(find_s)
#         s2.replace(find_s, '1')
#         print(s2)
#         lst.append(len(s2))
#
# print(min(lst))

'''
#10. 자물쇠와 열쇠
@문제
특이한 형태의 열쇠와 자물쇠를 푸는 방법에 대해 다음과 같이 설명해주는 종이가 발견
자물쇠는 격자 한 칸의 크기가 1 x 1 인 N x N 크기의 정사각 격자 형태
열쇠는 M x M 크기인 정사각 격자 형태로 되어 있음
자물쇠는 홈이 파여 있고
열쇠는 홈 및 돌기가 존재
열쇠의 돌기 부분이 자물쇠의 홈에 맞으면 자물쇠가 열림 (열쇠는 회전이동 가능)
열 수 있으면 true
열 수 없으면 false

'''

# def search(lst, lock, chk_lst, N, M):
#     # 중간에 답을 만나면 멈추게 해주게 하기 위해 함수로 정의
#     def pp():
#         # 키의 우측하단이 자물쇠의 좌측상단에 맞을 때부터
#         # 키의 좌측상단이 자물쇠의 우측하단에 맞을 때까지 반복
#         for i in range((M-1)+N):
#             for j in range((M-1)+N):
#                 # 먼저 홈이 다 맞는 지 확인하는 함수
#                 def chk(i, j):
#                     # 미리 구해둔 자물쇠의 홈과 키의 돌기가 맞는 지 확인
#                     for pair in chk_lst:
#                         r, c = pair
#                         # r이 키의 틀 안에 있고 해당 위치의 키가 돌기이면 계속 진행
#                         if i <= r <= i+M-1 and j<= c <= j+M-1 and lst[r-i][c-j] == 1:
#                             continue
#                         else:                   # 그렇지 않으면 답일 확률 x => False
#                             return False
#                     else:                       # 모든 자물쇠의 홈과 키의 돌기가 맞으면 True
#                         return True
#                 # 홈이 다 맞은 경우, 키의 돌기와 자물쇠의 돌기가 맞닿는 경우를 체크
#                 if chk(i,j) == True:
#                     def chk2(i,j):
#                         for r2 in range(M-1,M+N-1):
#                             for c2 in range(M-1,M+N-1):
#                                 if i <= r2 <= i+M-1 and j<= c2 <= j+M-1:
#                                     if lst[r2-i][c2-j] == 1 and lock[r2-(M-1)][c2-(M-1)] == 1:
#                                         return False
#                         # 다른 하자가 없으면 True
#                         else:
#                             return True
#                     if chk2(i,j) == True:
#                         return True
#         # 끝까지 돌려도 답이 안나오면 False
#         else:
#             return False
#     return pp()
#
# def solution(key, lock):
#     N = len(lock)
#     M = len(key)
#     ans = False
#     chk_lst = []
#     # 자물쇠를 체그하여 홈이 있는 좌표를 리스트에 담는다.
#     for i in range(N):
#         for j in range(N):
#             if lock[i][j] == 0:
#                 chk_lst.append((i+(M-1),j+(M-1)))
#     # 90도씩 돌리면서 확인
#     for i in range(4):
#         # 만약 열쇠가 맞으면 True 반환하고 멈추기
#         if search(key, lock, chk_lst, N, M):
#             ans = True
#             break
#         # 만약 열쇠가 맞지 않으면 90도 돌리고 더 해보기
#         else:
#             key = list(zip(*key[::-1]))
#
#     return ans
#
# k_n = int(input())
# l_n = int(input())
# k_lst = [list(map(int, input().split())) for _ in range(k_n)]
# l_lst = [list(map(int, input().split())) for _ in range(l_n)]
#
# solution(k_lst,l_lst)

'''
@리뷰
1. 처음 시작할 때는 풀이가 눈에 보인다고 생각했으나, 생각보다 구현에 오랜시간이 걸렸다.
2. 풀이가 길어지다보니 사소한 실수들이 발목을 계속 잡았다.
3. 이제 웬만한 배열문제는 잘 풀 수 있지 않을까..?
'''



'''
#12. 기둥과 보 설치
빙하가 깨지면서 죠르디는 기둥과 보를 이용하여 벽면 구조물을 자동으로 세우는 로봇을 개발할 예정
기둥 : 1. 바닥 위에 있거나 2. 보의 한쪽 끝부분 위에 있거나 3. 다른 기둥 위에 존재
보 : 1. 한쪽 끝부분이 기둥 위에 있거나 2. 양쪽 끝부분이 다른 보와 동시에 연결 

'''

def solution(n, build_frame):
    answer = [[]]
    build_frame.sort(key=lambda x: (x[0], x[1]))
    for i in range(n):
        c, r, a, b = build_frame[i]
        if len(answer) == 0:
            if a == 0:
                answer.append([c,r,a])
        else:
            if a == 1:          # 구조물이 보이면
                if b == 1:      # 설치
                    if answer[-1][2] == 0 and answer[-1][0] == c:
                        answer.append([c,r,a])
                    elif answer[-1][2] == 1 and answer[-1][1] == r:
                        answer.append([c,r,a])
                else:           # 삭제
                    pass
            else:               # 구조물이 기둥이면
                if b == 1:      # 설치
                    if r == 0:  # 바닥이면 
                        answer.append([c,r,a])
                    elif answer[-1][2] == 1 and answer[-1][1] == r:
                        answer.append([c,r,a])
                    elif answer[-1][2] == 0 and answer[-1][0] == c:
                        answer.append([c,r,a])
                else:           # 삭제
                    pass
            answer = answer[1:]
    return answer

lst = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
solution(5, lst)