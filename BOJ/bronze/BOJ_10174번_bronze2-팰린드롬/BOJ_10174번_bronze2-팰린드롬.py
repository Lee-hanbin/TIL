# baekjoon 10174 팰린드롬
def chk_pal(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            print('No')
            return
    print('Yes')

num = int(input())
lst = [list(input().lower()) for _ in range(num)]
for i in lst:
    chk_pal(i)

