#BOJ_2577_bronze2-숫자의개수

import sys

dict1 = {}
for i in range(10):
    dict1[i] = 0
sol = 1
for i in range(3):
    sol *= int(input())
for i in str(sol):
    dict1[int(i)] += 1
for i in dict1.values():
    print(i)