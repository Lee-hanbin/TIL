# #1 

# def conut_vowels(string):
#     sum = string.count('a') + string.count('e') + string.count('i') + string.count('o') + string.count('u')
#     return sum

# print(conut_vowels('free'))
# print(conut_vowels('studnet'))
# print(conut_vowels('serendipity'))

# #2

# #  (1)  맞음
# #  (2)  맞음
# #  (3)  맞음
# #  (4)  특정 문자를 지정하지 않으면 오류 발생 x , 공백을 기준으로 나눠서 반환


# #3

# def only_square_area(lst_1, lst_2):
#     lst_sol = []
#     for i in lst_1:
#         for j in lst_2:
#             if i == j:
#                 lst_sol.append(i**2)
#     return lst_sol            

# print(only_square_area([32, 55, 63], [13, 32, 40, 55]))