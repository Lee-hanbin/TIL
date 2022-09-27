# BOJ_1697_silver1-숨바꼭질

n, m = map(int, input().split())

if n > m:
    n, m = m, n
if m % 2 == 1:
    num_1 = m -1
    i = 1
    num_2 = m +1
    j = 1
    while num_1 > n:
        num_1 //= 2
        i += 1
    while num_2 > n:
        num_2 //= 2
        j += 1

    while num_1 ==n or num_2 ==n:
        if num_1 > n:
            num_1 -= 1
            i+=1
        else:
            num_1 += 1
            i+=1

        if num_2 > n:
            num_2 -= 1
            j+=1
        else:
            num_2 += 1
            j+=1
    if num_1 == n:
        print(i)
    else:
        print(j)
else:
    num_1 = 0
    i = 0
    while num_1 > n:
        num_1 //= 2
        i += 1
    while num_1 ==n:
        if num_1 > n:
            num_1 -= 1
            i+=1
        else:
            num_1 += 1
            i+=1
    print(i)

