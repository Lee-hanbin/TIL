#ch11_그리디_문제

'''
#1. 모험가 길드
@문제
모험가 N명 , N명을 대상으로 공포도 측정
공포도가 X인 사람은 최소 X명의 그룹원을 모아야 모험 가능
여행을 떠날 수 있는 최대 그룹 수를 구하여라
모든 모험가가 여행을 떠날 필요는 없다.

@입력조건
첫째 줄: 모험가의 수 N 입력 (1 ~ 100000)
둘째 줄: 각 모험가의 공포도의 값을 N이하의 자연수로 주어지며, 공백으로 구분

@input
5
2 3 1 2 2
@Output
2
'''

# N = int(input())
# lst = list(map(int, input().split()))
# lst.sort(reverse=True)
# i = 0
# cnt = 0
# while N > 0:
#     for _ in range(lst[i]):     # 가장 높은 숫자를 기준으로
#         N-=1                    # 남은 인원을 하나씩 줄여서
#         i+=1                    # 그룹이 지어지면 하나씩 늘리고
#     cnt += 1                    # 그룹 하나당 1씩 증가
# print(cnt)


'''
#2. 곱하기 혹은 더하기
@문제
각 자리가 숫자 0 ~ 9 로 이루어진 문자열 S가 존재
왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 '*' or '+' 연산자를 넣음
결과정으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.
항상 20억 이하의 정수가 입력

@입력조건
숫자로 구성된 하나의 문자열

@input          @input2
02984           567
@output         @output
576             210
'''

# lst = list(map(int, input().strip()))
# lst.sort(reverse=True)              # 내림차순
# sol = 1
# for i in lst:
#     if i == 0:                      # 0나오면 그만
#         break
#     else:                           # 0아니면 곱해
#         sol *= i
# print(sol)

'''
#3. 문자열 뒤집기(BOJ 1439)
@문제
0과 1로만 이루어진 문자열을 입력받기
문자열의 모든 숫자를 동일하게 만들고 싶음

@조건
1. 연속되는 숫자 뒤집기
2. 전체 뒤집기

@입력조건
1. 길이가 100이하인 0과 1로만 이루어진 문자열을 입력받음

'''
#
# lst = list(map(int, input().strip()))
# if lst[-1] == 0:           # 마지막 문자가 0 이면 1을 넣고
#     lst.append(1)
# else:                      # 마지막 문자가 1 이면 0 넣기
#     lst.append(0)
# cnt0, cnt1 = 0, 0
# tmp = 0
# for i, e in enumerate(lst):
#     if i == 0:              # 첫 숫자 할당
#         tmp = e
#         continue
#     if e == 0:              # 해당 숫자가 0이면
#         if tmp == 0:        # 이전에 0이었으면 그냥 바꾸고
#             continue
#         else:               # 이전에 1이었으면 counting 해주고
#             tmp = 0         # tmp 갱신
#             cnt0 += 1       # 0을 뒤집었을 경우, 카운팅
#     else:                   # 해당 숫자가 1이면
#         if tmp == 1:        # 이전에 1이었으면 그냥 바꾸고
#             continue
#         else:               # 이전에 0이었으면 counting 해주고
#             tmp = 1         # tmp 갱신
#             cnt1 += 1       # 1을 뒤집었을 경우, 카운팅
# print(min(cnt0, cnt1))

'''
#4. 만들 수 없는 금액
@문제
동빈이가 N개의 동전을 가지고 있음
N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하라.

@입력조건
첫째 줄 : 동전의 개수 양의 정수 N
둘째 줄 : 각 동전의 화폐 단위 N개 입력, 공백으로 구분 화폐단위는 1,000,000이하

@input
5
3 2 1 1 9
@output
8
'''

# N = int(input())
# lst = list(map(int, input().split()))
# for i in range(N):
#     sol = lst[i]
#     for j in range(i+1, N):     # lst에 화폐로 만들 수 있는 모든 경우의 수를 담는다.
#         sol += lst[j]
#         lst.append(sol)
# lst = set(lst)
# lst = list(lst)
# for i in range(1, lst[-1]+1):   # lst의 가장 큰 값 이전에 나올 수 있는 숫자들 순회
#     if i not in lst:            # 없는 값이 존재하면 출력
#         print(i)
#         break

'''
#5. 볼링공 고르기
@문제
서로 무게가 다른 볼링공을 고르려고 함
볼링공은 총 N개가 있으며 각 볼링공마다 무게가 적혀 있음
공의 번호는 1번부터 순서대로 부여
같은 무게의 공이 있더라도 다른 공으로 생각

@입력 조건
첫째 줄 : 볼링공의 개수 N (1~1000), 공의 최대 무게 M(1~10)
둘째 줄 : 볼링공의 무게, 공백으로 구분

@input              @input2
5 3                 8 5 
1 3 2 3 2           1 5 4 3 2 4 5 2
@output             @output2
8                   25
'''

# N, M = map(int, input().split())
# lst = list(map(int, input().split()))
# cnt = 0
# for i in range(N):
#     for j in range(i+1, N):
#         if lst[i] == lst[j]:    # 무게가 같으면 카운팅 하지 않음
#             continue
#         cnt += 1
# print(cnt)

'''
#6. 무지의 먹방 라이브
@문제
회전판에 먹어야 할 N개의 음식 존재
각 음식에는 1~N의 번호가 붙어있음
1. 무지는 1번 음식부터 먹기 시작하고, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓음
2. 마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 온다.
    - 다음 음식이란, 아직 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식
3. 회전판이 다음 음식을 무지 앞으로 가져오는데 걸리는 시간은 없다고 가정
무지가 먹방을 시작한 지 K초 후에 네트워크 장애로 방송 일시 중단
네트워크가 정상화 되어 다시 방송을 이어갈 때, 몇 번 음식부터 섭취해야 하는가?

@제한사항
1. food_times는 각 음식을 모두 먹는데필요한 시간이 음식의 번호 순서대로 들어가 있음
2. k는 방속이 중단된 시간을 나타냄
3. 만약 더 섭취가 필요한 음식이 없으면 -1 반환

@정확성 테스트 제한 사항
1. food_times의 길이는 1 ~ 2000
2. food_times의 원소는 1 ~ 100,000,000 의 자연수
3. k는 1~ 2*10^13 의 자연수

'''

# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1
#     answer = 0
#     i = 0
#     l = len(food_times)
#     while k > -1:
#         i = i % l
#         if food_times[i] == 0:
#             i+=1
#             continue
#         food_times[i] -= 1
#         i+=1
#         k-=1
#
#     answer = (i - 1) % l + 1
#     return answer
