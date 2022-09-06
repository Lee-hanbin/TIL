#BOJ 1110 브론즈1 A+B 8

import sys
input = sys.stdin.readline

str1 = input().strip()
if int(str1) < 10:
    str1 = '0' + str1
lst = [str1[0], str1[1]]
cnt = 0
while 1:
    cnt += 1
    temp = str(int(lst[0]) + int(lst[1]))
    str2 = lst[1] + temp[::-1][0]
    if str2 == str1:
        print(cnt)
        break
    lst[0] = str2[0]
    lst[1] = str2[1]
