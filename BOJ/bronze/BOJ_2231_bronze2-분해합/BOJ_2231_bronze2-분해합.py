#BOJ_2231_bronze2-분해합

N = int(input())
# 분해합 구하기
tmp = 1000000
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        M = 100000*a + 10000*b + 1000*c + 100*d + 10*e + f + a + b + c + d + e + f
                        print(M)
                        if N == M:
                            if 100000*a + 10000*b + 1000*c + 100*d + 10*e + f < tmp:
                                tmp = 100000*a + 10000*b + 1000*c + 100*d + 10*e + f
if tmp == 1000000:
    print(0)
else:
    print(tmp)