# BOJ_25501_bronze2-재귀의귀재

def rec(s, l, r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    else:
        if s[l] != s[r]:
            return 0
        else:
            return rec(s,l+1,r-1)

def is_palindrome(s):
    return rec(s,0,len(s)-1)

for i in range(int(input())):
    S = input().rstrip()
    cnt = 0
    print(is_palindrome(S), cnt)
