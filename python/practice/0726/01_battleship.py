import random  # 랜덤 모듈 활용

print("================================")
print("        Battle Ship Game        ")
print("            START !!            ")
print("================================")

# 필요에 따라 추가적으로 함수를 만들어 자유롭게 활용할 수 있습니다.
# 각자의 해역에 배를 위치시키는 함수
def set_ship(index, sea):
    for i in range(index - 1, index + 2):
        sea[i] = 1


player_sea = [0] * 15  # 플레이어의 해역
player_attacked = [False] * 15  # 플레이어의 공격 위치 기록

computer_sea = [0] * 15  # 컴퓨터의 해역
computer_attacked = [False] * 15  # 컴퓨터의 공격 위치 기록

round = 1  # 게임 라운드

# 1. 게임 준비
while True:
    # 1-1) 플레이어의 배 시작 위치 고르기
    player_index = int(input('배를 위치시킬 시작점을 고르세요. :'))

    # 1-2) 범위를 벗어난 시작점을 고른 경우
    if player_index > 15:
        print('-----해당 위치에는 배를 둘 수 없습니다.-----')
    else:
        break

# 1-3) 컴퓨터의 배 시작 위치를 랜덤으로 지정합니다.
computer_index = random.randint(1, 15)

# 1-4) 플레이어와 컴퓨터의 해역에 각각 배 위치시키기
set_ship(computer_index, computer_sea)
set_ship(player_index, player_sea)
print(computer_sea)
print(player_sea)

# 2. 라운드 진행
while True:
    # 2-1) 플레이어 공격
    print('-' * 128 + '\n' +
    '< Information Board >'+'\n' +
    f'플레이어의 해역: {player_sea}'+'\n' +
    f'플레이어의 공격 기록: {player_attacked}' +
    '\n' +'-' * 128 )
    
    # 2-2) 플레이어의 공격 위치 선택
    while True:
        player_attack_index = int(input('공격할 위치를 선택하세요. :'))                                                 # 플레이어가 공격할 위치를 입력 받는다.
        if player_attack_index > 15:                                                                                    # 플레이어가 공격할 위치가 15보다 크면 다시 입력 받는다.
            print('해역의 범위에서 벗어난 위치를 선택하셨습니다. 다시 선택해 주세요.')
            continue
        elif computer_attacked[player_attack_index - 1] == True:                                                        # 컴퓨터의 해당 해역을 이미 공격했으먄 다시 입력 받는다.
            print('이미 공격한 위치를 선택하셨습니다. 다시 선택해 주세요.')
        else:                                                                                                           
            break
    
    # 2-3) 플레이어의 공격이 성공한 경우
    if computer_sea[player_attack_index - 1] == 1:                                                                      # 컴퓨터의 배가 플레이어가 공격한 위치에 있는 경우 플레이어 승리
        print(f'<{round}라운드 결과!>' + '\n' +
        f'컴퓨터의 해역 : {computer_sea}' + '\n' +
          f'플레이어는 컴퓨터의 해역 {player_attack_index}번째 칸을 공격하였고, 컴퓨터의 배는 피격되었습니다.'+ '\n' +
          f'게임이 종료되었습니다! {round}라운드 만에 플레이어의 승리입니다!')
        break
    # 2-4) 플레이어의 공격이 실패한 경우
    else:                                                                                                               # 컴퓨터의 배가 플레이어가 공격한 위치에 없는 경우 해당 위치 True표시
        computer_attacked[player_attack_index - 1] = True
    
    # 2-5) 컴퓨터의 공격 위치 지정
    # 컴퓨터가 공격하지 않은 위치를 나타내는 리스트
    computer_attack_range = []                                                                                          # 컴퓨터가 공격 가능한 위치 리스트 정의
    for i in range(len(player_attacked)):                                                                               # False인 경우에 해당하는 번호만 할당
        if player_attacked[i] == False:                                                                                 
            computer_attack_range.append(i)
    computer_attack_index = random.choice(computer_attack_range)                                                        # 공격 가능한 위치 리스트 중에 random으로 할당

    # 2-6) 컴퓨터의 공격이 성공한 경우
    if player_sea[computer_attack_index] == 1:                                                                        # 컴퓨터가 random으로 할당 받은 위치에 플레이어의 배가 있는 경우
        print(f'<{round}라운드 결과!>' + '\n' +
         f'플레이어는 컴퓨터의 해역 {player_attack_index}번째 칸을 공격하였으나, 공격에 실패하였습니다!' + '\n' +
        f'컴퓨터는 플에이어의 해역 {computer_attack_index + 1}번쨰 칸을 공격하였고, 플레이어의 배는 피격되었습니다.' + '\n' +
        f'게임이 종료되었습니다! {round}라운드 만에 컴퓨터의 승리입니다!')
        break
    # 2-7) 컴퓨터의 공격이 실패한 경우
    else:                                                                                                               # 컴퓨터가 random으로 할당 받은 위치에 플레이어의 배가 없는 경우
        player_attacked[computer_attack_index] = True                                                                   # 플레이어의 공격 위치를 체크
        print(f'<{round}라운드 결과!>' + '\n' +
        f'플레이어는 컴퓨터의 해역 {player_attack_index}번째 칸을 공격하였으나, 공격에 실패하였습니다!' + '\n' +
        f'컴퓨터는 플레이어의 해역 {computer_attack_index + 1}번째 칸을 공격하였으나, 공격에 실패하였습니다!')
    round += 1                                                                                                          # 다음 라운드