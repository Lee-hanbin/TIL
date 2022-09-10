#BOJ 1546 브론즈1 평균

N = int(input())
lst = list(map(int, input().split()))
max1 = max(lst)
for i, e in enumerate(lst):
    lst[i] = e/max1*100
print(sum(lst) / N)