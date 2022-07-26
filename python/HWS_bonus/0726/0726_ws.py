# #1

# def duplicated_letters(string):
#     lst = []                        # 함수를 결과를 반환할 list 생성
#     lst_chk = set()                 # 중복을 제거해줄 set 생성
#     for i in string:                # string의 항목들을 받아오는 for문
#         if string.count(i) > 1:     # 항목들의 count가 1보다 크면 set에 추가
#             lst_chk.add(i)
#     lst = list(lst_chk)             # set을 list로 전환
#     return lst                      # list 반환

# print(duplicated_letters('apple'))
# print(duplicated_letters('banana'))


# #2

# def low_and_up(string):
#     lst = []
#     cnt = 0                             # 홀수와 짝수를 읽기 위해서 필요한 cnt 변수 정의
#     for i in string:                    # string을 하나씩 할당하여 반복
#         if cnt % 2 == 0:                # 홀수 자리이면 소문자
#             lst.append(i.lower())
#         else:                           # 짝수 자리이면 대문자
#             lst.append(i.upper())
#         cnt +=1                         # counting
#     return ''.join(lst)                 # list를 문자열로 만들어줌

# print(low_and_up('apple'))
# print(low_and_up('banana'))


# #3

# def lonely(lst):
#     lst_sol = []                          # 결과를 반환할 list 정의
#     for i in range(len(lst)):             # list의 크기만큼 for문 반복
#         if i == 0 :                       # 첫 값은 list에 추가
#             lst_sol.append(lst[i])  
#         elif lst[i] != lst[i-1]:          # 해당 요소가 이전 요소와 다르면 list에 추가
#             lst_sol.append(lst[i])
#     return lst_sol

# print(lonely([1, 1, 3, 3, 0, 1, 1]))
# print(lonely([4, 4, 4, 3, 3]))