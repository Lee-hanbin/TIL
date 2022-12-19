#SWEA 1206 View
import sys
sys.stdin = open('input.txt')

for test_case in range(1,11):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    chk = 0
    for i in range(2, N-2):
        chk = lst[i]
        case = []
        for j in range(5):
            if j == 2:
                case.append(0)
            else:
                case.append(lst[i-2+j])
        if case[0] < chk and case[1] < chk and case[3] < chk and case[4] < chk:
            case.sort()
            cnt += (chk-case[4])

    print(f'#{test_case} {cnt}')
