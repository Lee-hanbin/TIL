#BOJ 8958 bronze2 OX퀴즈

for _ in range(int(input())):
    sum1 = []
    cnt = 0
    str_OX = input() + 'Z'
    for i in str_OX:
        if i == 'O':            # O면 cnt
            cnt += 1
            sum1.append(cnt)    # cnt 한 값을 리스트에 넣기
        elif i == 'X':          # X면 cnt 초기화
            cnt = 0
        else:                   # Z나오면 break
            break
    print(sum(sum1))            # cnt들을 더함