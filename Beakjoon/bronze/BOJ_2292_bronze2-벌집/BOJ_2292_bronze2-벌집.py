#BOJ_2292_bronze2-벌집

# 1 -> 7 -> 19 -> 37 -> ..
#    6   12    18    24  ...
# 계차 수열

N = int(input())
M = 1
cnt = 1

while M < N:
    M = M + 6*cnt       # 1 -> 7 -> 19 -> 37
    cnt += 1
print(cnt)