#BOJ_1316_silver5-그룹단어체커

sol = 0
for _ in range(int(input())):
    index_set = set()
    s = input().strip()
    # 인덱스 셋
    for i in s:
        index_set.add(i)
    # 문자열의 연속성 구하기
    for i in index_set:
        switch = 0
        cnt = 0
        lst = []
        for j in s:                 # 문자열 하나씩 대조
            cnt += 1                # 문자열의 인덱스
            if i == j:              # 인덱스와 문자가 같으면 해당 인덱스를 list에 담기
                lst.append(cnt)
        for k, e in enumerate(lst): # list를 하나씩 읽어보면서 연속성 따지기
            if k == 0:              # 첫 값은 바로 값을 넣어주고
                tmp = int(e)
                continue
            if int(e) - tmp == 1:   # 연속적이면 값을 넣어주고 계속
                tmp = int(e)
                continue
            else:                   # 연속적이지 않으면 swich ON
                switch = 1
                break
        if switch == 1:
            break
    else:
        sol += 1
print(sol)