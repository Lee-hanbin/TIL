#BOJ_2675_bronze2-문자열반복

for _ in range(int(input())):
    N, s = input().split()
    for i in s:
        print(i*int(N),end='')
    print()
