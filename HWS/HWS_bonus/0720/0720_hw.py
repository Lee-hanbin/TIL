# #1 

#sum : 해당 parameter들을 모두 더함
#print : 출력함수
#len : 해당 자료형의 개수를 알려주는 함수
#split : space에 따라 구분해주는 함수
#strip : enter에 따라 구분해주는 함수

# #2

# lst = []    # list 생성
# [lst.append(i) for i in range(50) if i%2 == 1]  # 삼항연산자를 이용하여 생성한 list에 홀수만 대입
# print(lst)

# #3 

# n = 5   # 가로의 길이
# m = 9   # 세로의 길이
# for i in range(m):  # 가로
#     print(n*'*')    # 세로 출력

# #4

# temp = 37.5 #변수입력                                      
# print('입실 불가') if temp >= 36.5 else print('입실가능')   #삼항연산자를 통해 조건문

# #5

# def get_middle_char(str):     
#     if len(str) % 2 == 1:   #string의 길이가 홀수일떄
#         print(str[int(len(str)/2)])     #문자열의 가운대 문자 출력
#     else:                   #string의 길이가 짝수일때
#         print(str[int(len(str)/2 -1)] + str[int(len(str)/2)])   #문자열의 가운대 두 개의 문자 출력


# get_middle_char('ssafy')
# get_middle_char('coding')

