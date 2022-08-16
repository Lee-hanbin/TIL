#SWEA 13756 글자수
import sys
sys.stdin = open('sample_input(2).txt')

T = int(input())
for test_case in range(T):
    str1 = input()  # 짧은 문자열
    str2 = input()  # 긴 문자열
    dict1 = {}
    temp = 0    #가장 많은 개수입력 변수
    # 짧은 문자열을 돌면서 해당 문자를 key로 두고 value를 0으로 초기화
    for i in str1:
        dict1[i] = 0
    # 긴 문자열을 돌면서 해당 문자가 key값에 있으면 counting
    for i in str2:
        if i in str1:
            dict1[i] += 1
    #가장 많이 있는 문자 구하기
    for b in dict1.values():
        if b > temp:
            temp = b
    print(f'#{test_case+1} {temp}')
