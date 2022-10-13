# BOJ_1149_silver1-RGB거리

n = int(input())
dp = [list(map(int,input().split())) for _ in range(n)]
ans=[[0]*3 for _ in range(n+1)]
for i in range(1,n+1):
    ans[i][0] = min(ans[i-1][1],ans[i-1][2])+dp[i-1][0]
    ans[i][1] = min(ans[i-1][0],ans[i-1][2])+dp[i-1][1]
    ans[i][2] = min(ans[i-1][0],ans[i-1][1])+dp[i-1][2]
print(min(ans[n][0],ans[n][1],ans[n][2]))