# BOJ_5086_bronze3-배수와 약수
while 1:
    n, m = map(int,input().split())
    if n == 0 and m == 0:
        break
    if m % n == 0:
        print('factor')
    elif n % m == 0:
        print('multiple')
    else:
        print('neither')