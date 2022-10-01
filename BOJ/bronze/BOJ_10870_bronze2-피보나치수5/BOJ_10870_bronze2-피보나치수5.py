# BOJ_10870_bronze2-피보나치수5
def f(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return f(n-1) + f(n-2)

print(f(int(input())))