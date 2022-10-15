# BOJ_3009_bronze3-네번째점

x = []
y = []
sol = []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
for i in x:
    if x.count(i) == 1:
        sol.append(i)
for i in y:
    if y.count(i) == 1:
        sol.append(i)
print(*sol)