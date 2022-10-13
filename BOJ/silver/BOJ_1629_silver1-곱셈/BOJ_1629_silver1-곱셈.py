# BOJ_1629_silver1-곱셈

'''
모듈러의 계산 성질
A = B + K * C
=> A mod C = B mod C
1. 덥셈 : (a+b) % c = ((a%c) + (b%c)) %c
2. 빨셈 : (a-b) % c = ((a%c) - (b%c)) %c
3. 곱셈 : (a*b) % c = ((a%c) * (b%c)) %c
4. 나눗셈 => b와 c가 서로소이면 가능
'''

def power(a,b,c):
    if b == 1:
        return a%c
    elif b == 2:
        return a*a%c
    if b % 2 == 1:
        return (power(a,b//2,c)**2)*a%c
    else:
        return power(a, b//2,c)**2%c
a, b, c = map(int,input().split())

print(power(a,b,c))
