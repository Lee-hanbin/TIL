N = int(input())
L = list(map(int,input().split()))
 
L.sort()
K = int(N//2)
 
print(L[K])