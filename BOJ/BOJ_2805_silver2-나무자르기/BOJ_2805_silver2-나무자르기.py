# BOJ_2805_silver2-나무자르기
'''
@문제
절단기 높이 H
나무를 일렬로 세워놓고 한번에 자릅니다.
위로 잘린 나무만 가져 갑니다
H는 양의 정수 또는 0
적어도 M 미터의 나무를 가져가기 위한 H의 최대값은?

@ 입력조건
첫째 줄 : 나무의 수 N(1~100만) , 가져갈 나무의 길이 M(1~20억)
둘째 줄 : 나무들의 높이 ( 0 ~ 10억)
'''

import sys
from heapq import *
input = sys.stdin.readline

def binary(lst, M):
    start = 1
    end = lst[-1]
    while start <= end:
        H = 0
        mid = (start + end) // 2
        for i in lst:
            if i > mid:
                H += i - mid
        if H == M:
            return mid
        elif H < M:
            end = mid - 1
        else:
            start = mid + 1
    return end

N, M = map(int, input().split())
lst = list(map(int, input().split()))
heapify(lst)
lst_sort = []
while lst:
    lst_sort.append(heappop(lst))
print(binary(lst_sort, M))


