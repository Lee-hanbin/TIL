#BOJ_1654_silver2-랜선자르기

import sys
input = sys.stdin.readline

# 이진탐색
def binary(start,end,lst,middle,K):
    cnt = 0
    for i in lst:                   # 랜선의 개수 카운팅
        cnt += i//middle
    if cnt < K:                     # 랜선의 개수가 지정된 것보다 작으면
        return start, middle-1, cnt # 더 짧게 자르고
    else:                           # 많으면 더 길게 자르고
        return middle + 1, end, cnt

K, N = map(int, input().split())
lst = []
for i in range(K):
    lst.append(int(input()))
end = max(lst)
start = 1
middle = end//2 + 1
cnt = 0
lst2 = []
# 끝까지 탐색
while start <= end:
    start, end, cnt = binary(start, end, lst, middle, N)
    if cnt >= N:                    # 랜선의 길이가 지정된 것보다 많으면
        lst2.append(middle)         # 리스트에 넣기
    middle = (start + end)//2
print(max(lst2))                    # 최대값 뽑기