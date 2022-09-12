#BOJ 2884번 브론즈 3 알람시계

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

if b >= 45:
    print(f'{a} {b-45}')
else:
    if a == 0:
        print(f'{(a+24 - 1) % 24} {b + 60 - 45}')
    else:
        print(f'{a-1} {b + 60 - 45}')