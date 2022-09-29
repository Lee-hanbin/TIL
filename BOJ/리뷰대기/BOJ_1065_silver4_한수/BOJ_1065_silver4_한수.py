#BOJ_1065_silver4_한수

def f(N):
    sol = 0
    for i in range(1, N+1):                 # 한수 검증
        if i < 10:                          # 일의 자리 숫자는 counting
            sol += 1
        else:
            s = str(i)
            e_sum = int(s[1]) - int(s[0])   # 등차 구하기
            tmp = 0
            cnt = 0
            for e in s:                     # 한 자릿수씩 고려
                cnt += 1                    # index
                if cnt == 1:                # 첫 인덱스일때 값 지정
                    tmp = int(e)
                    continue
                elif int(e) - tmp != e_sum: # 두번째 자릿수부터 차이가 등차와 다르면 break
                    break
                else:                       # 같으면 다음 자릿수
                    tmp = int(e)
            else:                           # 모두 같으면 counting
                sol += 1
    return sol                              # counting 값 반환


print(f(int(input())))