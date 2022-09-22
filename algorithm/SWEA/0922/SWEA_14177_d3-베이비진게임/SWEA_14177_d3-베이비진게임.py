# SWEA_14177_d3-베이비진게임

# 연속 숫자
def rule1(p):
    lst = p[::]
    tmp = lst.pop()
    cnt = 1
    while lst and cnt < 3:
        if tmp + 1 == lst[-1]:
            cnt += 1
            tmp = lst.pop()
        else:
            tmp = lst.pop()
            cnt = 1
    if cnt >= 3:
        return True
    else:
        return False
# 같은 숫자
def rule2(p):
    lst = p[::]
    tmp = lst.pop()
    cnt = 1
    while lst and cnt < 3:
        if tmp == lst[-1]:
            cnt += 1
            lst.pop()
        else:
            tmp = lst.pop()
            cnt = 1
    if cnt >= 3:
        return True
    else:
        return False

import sys
sys.stdin = open('sample_input(4).txt')

T = int(input())
for t in range(1,T+1):
    lst_input = list(map(int, input().split()))[::-1]
    lst_1 = []
    lst_2 = []
    player1 = 0
    player2 = 0
    i = 0
    while i < 3:
        lst_1.append(lst_input.pop())
        lst_2.append(lst_input.pop())
        i += 1
    lst_1.sort(reverse=True)
    lst_2.sort(reverse=True)
    while i < 7:
        run_1 = rule1(lst_1)
        run_2 = rule1(lst_2)
        tr_1 = rule2(lst_1)
        tr_2 = rule2(lst_1)
        if (run_1 or tr_1) and (run_2 or tr_2):
            print(f'#{t} 0')
            break
        elif (run_1 or tr_1) and (run_2 == False and tr_2 == False):
            print(f'#{t} 1')
            break
        elif (run_1 == False and tr_1==False) and (run_2 or tr_2):
            print(f'#{t} 2')
            break
        else:
            if i == 6:
                print(f'#{t} 0')
                break
            lst_1.append(lst_input.pop())
            lst_2.append(lst_input.pop())
            i += 1
            lst_1.sort(reverse=True)
            lst_2.sort(reverse=True)
