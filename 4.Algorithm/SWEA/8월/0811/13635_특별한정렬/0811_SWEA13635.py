#SWEA13635-특별한 정렬

T = int(input())
for test_case in range(T):
    print(f'#{test_case + 1}', end=' ')

    N = int(input())    # 입력할 숫자의 개수
    lst = list(map(int, input().split()))   # 숫자 입력

    idx = 0
    for i in range(10):
        tmp = lst[i]
        if i % 2 == 0:  # 홀수번째는 최대값을 가장 앞에
            for j in range(N-i):  #정렬되지 않은 숫자만큼 순회
                if tmp < lst[j+i]:    #비교할 값이 비교된 값보다 작으면 갱신
                    tmp = lst[j+i]
                    idx = j + i
            if tmp == lst[i]:   #비교할 값이 최대값이면 그대로
                continue
            else:
                lst[i], lst[idx] = lst[idx], lst[i]
        else:           # 짝수번째는 최소값을 가장 앞에
            for j in range(N-i):  #정렬되지 않은 숫자만큼 순회
                if tmp > lst[j+i]:    #비교할 값이 비교된 값보다 크면 갱신
                    tmp = lst[j+i]
                    idx = j + i
            if tmp == lst[i]:   #비교할 값이 최소값이면 그대로
                continue
            else:
                lst[i], lst[idx] = lst[idx], lst[i]
    for k in range(10):
        print(lst[k], end=' ')
    print()