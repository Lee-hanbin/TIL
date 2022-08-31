# BOJ 2480번 브론즈 4 주사위 세개

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
chk = {a, b, c}
if len(chk) == 1:
    print(a *1000 + 10000)
elif len(chk) == 2:
    if a == b or a == c:
        print(1000+a*100)
    else:
        print(1000+b*100)
else:
    print(max(a, b, c)*100)