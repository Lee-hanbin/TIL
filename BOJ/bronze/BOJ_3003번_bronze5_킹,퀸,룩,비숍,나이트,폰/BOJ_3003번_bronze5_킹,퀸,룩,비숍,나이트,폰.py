# BOJ 3003번 bronze5 킹, 퀸, 룩, 비숍, 나이트 폰

pre = list(map(int, input().split()))

mal = [1, 1, 2, 2, 2, 8]
sol = []

for i in range(len(pre)):
    print(mal[i] - pre[i],end=' ')
