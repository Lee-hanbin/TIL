# SWEA_ 14075 d3 노드의 합

for t in range(int(input())):
    N, M, L = map(int, input().split())
    ch1 = [0]*(N*2)
    ch2 = [0]*(N*2)
    value = [0]*(N*2)

    #트리 생성
    for i in range(1, N//2+1):
        p = i
        ch1[i] = i*2
        ch2[i] = i*2 + 1
    for i in range(M):
        k, v = map(int, input().split())
        value[k] = v
    while value[1] == 0:
        for i in range(1, N//2+1):
            value[i] = value[ch1[i]] + value[ch2[i]]
    print(f'#{t+1} {value[L]}')