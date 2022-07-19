# #실습 1_1

# print("c:\\python_project\\test")


# #실습 1_2

# cnt_1 = int(input('게시글의 총 갯수를 입력하세요:'))
# cnt_2 = int(input('한 페이지에 필요한 게시글 수를 입력하세요:'))
# print(int(cnt_1/cnt_2))


# #실습 1_3

# s1 = input()
# s2 = input()
# print(f'{s1[0:6]}*******')
# print(f'{s2[0:6]}*******')


# #실습 1_4

# s = set()
# sum = 0
# for i in range(1,1000):
#     if i%2 == 0 or i%7 == 0:
#         s.add(i)
# for i in s:
#     sum += i
# print(sum)

# #실습 1_5

# m = int(input('가로의 길이 : '))
# n = int(input('세로의 길이 : '))
# for i in range(n):
#     print(m*'*')


# #과제 1_4

# s = input('숫자를 입력해주세요 : ')
# sum = 0
# for i in s:
#     sum += int(i)
# print(sum)

###################################################################################################################################################

#실습2_1

a = 3
b = 6
c = - 5

root_sol = (-b +-(b**2 - 4 * a * c)**(0.5))/2*a


print(root_sol)

# #과제 2_4

# orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
# orders = list(orders.split(','))

# print(f'음료주문이 총 {len(orders)}잔 들어왔습니다.')

# orders = set(orders.split(','))
# orders = list(orders)

# print(sorted(orders,reverse = True))