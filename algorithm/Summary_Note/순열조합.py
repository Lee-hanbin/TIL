'''
순열 생성
'''

#1. 단순 순열 생성
# for i in range(1,4):
#     for j in range(1, 4):
#         if i != j:
#             for k in range(1,4):
#                 if k != i and k != j:
#                     print(i, j, k)


# 사전적 순서

# 최소 변경을 통한 방법

#2. 재귀 호출을 통한 순열 생성
# def f(i,k):
#     if i == k:                          # 인덱스 i == 원소의 개수
#         print(p)
#     else:
#         for j in range(i,k):
#             p[i], p[j] = p[j], p[i]     # 바꿔서 비교
#             f(i+1, k)
#             p[i], p[j] = p[j], p[i]     # 다시 원상 복구
#
# p = [i for i in range(1, 11)]
# f(0,10)

#3. 재귀 호출을 통한 순열 생성 ( 사전순서 + N개중에 R개 순서 고려해서 뽑기 )
'''
r개씩 만들어지면 출력 or append하고
자리수들을 바꿔가며 다시 출력 or append
'''
# def f2(i,k, r):
#     if i == r:                          # 자리수가 r개가 되면 멈춰
#         print(p)
#     else:
#         for j in range(k):              # 자리수를 끝까지 돌려봐
#             if not used[j]:             # a[j]가 아직 사용되지 않으면
#                 used[j] = True          # a[j] 사용됨으로 표시
#                 p[i] = a[j]             # p[i]는 a[j]로 결정
#                 f2(i+1,k,r)               # p[i+1] 값을 결정하러 이동
#                 used[j] = False         # a[j]를 다른 자리에서 쓸 수 있도록 해제
#
# N = 5                           # N개 중에
# R = 3                           # R개 뽑기
# a = [i for i in range(1, N+1)]
# used = [0] * N
# p = [0] * R
# f2(0, N, 3)


# # 순열 연습문제
# def f(i, k):
#     global minV
#     if i == k:
#         s = 0                   # 모든 l행에서 p[l]열을 골랐을 때의 합
#         for l in range(k):
#             s += arr[l][p[l]]
#         if minV > s:
#             minV = s
#     else:
#         for j in range(i,k):
#             p[i], p[j] = p[j], p[i]
#             f(i+1, k)
#             p[i], p[j] = p[j], p[i]
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     p = [ i for i in range(N)]
#     minV = N*10
#     f(0, N)
#######################################################################################################################
'''
부분집합
'''
# 1. 단순하게 모든 부분 집합 생성

# 2. 바이너리 카운팅
'''
- 원소 수에 해당하는 N개의 비트열을 이용
- n번째 비트값이 1이면 n번째 원소가 포함되었음을 의미
'''
# arr = [3, 6, 7, 1, 5, 4]
# n =len(arr)
#
# for i in range(0, (1<<n)):
# # for i in range(1, 1 << n):       # 공집합 빼고 만들기
#     for j in range(0,n):
#         if i & (1<<j):              # j번 비트가 0이 아니면 arr[j] 부분집합의 원소
#             print(arr[j], end=' ')
#     print()

# # 3. 바이너리 카운팅 (재귀함수)
#
# def f(i,k):
#     if i == k:
#         #print(bit)
#         for j in range(k):
#             if bit[j]:
#                 print(arr[j], end=' ')
#         print()
#     else:
#         bit[i] = 0
#         f(i+1,k)
#         bit[i] = 1
#         f(i+1, k)
#
# arr = [3, 6, 7, 1, 5, 4]
# n = len(arr)
#
# bit = [0] * n               # bit[i] arr[i]
# f(0, n)
#

#########################################################################################################################

'''
조합
'''
# # 1. 단순 조합 생성
# N = 10
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             print(i,j,k)

# 2 . 재귀 호출을 통한 순열 생성 ( 사전순서 + N개중에 R개 순서 고려해서 뽑기 )
def nCr(n, r, s):
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)
A = [1, 2, 3, 4, 5]
n =len(A)
r = 3
comb = [0] * r
nCr(n, r, 0)

# 3. 조합 오름차순
# def nCr(s):
#     if len(ans) == M:
#         print(*ans)
#     else:
#         for i in range(s, N+1):
#             if i not in ans:
#                 ans.append(i)
#                 nCr(i+1)
#                 ans.pop()
#
# N, M = 4, 2  # N개 중 M개
# ans = []
# nCr(1)

#########################################################################################################################

