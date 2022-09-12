#BOJ_6996_bronze1_애너그램

for _ in range(int(input())):
    N, M = input().split()
    s1 = sorted(N)
    s2 = sorted(M)
    if s1 == s2:
        print(f'{N} & {M} are anagrams.')
    else:
        print(f'{N} & {M} are NOT anagrams.')
