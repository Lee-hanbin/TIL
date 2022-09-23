# BOJ_1712_bronze2-손익분기점


N, M, l = map(int,input().split())
i = 1
if M > l:
    print(-1)
else:
    while 1:
        if N + i*M <= i*l:
            print(i+1)
            break
        elif N + i*M > i*l:
            i+=1
