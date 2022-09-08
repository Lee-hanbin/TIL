#BOJ_2309_bronze1-일곱난쟁이

import random
import sys
input = sys.stdin.readline

# 9개 수가 주어졌을 때 7개로 100 만들기
lst = []
for _ in range(9):
    lst.append(int(input()))
sum1 = 0
while sum1 != 100:
    sum1 = 0
    lst2 = lst[::]
    random.shuffle(lst2)
    for i in range(7):
        if sum1 > 100:
            break
        else:
            sum1 += lst2[i]
for i in sorted(lst2[:7]):
    print(i)