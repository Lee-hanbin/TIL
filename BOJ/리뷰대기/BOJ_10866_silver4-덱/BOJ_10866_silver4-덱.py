#BOJ_10866_silver4-덱

import sys
input = sys.stdin.readline

def push_back(num):
    global back, front
    back += 1
    dec.append(num)

def pop_back(switch):
    global back, front
    if is_empty():
        return -1
    back -= 1
    tmp = dec.pop()
    is_empty()
    return tmp

def is_empty():
    global back, front
    if back == front:
        front = 0
        back = 0
        return 1
    else:
        return 0

N = int(input())
dec = []
front = 0
back = 0
for i in range(N):
    command = list(input().split())
    if command[0] == 'push_back':
        push_back(int(command[1]))
    elif command[0] == 'push_front':
        dec = dec[::-1]
        push_back(int(command[1]))
        dec = dec[::-1]
    elif command[0] == 'pop_back':
        print(pop_back(1))
    elif command[0] == 'pop_front':
        dec = dec[::-1]
        print(pop_back(2))
        dec = dec[::-1]
    elif command[0] == 'front':
        if is_empty():
            print(-1)
        else:
            print(dec[0])

    elif command[0] == 'back':
        if is_empty():
            print(-1)
        else:
            print(dec[back-1])
    elif command[0] == 'empty':
        print(is_empty())
    else:#size
        print(back - front)

