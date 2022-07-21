# #1

# num = int(input())

# lst = list(range(1,num+1))
# for i in lst:
#     if num % i == 0:
#         print(i,end = ' ')

# #2

# def list_sum(lst):
#     sum_a = 0
#     for i in lst:
#         sum_a += i
#     return sum_a 

# sol = list_sum([1, 2, 3, 4, 5])
# print(sol)

# #3

# def dict_list_sum(lst):
#     sum = 0
#     for i in lst:
#         for j,s in i.items():                                 # sum += i['age']
#             if j == 'age':
#                 sum += s
#     return sum
# sum = dict_list_sum([{'name':'kim', 'age':12},{'name':'lee','age':4}])
# print(sum)

# #4

# def all_list_sum(lst):
#     sum = 0
#     for i in lst:
#         for j in i:
#             sum += j
#     return sum

# print(all_list_sum([[1],[2,3],[4,5,6],[7,8,9,10]]))

# #5

# print(chr(83))

# def get_secret_word(lst):
#     lst_new = []
#     for i in lst:
#         lst_new.append(chr(i))
#     return lst_new

# lst = get_secret_word([83, 115, 65, 102, 89])
# for i in lst:
#     print(i ,end= '')

# #6

# def get_secret_number(string):
#     sum = 0
#     for i in string:
#         sum += ord(i)
#     return sum

# sol = get_secret_number('happy')
# print(sol)

# #7

# def get_strong_word(str_1,str_2):
#     sum_1, sum_2 = 0, 0
#     for i in str_1:                           
#         sum_1 += ord(i)
#     for i in str_2:
#         sum_2 += ord(i)
#     if sum_1 > sum_2:
#         return str_1
#     elif sum_1 == sum_2:
#         return str_1, str_2
#     else:
#         return str_2

# lst = get_strong_word('delilah','dixon')
# print(lst)
