# SWEA_14073_D2-이진탐색

def inorder(N):
    global cnt
    if N:
        inorder(ch1[N])
        cnt += 1
        value[N] = cnt
        inorder(ch2[N])

for t in range(int(input())):
    N = int(input())
    cnt = 0
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    value = [0] * (N+1)
    # 완전이진트리 만들기
    for i in range(1, N+1):
        if i * 2 <= N:                  # 인덱스 에러를 방지
            ch1[i] = i * 2
        if i * 2 + 1 <= N:
            ch2[i] = i * 2 + 1

    inorder(1)
    print(f'#{t+1}', value[1], value[N//2])