# # 배열의 합
# def f(i, k):                # k : 원소 개수 / i : 선택된 원소의 수
#     global min_v
#     if i == k:
#         s = 0               # a 행에서 p[a] 열을 골랐을 때의 합
#         for a in range(k):
#             s += arr[a][p[a]]
#         if min_v > s:
#             min_v = s
#         print(p)
#     else:
#         for j in range(i, k):
#             p[i], p[j] = p[j], p[i]
#             f(i+1, k)
#             p[i], p[j] = p[j], p[i]
#
# N = 3
# arr = [[2, 1, 2], [5, 8, 5], [7, 2, 2]]
# p = [i for i in range(N)]
# min_v = N * 10
# f(0, N)
# print(min_v)
#
# # ------------------------------------------------------------------------
#
# # 부분집합
# arr = [3, 6, 7, 1, 5]
# n = len(arr)
#
# for i in range(0, 1 << n):              # 부분집합의 개수 (1부터 시작하면 공집합 x)
#     for j in range(0, n):               # 원소 수만큼 비트 비교
#         if i & (1 << j):                # i의 j번째 비트가 1이면 j번째 원소 출력
#             print(arr[j], end=' ')
#     print()
#
# print()
#
# # 부분집합 2
# arr = [1, 2, 3, 4, 5]
# n = len(arr)
#
# res = []
# for i in range(1, 1 << n):
#     tmp = []
#     for j in range(0, n):
#         if i & (1 << j):
#             tmp.append(arr[j])
#     res.append(tmp)
# print(res)
#
# print()
#
# # 부분집합 3
# A = [-1, 3, -9, 6, 7, -6, 1, 5, 4]
# n = len(A)
#
# ans = 0
# for i in range(0, 1 << n):
#     lst = []
#     for j in range(0, n):
#         if i & (1 << j):
#             lst.append(A[j])
#     if sum(lst) == 0:
#         ans += 1
#         print(lst)
#
# # ------------------------------------------------------------------------
#
# def f(i, k):
#     if i == k:
#         print(bit)
#     else:
#         bit[i] = 0
#         f(i+1, k)
#         bit[i] = 1
#         f(i+1, k)
#
# arr = [3, 6, 7]
# n = len(arr)
# bit = [0] * n
# f(0, n)
#
# print()
# # ------------------------------------------------------------------------
#
# def f(i, k):
#     if i == k:
#         for j in range(k):
#             if bit[j]:
#                 print(arr[j], end=' ')
#         print()
#     else:
#         bit[i] = 0
#         f(i+1, k)
#         bit[i] = 1
#         f(i+1, k)
#
# arr = [3, 6, 7]
# n = len(arr)
# bit = [0] * n
# f(0, n)
#
# print()
#
# # ------------------------------------------------------------------------
#
#
# # 조합
# N = 5
# for i in range(N - 2):
#     for j in range(i + 1, N - 1):
#         for k in range(j + 1, N):
#             print(i, j, k)
#
# print()
#
#
# # ------------------------------------------------------------------------
#
# # 조합 (
# def nCr(n, r, s):
#     if r == 0:
#         print(*comb)
#     else:
#         for i in range(s, n - r + 1):
#             comb[r - 1] = A[i]
#             nCr(n, r - 1, i + 1)
#
#
# A = [x for x in range(5)]
# n = len(A)
# r = 3
# comb = [0] * r
# nCr(n, r, 0)
#
# # ----------------------------------------------------------
# # {1,2,3} 을 포함하는 모든 순열을 생성
# for i in range(1, 4):
#     for j in range(1, 4):
#         if i != j:
#             for k in range(1, 4):
#                 if k != i and k != j:
#                     print(i, j, k)
#
# print()
# # ------------------------------------------------------------------------
#
# # 재귀 호출을 통한 순열 생성
# def f(i, k):                # k : 원소 개수 / i : 선택된 원소의 수
#     if i == k:              # i == 원소 개수 => 출력
#         print(p)
#     else:
#         for j in range(i, k):
#             p[i], p[j] = p[j], p[i]
#             f(i+1, k)
#             p[i], p[j] = p[j], p[i]
#
# p = [1, 2, 3, 4]
# f(0, 4)
#
# print()
# # ---------------
#
# # 재귀 호출을 통한 순열 생성 2
# def f(x, y):
#     global res
#     if x == y:
#         res.append(p[:])
#     else:
#         for i in range(x, y):
#             p[x], p[i] = p[i], p[x]
#             f(x+1, y)
#             p[x], p[i] = p[i], p[x]
#
# p = [1, 2, 3, 4]
# res = []
# f(0, 4)
# print(res)
#
# print()
#
# # ------------------------------------------------------------------------
#
# # 재귀 호출을 통한 순열 생성 - 사전순으로 정의
# # N 개 중에 R 개를 고르는 순열
# def f(i, k, r):                     # k : 원소 개수 / i : 선택된 원소의 수 / r : 원하는 원소 개수
#     if i == r:
#         print(p)
#     else:
#         for j in range(k):
#             if used[j] == 0:        # a[j]가 아직 사용되지 않았으면
#                 used[j] = 1         # a[j] 사용 표시
#                 p[i] = a[j]         # p[i] = a[j]
#                 f(i+1, k, r)        # p[i+1] 을 결정하러 이동
#                 used[j] = 0         # a[j]를 다른 자리에서 쓸 수 있도록 해제
#
# N = 5
# R = 3
# a = [i for i in range(1, N+1)]
# used = [0] * N
# p = [0] * R
# f(0, N, R)
#
# print()
# # ------------------------------------------------------------------------