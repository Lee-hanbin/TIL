# swea_ 14071_D2_subtree

def preorder(N):
    global cnt
    if N:
        cnt += 1
        preorder(ch1[N])
        preorder(ch2[N])

for t in range(int(input())):
    cnt = 0
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = max(arr) + 1
    ch1 = [0]*(V+1)
    ch2 = [0]*(V+1)
    for i in range(E):
        p, c = arr[i*2], arr[i*2 + 1]
        if ch1[p] == 0:
            ch1[p] = c                  # 왼쪽 자식노드
        else:
            ch2[p] = c                  # 오른쪽 자식노드
    preorder(N)
    print(f'#{t+1} {cnt}')