#BOJ 8393_bronze5-합
N = int(input())
sol = (1 + N) * (N//2)
if N % 2 == 1:
    sol += N//2 + 1
print(sol)
