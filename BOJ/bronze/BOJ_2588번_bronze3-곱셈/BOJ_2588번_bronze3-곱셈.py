# baekjoon 2588번 bronze 3 곱셈

N = int(input())
M = int(input())

a = M // 100
b = M // 10 - M // 100 * 10
c = M - a * 100 - b * 10
print(N *c)
print(N *b)
print(N *a)
print(N *c + N*b*10 + N*a*100)