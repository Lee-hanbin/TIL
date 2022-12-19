# swea 13882 배열최소합

import sys
sys.stdin = open('sample_input(3).txt')

# 첫 행에서 가장 작은 숫자의 인덱스를 뽑고
# 두번째 행에서 될 수 있는 수 중에 작은 숫자의 인덱스를 뽑고
# 세번째 행은 fix

def f(idx, n, r, res):                                  # 0 3 3 []
    global temp, min_sum
    if idx==r:
        min_sum = temp
        return
        # cf = 0
        # for j in range(len(res)):
        #     if cf > temp:
        #         break
        #     cf += mat[j][res[j]]
        # if temp > cf:
        #     temp = cf
        # return
    for i in range(n):
        if i not in res: # if 분기가 없다면 중복
            res.append(i)               # 해당 자리 push
            temp += mat[res.index(i)][i]

            if temp > min_sum:                  # 해당 자리수가 더 커지면 다음 자리 수로 옮겨
                temp -= mat[res.index(i)][i]
                res.pop()
                continue

            f(idx + 1, n, r, res)       # 다음 자리 반환
            temp -= mat[res.index(i)][i]
            res.pop()                   # pop 하고 다음자리

for t in range(int(input())):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 9 * N + 1
    temp = 0
    f(0, N, N, [])

    print(f'#{t+1} {min_sum}')