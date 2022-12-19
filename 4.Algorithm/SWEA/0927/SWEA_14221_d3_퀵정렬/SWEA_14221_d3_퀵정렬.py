# SWEA_14221_d3_퀵정렬
import time
from random import shuffle
now = time.time()
# 피봇을 정해주는 함수
def pivot_search(lst, l, r):
    length = r - l
    pivot_lst = [[lst[l],l], [lst[length//2], length//2],[lst[r], r]]  # 순회할 리스트의 처음 중간 마지막 값을 넣고
    pivot_lst.sort()                        #
    tmp = pivot_lst[1]
    lst[l], lst[tmp[1]] = lst[tmp[1]], lst[l]
    return tmp[0]

def partition(lst, l, r):
    # 피봇 정해서 첫번째 값과 바꾼 리스트 반환
    pivot = pivot_search(lst, l, r)
    i, j = l, r
    while i <= j:
        while i <= j and lst[i] <= pivot:
            i += 1
        while i <= j and lst[j] >= pivot:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[l], lst[j], = lst[j], lst[l]
    return j

def q_sort(lst, l, r):
   if l < r:
       s = partition(lst, l, r)
       q_sort(lst, l, s-1)
       q_sort(lst, s+1, r)

T = int(input())
for t in range(1,T+1):
    sol = 0
    # N = int(input())
    lst = list(range(1, 50000000))
    shuffle(lst)
    N = len(lst)
    q_sort(lst, 0, N-1)
    print(f'#{t} {lst[N//2]}')

print(time.time() - now)