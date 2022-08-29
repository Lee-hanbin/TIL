# swea 1225번 암호생성기
import sys
sys.stdin = open('input.txt')

# 자기 자리 값을 바꾸고
# front를 갱신해서 빼줄 값들만 고쳐주면 되는 거 아니야?
# 그럼 결과의 순서가 달라지지 않을까?
# 어떻게 해야하지

for _ in range(10):
    test_case = int(input())
    que = list(map(int, input().split()))
    front = 0
    temp = 1

    while temp != 0:
        for i in range(1, 6):
            temp = que[front] - i
            if temp <= 0:
                temp = 0
                que[front] = temp
                front += 1
                front = front % 8
                break
            else:
                que[front] = temp
                front += 1
                front = front % 8
    idx = 0
    for i in range(7):
        if que[i] == 0:
            idx = i
            break
    temp = 7 - idx
    sol_lst = [0]* 8
    for i in range(8):
        sol_lst[(i+temp) % 8] = que[i]
    print(f'#{test_case}', *sol_lst)