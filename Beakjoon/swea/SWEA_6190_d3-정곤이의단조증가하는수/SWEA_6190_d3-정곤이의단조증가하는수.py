# swea 6190번 정곤이의 단조 증가하는 수

for t in range(int(input())):
    sol = [-1]                              #  sol에 아무것도 못 담으면 -1 출력
    N = int(input())
    lst = list(map(int, input().split()))
    for i in range(N):
        tmp = 0
        tmp2 = 0
        for j in range(i+1, N):
            tmp = str(lst[i] * lst[j])      # Ai * Aj
            for k, e in enumerate(tmp):     # Ai * Aj의 값이 단조증가인지 확인
                if k == 0:                  # 첫 값은 넣어주고
                    tmp2 = e
                    continue
                if tmp2 > e:                # 두번째 값부터 단조증가가 아니면 break
                    break
                else:                       # 맞으면 계속 확인
                    tmp2 = e
            else:                           # 모두 다 돌면 저장
                sol.append(int(tmp))
    sol.sort()                              # 정렬
    print(f'#{t+1} {sol[-1]}')              # 제일 뒤에 값 출력