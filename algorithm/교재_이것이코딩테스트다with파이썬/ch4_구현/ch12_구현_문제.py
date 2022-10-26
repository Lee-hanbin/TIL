#ch12 구현 문제

'''
#7 럭키 스트레이트 (BOJ 18406)
@문제
아웃복서 캐릭터는 필살기인 '럭키 스트레이트' 기술이 있다.
특정 조건에서만 사용 가능
조건 1. 현재 캐릭터의 점수(N) 자릿수 기준으로 점수를 N으로 나누어 왼쪽과 오른쪽의 각 자릿수 합이 동일하면 필살기 사용가능

@입력조건
첫째 줄: 점수 N이 주어짐 (10 ~ 99,999,999), 단, N의 자릿수는 항상 짝수

@출력조건
필살기 사용 가능 : LUCKY
필상기 사용 불가 : READY

@input
123402
@output
LUCKY
'''

# import sys
# input = sys.stdin.readline
#
# lst = list(map(int,input().strip()))    # N자리 숫자를 각 자리 리스트로 받기. 한자리씩 받으므로 strip을 통해 널값 제거
# length = len(lst)
# left, right = 0, 0
# for i in range(length//2):              # 투 포인트
#     left += lst[i]                      # 왼쪽만 더하고
#     right += lst[length-1-i]            # 오른쪽만 더하고
# if left == right:                       # 같으면 LUCKY
#     print("LUCKY")
# else:                                   # 다르면 READY
#     print("READY")

'''
@리뷰
1.문제가 간단하여 구상한 것 처럼 바로 구현 가능했다.
2.lst를 한 자씩 입력 받을 떄는 반드시 strip을 통해 '\n'을 지워줘야 함을 잊지 말자.
3.투포인트로 하나의 for문을 통해 돌린 것 보다 for문 2개로 돌린 것이 실행시간이 적게 나왔다.. 왜 그럴까?
=> 아마도 length-1-i라는 연산을 지속적으로 해줘서 그런 것 같다.
=> for문을 2개 돌리면 그래봤자 O(n) 인데, for문이 돌아갈때마다 연산이 들어가면 O(n^2)이 되지 않을까?
'''


'''
#8 문자열 재정렬 
@문제
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주짐
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤, 모든 숫자를 더한 값을 이어서 출력

@입력조건
첫째 줄: 문자열 S가 주어짐 ( 1 ~ 10000) 

@input1
K1KA5CB7

@input2
AJDLSI412K4JSJ9D

@output1
ABCKK13

@output2
ADDIJJJKKLSS20

'''

# s = list(input().strip())   # 문자열읜 sort 메서드 사용 불가


s = input().strip()
s = sorted(s)                 # 문자열은 sorted만 가능 sort 메서드는 리스트의 메서드!! => sorted로 해도 sort로 받음
sol = 0
chk = ''
for i,e in enumerate(s):
    if e.isdigit():
        sol += int(e)
    else:
        chk += e
s = chk
print(f'{s}{sol}')


'''
#9. 문자열 압축
@문제
데이터 처리 전문가가 되고 싶은 '어피치'는 문자열을 압축하는 방법에 대해 공부를 하고 있다.
최근에는 문자열에서 같은 패턴이 연속으로 나오는 것을 문자열 앞에 숫자가 나오도록 하여 문자열을 줄여서 표현하는 알고리즘으 공부
문자열의 길이를 최소로 만들도록 줄이고 그 길이를 출력
ex) aabbaccc => 2a2ba3c
    ababcdcdababcdcd => 2ab2cd2ab2cd 
                     => 2ababcdcd 

@제한사항
1.s의 길이는 1~1000
2.s는 소문자

@input                          @output
aabbacc                         7
ababcdcdababcdcd                9
abcabcdede                      8
abcabcabcabcdededededede        14
xababcdcdababcdcd               17
'''



# s = input().strip()
#
# lst = []
# for i in range(len(s)//2):                       # 문자열 한칸씩 옆으로 가는 for문
#     for j in range(2+i,len(s)-2-i):                  # 슬라이싱 할 for문 최소 2개
#         s2 = s
#         find_s = s2[i:j]
#         print(find_s)
#         s2.replace(find_s, '1')
#         print(s2)
#         lst.append(len(s2))
#
# print(min(lst))
