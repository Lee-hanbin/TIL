dict_num = {
    'ABC': 3,
    'DEF': 4,
    'GHI': 5,
    'JKL': 6,
    'MNO': 7,
    'PQRS': 8,
    'TUV': 9,
    'WXYZ': 10
}
string = input()
sum = 0
for i in string:
    for j, h in dict_num.items():
        if i in j:
            sum += h

print(sum)

# chk = 0
# while chk == 0:
#     string = input('길이가 2보다 크거나 같고 15보다 작거나 같은 단어를 입력하시오.')
#     if len(string) < 2 or len(string) > 15:
#         continue
#     else:
#         chk = 1
#
# string = string.upper()
# sum = 0
# for i in string:
#     for j, h in dict_num.items():
#         if i in j:
#             sum += h
#
# print(sum)