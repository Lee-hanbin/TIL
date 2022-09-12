# BOJ 4344 브론즈1 평균은 넘겠지

for i in range(int(input())):
    lst = list(map(int, input().split()))
    N = len(lst)-1
    avg = (sum(lst)-lst[0])/N
    cnt = 0
    for i in range(1, N+1):
        if lst[i] > avg:
            cnt += 1
    print(f'{cnt/N*100:.3f} %')             # 출력형식 1
    # print('%.3f' %(cnt/N*100)+'%')        # 출력형식 2