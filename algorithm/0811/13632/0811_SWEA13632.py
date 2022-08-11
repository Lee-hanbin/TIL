#SWEA13632-이진탐색

def binay_func(total , target):
    first = 1
    cnt = 0
    while True:
        cnt += 1
        middle = (first + total) // 2
        if middle == target:
            break
        elif middle > target:
            total = middle
        else:
            first = middle
    return cnt

N = int(input())
for test_case in range(N):
    print(f'#{test_case+1}', end=' ')
    total, a, b = map(int, input().split())
    cnt_a, cnt_b = 0, 0

    cnt_a = binay_func(total, a)
    cnt_b = binay_func(total, b)

    if cnt_a > cnt_b:
        print('B')
    elif cnt_a == cnt_b:
        print(0)
    else:
        print('A')






