# BOJ_4153_bronze3-직각삼각형

t = 1

while 1:
    lst = list(map(int, input().split()))
    lst.sort()
    t = lst[0]
    if t == 0:
        break
    if lst[2]**2 == lst[1]**2 + lst[0]**2:
        print('right')
    else:
        print('wrong')
