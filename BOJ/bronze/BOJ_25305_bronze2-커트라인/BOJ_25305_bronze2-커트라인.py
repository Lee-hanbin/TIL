# # BOJ_25305_bronze2-커트라인
#
# n, k = map(int,input().split())
#
# lst = list(map(int,input().split()))
#
# print(sorted(lst,reverse=True)[k-1])

n = int(input())
i = 2
while n > 1:
    if n % i == 0:
        n //= i
        print(i)
    else:
        i+=1
