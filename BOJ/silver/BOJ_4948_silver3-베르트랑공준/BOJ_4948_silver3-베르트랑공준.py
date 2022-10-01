# BOJ_4948_silver3-베르트랑공준

while 1:
# 에라토스테네스의 체
    start = int(input().strip())
    end = start * 2
    lst = [0] * (end+1)
    cnt = 0
    if start == 0:
        break
    for i in range(2, int(end**0.5)+1):               # 2부터 끝까지
        if lst[i] == 0:                     # 숫자가 초기화 되어 있을때
            for j in range(i*i, end+1, i):  # 배수가 되려면 적오도 제곱배가 필요
                lst[j] = 1
    for i in range(start+1, end + 1):         # 소수만 출력
        if i != 1 and lst[i] == 0:          # 1은 제외
            cnt += 1
    print(cnt)

