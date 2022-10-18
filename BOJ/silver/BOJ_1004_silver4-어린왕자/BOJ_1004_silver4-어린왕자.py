# BOJ_1004_silver4-어린왕자

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int,input().split())
    n = int(input())
    sol = 0
    for i in range(n):
        cx, cy, r = map(int,input().split())
        chk = 0
        if (cx-x1)**2+(cy-y1)**2 <= r**2:
            chk +=1
        if (cx-x2)**2+(cy-y2)**2 <= r**2:
            chk +=1
        if chk == 1:
            sol += 1
    print(sol)
