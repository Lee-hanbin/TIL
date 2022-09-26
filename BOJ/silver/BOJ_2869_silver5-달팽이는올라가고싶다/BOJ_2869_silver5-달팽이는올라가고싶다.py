# BOJ_2869_silver5-달팽이는올라가고싶다

# A, B, V = map( int, input().split())
#
# day = 1
# V-=A
# if V > 0:
#     C=V//(A-B)
#     if V%(A-B)!=0:
#         C+=1
#     day+=C
# print(day)

A, B, V = map( int, input().split())

day = 1
if V==A:
    print(day)
else:
    V-=A
    C=V//(A-B)
    if V%(A-B)!=0:
        C+=1
    print(day+C)
