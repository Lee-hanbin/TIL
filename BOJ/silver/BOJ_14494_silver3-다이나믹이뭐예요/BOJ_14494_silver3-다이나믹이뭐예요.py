# BOJ_14494_silver3-다이나믹이뭐예요

n, m = map(int, input().split())

d = [[0]*m for _ in range(n)]
for i in range(m):
    d[0][i] = 1
for i in range(n):
    d[i][0] = 1
for i in range(1,n):
   for j in range(1,m):
        d[i][j] = d[i-1][j] + d[i][j-1] + d[i-1][j-1]

print(d[n-1][m-1] % 1000000007)