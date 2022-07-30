'''
lotto.py의 Lotto 클래스 내에 있는 생성자와 스태틱 메서드에 대한 테스트 코드입니다.
이 파일을 실행하면 터미널에 테스트 결과가 출력됩니다.
이 파일은 별도로 수정하지 않습니다!
'''
from lotto import Lotto


lotto = Lotto()
mains, bonus = [10, 14, 16, 18, 29, 35], 25  # 예시 당첨 번호 (메인 6개 + 보너스 1개)

checks = [
    'lotto.number_lines == []',  # 생성자에서 인스턴스 변수가 빈 리스트로 초기화 되는지 테스트
    'lotto.get_draw_date(1023) == ("2022", "07", "09")',
    'lotto.get_draw_date(1024) == ("2022", "07", "16")',
    'lotto.get_draw_date(1025) == ("2022", "07", "23")',
    'lotto.get_lotto_numbers(1023) == ([10, 14, 16, 18, 29, 35], 25)',
    'lotto.get_lotto_numbers(1024) == ([9, 18, 20, 22, 38, 44], 10)',
    'lotto.get_lotto_numbers(1025) == ([8, 9, 20, 25, 29, 33], 7)',
    'lotto.get_same_info(mains, bonus, [10, 14, 16, 18, 29, 35]) == (6, False)',
    'lotto.get_same_info(mains, bonus, [10, 14, 16, 18, 25, 35]) == (5, True)',
    'lotto.get_same_info(mains, bonus, [10, 14, 16, 18, 30, 35]) == (5, False)',
    'lotto.get_same_info(mains, bonus, [10, 14, 15, 18, 25, 35]) == (4, True)',
    'lotto.get_same_info(mains, bonus, [10, 14, 15, 17, 29, 35]) == (4, False)',
    'lotto.get_same_info(mains, bonus, [10, 12, 15, 18, 25, 35]) == (3, True)',
    'lotto.get_same_info(mains, bonus, [10, 12, 15, 18, 24, 35]) == (3, False)',
    'lotto.get_same_info(mains, bonus, [10, 14, 15, 17, 25, 36]) == (2, True)',
    'lotto.get_same_info(mains, bonus, [10, 14, 15, 17, 24, 36]) == (2, False)',
    'lotto.get_same_info(mains, bonus, [10, 13, 15, 17, 25, 36]) == (1, True)',
    'lotto.get_same_info(mains, bonus, [10, 13, 15, 17, 24, 36]) == (1, False)',
    'lotto.get_same_info(mains, bonus, [9, 13, 15, 17, 25, 36]) == (0, True)',
    'lotto.get_same_info(mains, bonus, [9, 13, 15, 17, 24, 36]) == (0, False)',
    'lotto.get_ranking(6, True) == 1',
    'lotto.get_ranking(6, False) == 1',
    'lotto.get_ranking(5, True) == 2',
    'lotto.get_ranking(5, False) == 3',
    'lotto.get_ranking(4, True) == 4',
    'lotto.get_ranking(4, False) == 4',
    'lotto.get_ranking(3, True) == 5',
    'lotto.get_ranking(3, False) == 5',
    'lotto.get_ranking(2, True) == -1',
    'lotto.get_ranking(2, False) == -1',
    'lotto.get_ranking(1, True) == -1',
    'lotto.get_ranking(1, False) == -1',
    'lotto.get_ranking(0, True) == -1',
    'lotto.get_ranking(0, False) == -1',
]

counts = 0

for i, check in enumerate(checks):
    if not eval(check):
        exp, value = check.split(' == ')
        if 7 <= i <= 19:
            print(f'mains, bonus = {mains}, {bonus}')
        print(exp)
        print(f'기댓값 : {value}')
        print(f'반환값 : {eval(exp)}')
        print()
        counts += 1

if counts == 0:
    print('축하합니다! 모든 테스트를 통과하였습니다.')
else:
    print(f'{counts}개의 통과하지 못한 테스트가 있습니다.')
