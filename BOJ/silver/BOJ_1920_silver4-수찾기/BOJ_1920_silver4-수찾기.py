#BOJ_1920_silver4-수찾기

import sys
input = sys.stdin.readline

# 이진탐색
def binary(lst, N, key):
    start = 0
    end = N -1
    while start <= end:
        middle = (start + end) //2
        if lst[middle] == key:
            return 1
        elif lst[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return 0

N = int(input())
lst1 = list(map(int, input().split()))
M = int(input())
lst2 = list(map(int, input().split()))
lst2 = lst2[::-1]                   # pop의 효율성을 위해 뒤집기
lst1.sort()                         # 이진탐색을 위해 정렬

while lst2:
    e = lst2.pop()
    print(binary(lst1, N, e))
