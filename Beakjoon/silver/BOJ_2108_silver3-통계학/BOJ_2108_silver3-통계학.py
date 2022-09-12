# BOJ_2108_silver3-통계학

import sys
input = sys.stdin.readline

N = int(input())

sol_avg, sol = 0 , []
for _ in range(N):
    M = int(input())
    sol_avg += M
    sol.append(M)

sol.sort()
#1 산술평균
print(round(sol_avg/N))

#2 중앙값
print(sol[N//2])

#3 최빈값
dict1 = {}
for i in sol:
    if i not in dict1.keys():   # 해당 값이 처음이면 생성
        dict1[i] = 1
    else:                       # 아니면 갱신
        dict1[i] += 1
cf_max = max(dict1.values())    # values값에서 최빈값 뽑기
cnt = 0
cf_lst = []
for k, i in dict1.items():      # 최빈값의 개수와 그 key를 list로 생성
    if i == cf_max:
        cnt+=1
        cf_lst.append(k)
if cnt == 1:                    # 최빈값이 하나면 출력
    print(cf_lst[0])
else:                           # 최빈값이 여러개면 정렬후, 2번째 값 출력
    cf_lst.sort()
    print(cf_lst[1])

#4 범위
print(max(sol)- min(sol))