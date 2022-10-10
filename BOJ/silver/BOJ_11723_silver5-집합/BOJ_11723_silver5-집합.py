# BOJ_11723_silver5-집합

from copy import copy

S_tmp = list(range(1,21))
S_tmp = set(S_tmp)
n = int(input())
S = set()
for _ in range(n):
    command = input().split()
    if len(command) == 1:
        if command[0] == 'all':
            S = copy(S_tmp)
        else:
            S = set()
    else:
        com = command[0]
        num = int(command[1])
        if com == 'add':
            S.add(num)
        elif com == 'remove':
            S.discard(num)
        elif com == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif com == 'toggle':
            if num in S:
                S.remove(num)
            else:
                S.add(num)
