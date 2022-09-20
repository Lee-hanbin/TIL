# BOJ_1359_silver4-복권

from math import comb

N, M, K = map(int, input().split())

lst = list(range(1,N+1))

fraction = comb(N,M)
numerator = 0

for i in range(K, M+1):
    numerator += (comb(M,i)*comb(N-M,M-i))
print(numerator/fraction)