# #1 

# num = int(input())    #숫자를 입력받음
# for i in range(num):  #하나씩 출력
#     print(i+1)

# #2 (구글링)

# num = int(input())  #숫자를 입력받음

# for i in range(num):    #end라는 연산자를 통해 print함수의 \n을 ' '로 대신함
#     print(i+1,end=' ')

# #3

# num = int(input())  #숫자를 입력받음
# lst = []    #list 생성
# for i in range(num):    #입력받은 숫자만큼 반복
#     lst.append(i)   #입력받은 숫자들을 list에 삽입
# for i in lst[::-1]: #list를 거꾸로 출력
#     print(i)

# #4 

# num = int(input())  #숫자를 입력받음
# for i in list(range(num+1))[::-1]:  #입력받은 숫자의 크기보다 1큰 list생성 후, 역으로 출력
#     print(i, end=' ')   #end 연산자를 통해 \n을 space로 바꿈


# #5

# num = int(input())  #숫자를 입력받음
# lst = list(range(num))  #0부터 입력받은 숫자의 개수만큼의 정수로 list생성
# sum = 0
# for i in lst:   
#     sum += i+1
# print(sum)

# #6

# num = int(input())    #숫자를 입력받음
# [print(' '*(num-(i+1))+'*'*(i+1)) for i in range(num)]  

# #7

# numbers = [
# 85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
# 51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
# 52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24,
# ]
# numbers = sorted(numbers)   #오름차순 정렬 c.f) sorted(numbers,reverse = True)
# print(numbers[int(len(numbers)/2)]) #중간값 출력
