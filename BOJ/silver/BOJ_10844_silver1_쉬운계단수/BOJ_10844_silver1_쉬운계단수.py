# BOJ_10844_silver1_쉬운계단수

from collections import defaultdict
from copy import deepcopy
N = int(input())

operator = defaultdict()

# N = 2 인 경우를 딕셔너리에 담아준다.
for i in range(0, 10):
    if i == 9 or i == 0:
        operator[i] = 1
    else:
        operator[i] = 2

sol = 0
idx_2 = [1, 2]                      # 0이 나오는 경우는 따로 정해줘야 하는데
                                    # 숫자 2와 규칙이 연관되어 있다.
if N == 1:                          # N = 1인 경우
    sol = 9
elif N == 2:                        # N = 2인 경우
    for i in operator.values():
        sol += i
    sol -= 1                        # 맨 앞이 0인 경우는 빼준다.
else:                               # N >= 3인 경우,
    j = 2
    while j < N:                                # N자리까지 반복
        operator_tmp = deepcopy(operator)       # 딕셔너리를 수정해주기 위해 딥카피 사용
        for i in range(1, 10):                  # 모든 자리 숫자의 1 ~ 0 이 나왔을 때 경우의 수를 갱신
            tmp = 0
            if i < 9:                           # i 가 9보다 작은 경우는 2개씩 올 수 있다.
                tmp = operator_tmp[i-1] + operator_tmp[i+1]
            else:                               # i가 9인 경우는 8밖에 올 수 없다.
                tmp += operator_tmp[i-1]
            operator[i] = tmp                   # i라는 숫자가 나오면 뒤에 몇 개의 경우의 수가 있는지 갱신
        idx_2.append(operator[2])               # 위에서 정의 했던 2와 연관된 0의 경우의 수를 위해 2를 계속 추가
        j += 1                                  # j 갱신
        # 숫자 0이 오는 경우, 뒤에 나올 수 있는 경우의 수 갱신
        if j % 2 == 1:                          # 홀수 자리수일 경우
            operator[0] = 1                     # 기본 1010101과 같은 숫자 한개와
            for i in range(0,j-2,2):            # 자리수가 홀수인 2의 경우의 수들의 합이 0의 경우의 수
                operator[0] += idx_2[i]
        else:                                   # 짝수도 마찬가지로
            operator[0] = 1                     # 기본 10101010과 같은 숫자 한개와
            for i in range(1,j-2,2):            # 자리수가 짝수인 2의 경우의 수들의 합이 0의 경우의 수
                operator[0] += idx_2[i]

    for i in range(1,10):                       # 원하는 자리수까지 반복하면 경우의 수를 모두 더해준다.
       sol += operator[i]
print(sol%1000000000)
