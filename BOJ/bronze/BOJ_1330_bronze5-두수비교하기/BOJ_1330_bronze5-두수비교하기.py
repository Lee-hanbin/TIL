#BOJ 1330번 bronze5 -두수비교하기

A, B =map(int, input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')