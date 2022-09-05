#BOJ 25304번 bronze5 영수증


X = int(input())
sum1 = 0
for _ in range(int(input())):
    N, M = map(int,input().split())
    sum1 += (N*M)
if X == sum1:
    print('Yes')
else:
    print('No')