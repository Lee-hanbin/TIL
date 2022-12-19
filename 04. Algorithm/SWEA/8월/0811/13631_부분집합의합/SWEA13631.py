#SWEA13631 부분집합의합

lst = list(range(1, 13))
total = []
# 1~12의 숫자의 부분집합 생성
for i in range(1 << len(lst)):
    subset = []
    for j in range(len(lst)):
        if i & (1 << j):
            subset.append(lst[j])
    total.append(subset)

T = int(input())
for test in range(T):
    N, K = map(int, input().split())
    cnt = 0
    #해당 부분집합의 개수
    for subset in total:
        if len(subset) == N and sum(subset) == K:
            cnt += 1
    print(f'#{test+1} {cnt}')
