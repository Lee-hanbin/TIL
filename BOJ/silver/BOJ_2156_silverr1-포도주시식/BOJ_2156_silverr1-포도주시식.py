# BOJ_2156_silver1-포도주시식

n = int(input())
lst = [0]
for i in range(1,n+1):
    lst.append(int(input().strip()))
dp = [0 for _ in range(n+2)]


dp[1] = lst[1]
# n이 1이 아닌 경우에만 dp[2]를 구해준다.
if n != 1:
    dp[2] = lst[1] +lst[2]
    # 3가지 경우에 대해서 가장 큰 값을 dp에 넣는다
    for i in range(3, n+1):
        # dp[i] = dp[i-2] + lst[i]                        # 현재 잔이 첫 번째 잔 => 2번째 전 값 + 현재 값
        # dp[i] = max(dp[i], dp[i-3] + lst[i-1] +lst[i])  # 현재 잔이 두 번째 잔 => 연속으로 마시기 전의 값 + 연속으로 마신 값
        # dp[i] = max(dp[i],dp[i-1])                      # 현재 잔이 안마시는 잔 => 이전 잔의 값
        dp[i] = max(dp[i-2] + lst[i] , dp[i-3] + lst[i-1] +lst[i],dp[i-1])
print(dp[n])