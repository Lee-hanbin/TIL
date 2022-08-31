# BOJ 2753번 브론즈 5 윤년

y = int(input())
sol = 0

if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print(1)
else:
    print(0)