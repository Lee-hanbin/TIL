# BOJ_1427_silver5-소트인사이드

lst = list(input().strip())
lst.sort(reverse=True)
sol = str()
for i in lst:
    sol += i
print(sol)