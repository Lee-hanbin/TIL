#BOJ_2920_bronze2-음계

# c d e f g a b C
# 1 2 3 4 5 6 7 8
# ascending , descending, mixed

lst = list(map(int, input().split()))
lst2 = sorted(lst)
lst3 = sorted(lst, reverse=True)
if lst == lst2:
    print('ascending')
elif lst == lst3:
    print('descending')
else:
    print('mixed')


