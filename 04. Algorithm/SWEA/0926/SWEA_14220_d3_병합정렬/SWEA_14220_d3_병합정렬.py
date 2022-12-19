# SWEA_14220_d3_병합정렬

from collections import deque

def merge_sort(lst):
    global cnt
    if len(lst) == 1:
        return lst
    middle = len(lst)//2

    left = lst[:middle]
    right = lst[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    if left[-1] > right[-1]:
        cnt += 1

    return merge(left, right)

def merge(left, right):
    rst = []
    left = deque(left)
    right = deque(right)
    while left or right:
        if left and right:
            if left[0] <= right[0]:
                rst.append(left.popleft())
            else:
                rst.append(right.popleft())
        elif left:
            rst.extend(left)
            break
        elif right:
            rst.extend(right)
            break
    return rst

T = int(input())
for t in range(1,T+1):
    sol = 0
    cnt = 0
    n = int(input())
    lst = list(map(int, input().split()))
    lst = merge_sort(lst)
    print(f'#{t} {lst[n//2]} {cnt}')