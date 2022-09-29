# BOJ_7568_silver5-덩치

N = int(input())
lst = []
for i in range(N):
    n, m = map(int,input().split())
    lst.append([n,m])
lst_sol = []
for i in range(N):
    cnt = 0
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt += 1
    lst_sol.append(cnt+1)
print(*lst_sol)