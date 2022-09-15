# BOJ_10250_bronze2-ACM호텔

for _ in range(int(input())):
    floor, ho, find = map(int,input().split())
    lst = [[0] * ho for _ in range(floor)]
    if find % floor == 0:                   # 플로어가 꼭대기일 때
        sol_floor = floor                   # floor로 나눠 줬으므로 floor 일 경우 따로 따져줘야함
        sol_ho = find // floor              # ho도 마찬가지로 넘어가지 않고 하나 줄여줘야함
    else:
        sol_floor = find % floor            # 꼭대기가 아니면 층수로 나눈 나머지가 층수
        sol_ho = find // floor + 1          # 꼭대기가 아니면 층수로 나눈 몫이 호수
    sol_floor = str(sol_floor)
    if sol_ho < 10:
        sol_ho = '0' + str(sol_ho)
    else:
        sol_ho = str(sol_ho)

    print(int(sol_floor + sol_ho))
