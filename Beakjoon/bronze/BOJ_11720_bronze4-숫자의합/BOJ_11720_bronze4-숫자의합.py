#BOJ_11720_bronze4-숫자의합

N = int(input())
s = input()
sol = 0
for i in s:
    sol += int(i)
print(sol)