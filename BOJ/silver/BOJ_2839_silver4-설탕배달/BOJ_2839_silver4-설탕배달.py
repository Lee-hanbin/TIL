# BOJ_2839_silver4-설탕배달

n = int(input())

if n == 4 or n == 7:
    print(-1)
else:
    if n % 5 == 0:
        print(n//5)
    else:                                   # 14
        c = n//5                            # c = 2
        i = 1                               # i = 1
        while 1:
            if n == c*5 + 3*i:              # 13            # 11
                print(c + i)
                break
            else:
                if c == 0:
                    i += 1
                elif n >= c*5 + 3*(i+1):     # 15 < 16       #  1 > 14
                    i += 1
                else:
                    c -= 1                  # c = 1
                    i += 1                  # i = 2