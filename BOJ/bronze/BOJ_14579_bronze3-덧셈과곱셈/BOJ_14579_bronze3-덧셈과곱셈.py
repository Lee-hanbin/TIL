# BOJ_14579_bronze3-덧셈과곱셈

a, b = map(int,input().split())

sum1 = 0
for i in range(1,a+1):
    sum1 += i
sol = sum1
for i in range(a+1, b+1):
    sum1 += i
    sol *= sum1
print(sol % 14579)