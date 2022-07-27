########################################################################################################
#   서울4반_이한빈    #
#
# #리뷰#
# 1. 교수님이 원하는 4가지 조건을 생각해봤습니다.
#   - 함수 사용
#   - 이름만으로 같이 먹을 사람을 알기 힘드니 간단한? MBTI 정도의 추가정보
#   - 단순 출력보다는 시각적으로 보여줄 수 있는 출력물 
#   - oop 이용..?
#
# 2. 아쉬운점 및 어려웠던 점
#   - 코드가 너무 조잡해서 민망합니다.
#   - 처음에 단순하게 할 수 있을거라 생각했지만, 생각보다 구현하는데 오래걸렸습니다.
#   - 반 사람들의 정보를 적으면서 이래도 되는건가.. 싶었습니다. 
#
#########################################################################################################

# 점심 랜덤 박스
import random

students = {
'기남석' : 'mbti x & 한강 맥주 반대...ㅠ' ,
'김경림' : 'INTP & 너가 I라고? 소리 많이 들음 ',
'김규리' : 'INFJ & 일어과에서 도망..!?',
'김동수' : 'INFP & (CA 최고) 마음 맞는 사람이랑 노가리 좋아함',
'김영식' : 'ISFJ & 완전 동안 생일 축하해요',
'김영준' : 'INTJ & 첫 날부터 집에 가고 싶었음',
'김하늬' : 'INTP & 식품영양학 오늘의 점심은..?',
'류태규' : 'ENFP & 인천 자차 통학러',
'박시현' : 'INFJ & 노예 생활 싫어서 대학원 거부',
'박준하' : 'INTJ & 스윙댄스, 스페인어 회화 가능',
'서영준' : 'INFP & (모각코장 최고) 게임 BJ경험 ',
'신선호' : 'mbti 안하는 유형 ISTJ 예상',
'안예나' : 'INTP & 자기소개 도중에 카메라 난입',
'양희진' : 'INFP & 파판14 같이할 파티구함..',
'오지원' : 'ENFJ & (반장 최고) 사진촬영 좋아함',
'유정훈' : 'INTP & 철학과 멍때리기 좋아함',
'이경진' : 'ENFP & 환승없이 7정거장..부럽',
'이여민' : 'INFP & KPOP 좋아함 작사도 하심',
'이창준' : 'INFJ & 교수님이랑 이름 같아서 branch이름 빼앗김',
'이한빈' : 'ESFJ & 혼자 여행가는 거 좋아함',
'정석진' : 'INTP & 심리학과, 첫번째 자기소개  ',
'정유정' : 'INFP & 우영우 역삼역 정유정 예쁜 쓰레기 좋아함',
'정효상' : 'INFP & 마지막 자기소개 퍼즐 좋아함',
'조민주' : 'ISFP & 이란성 쌍둥이 마라톤 좋아함',
'최종현' : 'INFP & 대학한테 물류 사기 당함 '
}

# 난수 발생 함수
def random_box(dict_a):                         # 난수를 발생시켜 주어진 정보를 섞는 함수
    for k in range(5000001):                    # loading 중임을 시각적으로 보여줌
        if k % 1000000 == 0:
            print(' *** ',end = '')
        elif k == 5000000 / 2:
            print('loading', end = '')
    print()
    print()
    party = [i for i in dict_a.keys()]          # dictionary의 key들을 list에 담는다
    random.shuffle(party)                       # 해당 key들을 섞는다.
    return party                                # list를 반환한다.

# 조 생성
def lunch_box(lst, num, index):                 # 섞인 이름을 리스트로 받아와서 조원을 뽑는 함수
    lst_box = []
    for i in range(0, num):                     # 처음에 정한 조원수 만큼 반복
        lst_box.append(lst[index])              # list에 조원 추가
        index += 1                              
    return lst_box

# 결과로 도출될 박스 출력 함수
def box_print(dict_a, lst):                     # 조원의 정보와 리스트를 가지고 출력하는 함수
    cnt = 1                                     # 해당 조를 식별하기 위한 변수 정의
    for i in lst:                               
        print(f'{cnt}조')
        print('*'* 70)
        for j in i:
            print('***', ' ', j, ' : ', dict_a.get(j) )
        print('*'* 70) 
        cnt +=1

###################################################################################################
# main #

num = int(input('한 조에 몇명? '))              # 한 조당 인원을 입력받는 변수

print()
print('random box를 섞겠습니다.' + '\n')
name = random_box(students)                     # 섞인 이름의 list를 할당 받음
print( 'random box가 모두 섞였습니다. '+ '\n')
input('* 조를 선정하시려면 enter를 눌러주세요 *')

max_party = len(name) // num                    # 나올 수 있는 조의 개수
dec_cnt = max_party * num                       # 조가 정해진 사람의 수
party_box = []                                  # 정해진 조를 담는 list


j = 0
for i in range(max_party):                      # 각 조에 사람들을 배정    
    party_box.append(lunch_box(name, num, j))   
    j += num


if  len(name)-dec_cnt < 4:                      # 배정받지 못한 인원의 수가 4명 미만이면 남은 인원을 다른 조에 한명씩 배정
    k = 0
    for i in range(dec_cnt,len(name)):          
        party_box[k].append(name[i])
        k += 1
else:                                           # 남은 인원이 4명 이상이면 남은 사람들로 한 조를 배정
    lst = []
    for i in range(dec_cnt,len(name)):
        lst.append(name[i])
    party_box.append(lst)

print()
print(' '* 5 ,'ㄷㄱ'*5)
print()
input('* 조 선정이 완료되었습니다 enter 눌러주세요 *')
print()
print()

box_print(students, party_box)      # 박스 출력
