def fe(N):
    sol = 1
    for i in range(1,N+1):
        sol *= i
    return sol

n, r = map(int, input().split())

print(fe(n)//(fe(n-r)*fe(r)))