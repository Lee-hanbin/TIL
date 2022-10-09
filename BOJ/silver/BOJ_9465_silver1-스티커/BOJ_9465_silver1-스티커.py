# BOJ_9465_silver1-스티커
T = int(input())
for _ in range(T):
    n = int(input())
    lst = [[0] for _ in range(2)]
    dp = [[0]*(n+1) for _ in range(2)]
    lst_sol = [0] * (n+1)
    for i in range(2):
        lst[i] += list(map(int,input().split()))
    dp[0][1] = lst[0][1]            # 초기값 => 위에 스티커
    dp[1][1] = lst[1][1]            # 초기값 => 아래 스티커
    for i in range(2,n+1):
        lst_sol[i] = max(dp[0][i-1], dp[1][i-1])              # 현재 dp 값
        dp[0][i] = lst[0][i] + max(lst_sol[i-1], dp[1][i-1])  # 위에 스티커 => 현재 스티커 + max(이전 dp 값, 이전 아래 스티커 dp)
        dp[1][i] = lst[1][i] + max(lst_sol[i-1], dp[0][i-1])  # 아래에 스티커 => 현재 스티커 + max(이전 dp 값, 이전 위 스티커 dp)
    print(max(dp[0][n], dp[1][n]))
