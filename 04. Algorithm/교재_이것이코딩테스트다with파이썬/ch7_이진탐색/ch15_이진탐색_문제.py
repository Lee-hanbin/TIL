#ch15 이진탐색 문제

'''
@27 정렬된 배열에서 특정 수의 개수 구하기

#문제
 N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬
 수열에서 x가 등장하는 횟수를 계산
 O(logN)으로 알고리즘을 설계해야함

#입력조건
 첫째 줄: N과 x가 정수 형태로 공백으로 구분되어 입력 (1<=N<=1000000) (1e-9 <= x <= 1e9)
 둘째 줄: 둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력

#출력조건
 값이 x인 원소의 개수 구하기. 없으면 -1 출력
'''

# n, x = map(int, input().split())
# lst = list(map(int, input().split()))
#
# def binary_search(n, x):
#     s = 0
#     end = n - 1
#     while s <= end:
#         mid = (s+end)//2
#         if lst[mid] == x:
#             return mid
#         elif x < lst[mid]:
#             end = mid -1
#         else:
#             s = mid + 1
#     return -1
#
# idx = binary_search(n,x)            # 이진 탐색으로 target 값의 인덱스 찾기
#
# if idx == -1:                       # 못 찾으면 -1
#     print(-1)
# else:                               # 찾았으면 왼쪽과 오른쪽 체크
#     i = idx - 1
#     j = idx + 1
#     cnt = 1
#     while lst[i] == x or lst[j] == x:
#         if lst[i] == x:
#             cnt += 1
#             i -= 1
#         if lst[j] == x:
#             cnt += 1
#             j += 1
#     print(cnt)

'''
@ 29 공유기 설치(BOJ 2110)

# 문제
도현이의 집 N개가 수직선 위에 있음
집의 좌표는 x1,x2,...,xN, 집 여러 개가 같은 좌표를 가지는 일은 없음
공유기 C개 설치 예정
최대한 많은 곳에서 와이파이를 사용하고 싶음
한 집에 공유기는 하나만 설치 가능
가장 인접한 두 공유기 사이의 거리를 가능한 크게하여 설치하고 싶음
C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하게 하라

#입력조건
첫째 줄: N (2~200,000)  C(2~N)
둘째 줄: Xi(1 ~ 1,000,000,000)
'''
import sys
input =sys.stdin.readline

def binary_search(lst,n ,g):
    rst = 0
    s = 1                       # 최소 공유기 사이의 거리
    e = lst[-1] - lst[0]        # 최대 공유기 사이의 거리
    while s <= e:                # c개의 공유기가 설치 가능 할 때 까지 거리를 조절
        mid = (s + e)//2
        C = 1                       # 공유기의 개수를 1개로 잡고
        before = 0                  # 이전 집 인덱스
        after = 1                   # 이후 집 인덱스
        while after < n and C <g:            # 집이 끝까지 가지 않고고 유기 개수가 초과 하지 않으면 반복
            if lst[after] >= lst[before] + mid:     # 이후 집이 이전집 위치 + 중간값 크거나 같으면
                C += 1                              # 공유기 설치
                before, after = after, before +1    # 이전집 인덱스르 이후 집 인덱스로 바꿔주기
            else:                           # 다음 집이  이전 집 + 중간값보다 작으면
                after += 1                  # 이후 집의 크기를 늘려줌
        if C < g:               # 공유기 개수가
            e = mid - 1
        elif g == C:
            rst = mid
            s = mid + 1
        else:
            s = mid + 1

    return rst


n, g = map(int, input().split())

lst = [0] * n
for i in range(n):
    lst[i] = int(input())
lst.sort()


print(binary_search(lst, n, g))