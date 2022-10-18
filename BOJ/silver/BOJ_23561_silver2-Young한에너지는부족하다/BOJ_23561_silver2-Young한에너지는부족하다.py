# BOJ_23561_silver2-Young한에너지는부족하다

import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(list(map(int,input().split())))
print(lst[2*n-1]-lst[n])