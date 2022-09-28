# # BOJ_15829_bronze2-hashing
# from math import log
#
# H = dict()
# for i in range(ord('a'),ord('z')+1):
#     H[chr(i)] = i-96
# L = int(input())
# s = input().strip()
# lst = [1]
# tmp = 1
# for _ in range(1,L):
#     tmp *= 31
#     lst.append(tmp)
# j = 0
# sol = 0
# for i in s:
#      sol += H[i] * lst[j]
#      j += 1
# print(sol%1234567891)   #자리수채우기

