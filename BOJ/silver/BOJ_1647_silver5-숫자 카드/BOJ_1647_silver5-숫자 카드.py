# BOJ_1647_silver5-숫자 카드

n = int(input())
set1 = set()
set1 = set(map(int, input().split()))
m = int(input())
lst = list(map(int, input().split()))
for i in lst:
    if i in set1:
        print(1,end=' ')
    else:
        print(0,end=' ')