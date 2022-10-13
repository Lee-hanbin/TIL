# BOJ_11053_silver2-가장긴증가하는부분수열


n = int(input())
lst = list(map(int,input().split()))
dp = [0] * n
for i in range(n):
    dp[i] = 1
    for j in range(0,i):
        if lst[j] < lst[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j]+1
print(max(dp))
print(dp)
