# SWEA_14174_d3-전자카트

import sys
sys.stdin = open('sample_input(1).txt')

# 순열 함수
def pmt(lst, result):
    if len(result) == len(lst):
        lst_pmt.append(result[:])
        return
    for i in lst:
        if i not in result:
            result.append(i)
            pmt(lst, result)
            result.pop()

T = int(input())
for t in range(1, T+1):
    lst_idx = []
    lst_pmt = []
    # lst_sol = []
    N = int(input())
    map_a = [list(map(int,input().split())) for _ in range(N)]
    lst_idx = list(range(1,N))
    # 순열 리스트 생성
    pmt(lst_idx, [])
    min1 = N * N * 100
    for i in lst_pmt:
        i = [0] + i + [0]                   # 처음과 끝 값을 경로를 추가
        tmp = 0
        for j in range(len(i)-1):           # 경로를 찾아서 끝까지
            tmp += map_a[i[j]][i[j+1]]
            # if min1 < tmp:
            #     break
        if min1 > tmp:
            min1 = tmp
        # lst_sol.append(tmp)                 # 경로 하나당 값을 비교
    # print(f'#{t} {min(lst_sol)}')
    print(f'#{t} {min1}')