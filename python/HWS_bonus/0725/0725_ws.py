# #1

# def get_dict_avg(dict_a):
#     sum1 = 0
#     cnt = 0
#     for i in dict_a.values():
#         sum += i
#         cnt += 1
#     return sum / cnt

# print(get_dict_avg({
#     'python' : 80,
#     'web' : 83,
#     'algorithm' : 90,
#     'django' : 89,
# }))


# #2

# def count_blood(lst):
#     dict_a = {}
#     cnt_a, cnt_b, cnt_o, cnt_ab = 0, 0, 0, 0
#     for i in range(len(lst)):
#         if lst[i] == 'A':
#             cnt_a += 1
#         elif lst[i] == 'B':
#             cnt_b += 1
#         elif lst[i] == 'O':
#             cnt_o += 1
#         elif lst[i] == 'AB':
#             cnt_ab += 1
#     dict_a['A'] = cnt_a
#     dict_a['B'] = cnt_b
#     dict_a['O'] = cnt_o
#     dict_a['AB'] = cnt_ab

#     return dict_a

# print(count_blood([
#         'A', 'B', 'A', 'O', 'AB', 'AB',
#         'O', 'A', 'B', 'O', 'B', 'AB',
# ]))