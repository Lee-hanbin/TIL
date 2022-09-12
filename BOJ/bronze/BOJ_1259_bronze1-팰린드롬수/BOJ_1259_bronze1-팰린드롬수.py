#BOJ_1259_bronze1-팰린드롬수

while 1:
    s = input().strip()
    length = len(s)
    if s == '0':
        break
    else:
        for i in range(length//2):
            if s[i] != s[length-1-i]:
                print('no')
                break
        else:
            print('yes')
            