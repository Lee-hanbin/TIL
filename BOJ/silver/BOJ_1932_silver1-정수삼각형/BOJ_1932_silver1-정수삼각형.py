# BOJ_1932_silver1-정수삼각형

n = int(input())
dp = [0] * (n+1)
for i in range(1, n+1):
    chk = [0] + list(map(int,input().split()))
    if i == 1:
        dp[i] = chk[1]
        continue
    tmp = dp[::]
    for j in range(1, i+1):
        if j == 1:
            tmp[1] = dp[1] + chk[1]
        elif j == i:
            tmp[i] = dp[j-1] + chk[i]
        else:
            tmp[j] = max(dp[j-1], dp[j])+chk[j]
    for i, e in enumerate(tmp):
        dp[i] = e
print(max(dp))


