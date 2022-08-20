import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline

cnt_book, cnt_stack = map(int, input().split())


# 어떤 더미든 내림차순이 아니면 No
for t in range(cnt_stack):
    N = int(input())
    lst = list(map(int, input().split()))
    lst_sort = sorted(lst, reverse=True)
    if lst != lst_sort:
        print('No')
        break
else:
    print('Yes')
