# SWEA 13753번 문자열 비교

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    cnt, chk = 0, 0
    idx = []
    #str1의 첫번째 문자에 해당하는 인덱스 리스트
    for i in range(len(str2)):
        if str1[0] == str2[i]:
            idx.append(i)
    #마지막 idx가 될 때까지 반복
    while chk != idx[len(idx)-1]:
        chk = idx[cnt]  #idx의 값 대입
        for i in range(len(str1)):
            if chk + i == len(str2):    #문자열을 벗어나면 멈춰
                break
            if str2[chk + i] != str1[i]:    #찾는 문자열과 틀린 문자가 있으면 멈추고 다음 인덱스
                cnt += 1
                break
        else:   #전부 다 돌아가면 T를 저장하고 멈춰
            chk = 'T'
            break
    if chk == 'T':
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')


