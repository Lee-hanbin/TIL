# BOJ_11399_silver4-ATM

n = int(input())
lst = sorted(list(map(int,input().split())))
sol = [0] * n
chk = 0
for i,e in enumerate(lst):
    chk += e
    sol[i] = chk
print(sum(sol))
