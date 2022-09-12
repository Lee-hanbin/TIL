# BOJ 2475 브론즈5 검증수


lst = list(map(int, input().split()))
sol = 0
for i in lst:
    sol += i**2
print(sol % 10)