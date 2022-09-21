# BOJ_14888_silver1-연산자끼워넣기


'''
@ 19) 연산자 끼워 넣기 (BOJ 14888)

#문제
1. N개의 수로 이루어진 수열 A1,A2,...,AN
2. 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어짐
3. 연산자는 +,-,*,//
4. 주어진 수의 순서는 그대로 유지
5. 연산자 우선순위의 법칙은 무시하고 앞에부터 연산
6. 나눗셈은 정수 나눗셈 몫만 취한다.
7. 음수를 양수로 나눌 때는 C++14의 기준을 따름
    - 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꿈
8. 이때, 연산자의 경우에 따른 식의 최대값과 최소값을 구하여라

#입력조건
첫째 줄: 수열의 크기
둘째 줄: 수열의 값
셋째 줄: 연산자 ( 덧셈, 뺄셀, 곱하기, 나눗셈 ) 각각의 개수

#출력조건
첫째 줄: 최대값
둘째 줄: 최솟값

'''

# # 순열 풀이
# import sys
# input = sys.stdin.readline
#
# # 연산 함수
# def operator(s, num1, num2):
#     if 'a' in s:
#         return num1 + num2
#     elif 's' in s:
#         return num1 - num2
#     elif 'm' in s:
#         return num1 * num2
#     elif 'd' in s:
#         if num1 <0 and num2 >0:
#             num1 = -num1
#             return -(num1//num2)
#         return num1 // num2
#
# # 순열 함수
# def pmt(lst_operator, result):
#     if len(result) == len(lst_operator):
#         lst_operator_pmt.append(result[:])  # 위와 같으나 shallow copy 고려해서 deep copy로 해줘야함.
#         return
#     for i in lst_operator:
#         if i not in result:
#             result.append(i)
#             pmt(lst_operator, result)
#             result.pop()
#
# N = int(input())
# lst = list(map(int,input().split()))
# a, s, m, d = map(int, input().split())
# M = a + s + m + d
# lst_operator = []
# lst_operator_pmt = []
# lst_sol = []
# # 중복순열 대신 각 부호에 번호를 매겨서 순열로 활용
# for i in range(a):
#     lst_operator.append('a'+str(i))
# for i in range(s):
#     lst_operator.append('s'+str(i))
# for i in range(m):
#     lst_operator.append('m'+str(i))
# for i in range(d):
#     lst_operator.append('d'+str(i))
#
# # 순열 리스트 생성
# pmt(lst_operator, [])
#
# # 연산 반복문
# for i in lst_operator_pmt:
#     cnt = 0
#     tmp = lst[0]                            # 첫 값 넣어주고
#     for j in i:                             # 경우의 수 중에 하나인 연산자 리스트 i
#         tmp = operator(j, tmp, lst[cnt+1])  # tmp는 순서대로 연산
#         cnt +=1                             # 다음 숫자
#     lst_sol.append(tmp)                     # 결과를 리스트에 담기
#
# print(max(lst_sol))     # 최대값
# print(min(lst_sol))     # 최소값

# #dfs 풀이
#
# N = int(input())
# lst = list(map(int,input().split()))
# a, s, m, d = map(int, input().split())
#
# max_value = -1e9
# min_value = 1e9
#
# def dfs(i, now):
#     global min_value, max_value, a, s, m, d
#     if i == N:
#         min_value = min(min_value, now)
#         max_value = max(max_value, now)
#     else:
#         if a > 0:
#             a -= 1
#             dfs(i+1, now+lst[i])
#             a += 1
#         if s > 0:
#             s -= 1
#             dfs(i+1, now-lst[i])
#             s += 1
#         if m > 0:
#             m -= 1
#             dfs(i+1, now*lst[i])
#             m += 1
#         if d > 0:
#             d -= 1
#             dfs(i+1, int(now/lst[i]))
#             d += 1
#
# dfs(1, lst[0])
#
# print(max_value)
# print(min_value)

'''
#리뷰
처음 생각난 풀이는 순열이었고... dfs로 어떻게 풀어야 할지 감도 잡히지 않았다.
순열도 중복순열을 생각하였으나, 구현할 자신이 없어서 연산자에 숫자를 붙여서 순열로 풀었다.
분명 dfs, bfs 파트인데 제대로 사용해서 풀지를 못하니.. 연습이 많이 필요할 것 같다.
'''
