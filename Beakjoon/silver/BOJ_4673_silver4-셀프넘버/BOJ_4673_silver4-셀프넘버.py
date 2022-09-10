#BOJ_4673_silver4-셀프넘버

def f(N):
    sol = N
    M = str(N)
    for i in M:
        sol += int(i)
    return sol

lst = []
lst2 = []
for i in range(1, 10000):
    lst.append(i)
    if f(i) < 10000:
        lst2.append(f(i))
for i in lst:
    if i not in lst2:
        print(i)