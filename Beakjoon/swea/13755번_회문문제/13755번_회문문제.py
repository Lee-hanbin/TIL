#SWEA 13755번 회문문제

import sys
sys.stdin = open('sample_input(1).txt')

#회문이 있는 문자열과 회문이 시작하는 인덱스를 도출하는 함수
def decalcomanie_search(lst, N, M):
    for s in lst:   #문자열 한 줄씩 읽음
        for i in range(N-M+1):  #전체문자열 크기에서 회문의 크기를 뺀 만큼만 회문
            for j in range(M//2):   #회문이므로 절반만 확인
                # 회문이 아니면 빠져나옴. 단, 회문의 크기가 홀수인 경우 중앙값 제외
                if s[i+j] != s[M+i-j-1] and (M // 2 + 1) != j:
                    break
            else:
                return s, i #회문을 발견하면 해당 문자열과 첫번째 문자가 있는 인덱스 리턴
    return 0, 0

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(input()) for _ in range(N)]
    lst_tmp = []    #회문이 있는 문자열을 저장
    lst_sol = []    #회문을 저장
    lst2 = []   #90도 돌린 리스트 저장
    lst_tmp, first = decalcomanie_search(lst, N, M)

    #가로 리스트에서 회문을 찾지 못한 경우
    if lst_tmp == 0:
        for i in zip(*lst): #세로 리스트를 생성
            lst2.append(list(i))
        lst_tmp, first = decalcomanie_search(lst2, N, M)

    #회문이 있는 문자열에서 회문에 해당하는 리스트 뽑아내기
    for i in range(M):
        lst_sol.append(lst_tmp[first+i])

    #리스트를 문자열로
    sol = ''.join(lst_sol)
    print(f'#{test_case} {sol}')

