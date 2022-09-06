# BOJ_17502_bronze2-클레어와팰린드롬
n = int(input())
s = input()
sol = str()
for i in range(n//2):
    if s[i] != '?':
        sol += s[i]
    elif s[n-1-i] != '?':
        sol += s[n-1-i]
    else:
        sol += 'a'
if len(s) % 2 == 1:
    if s[n//2] == '?':
        sol = sol + 'a' + sol[::-1]
    else:
        sol = sol + s[n//2] + sol[::-1]
else:
    sol = sol + sol[::-1]


print(sol)


