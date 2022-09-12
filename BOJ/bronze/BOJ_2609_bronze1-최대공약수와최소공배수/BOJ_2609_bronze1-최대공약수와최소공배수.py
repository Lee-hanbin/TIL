#BOJ_2609_bronze1-최대공약수와최소공배수

N, M = map(int, input().split())

R = min(N,M)
T = max(N,M)

# 최대공약수
for i in range(R,0,-1):
    if N % i == 0 and M % i == 0:
        print(i)
        break

# 최소공배수
i = 0
j = 1
switch = 1
while switch == 1:
    i += 1
    a = T*i             # 큰 값을 한번씩 더 더해줌
    b = 0
    while a > b:        # 큰 값의 배수보다 작은 값의 배수가 커지면 break
        b = R * j       # 작은 값을 한번씩 더 더해줌
        if a == b:      # 두 값이 같으면 스위치를 켜고 break
            switch = 0
            print(b)
            break
        j += 1
