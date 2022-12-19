#과제 6_2
i, final_percentage, final_mass, final_salt = 0, 0, 0, 0
string = ''
lst = []
percentage =[]
mass = []
salt = []

while string != 'Done' and i < 5:
    lst = list(map(str,input(f'{i+1}.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오:').split()))
    percentage.append(int(lst[0].strip('%')))
    mass.append(int(lst[1].strip('g')))
    salt.append(int(lst[1].strip('g')) / 100 * int(lst[0].strip('%')))
    string = input('혼합된 소금물의 농도(%)와 소금물의 양(g)을 구하시겠습니까?(Done)')
    i += 1

for i in range(len(percentage)):
    final_mass += mass[i]
    final_salt += salt[i]

final_percentage = final_salt * 100 / final_mass
print(f'{round(final_percentage,2)}% {round(final_mass,2)}g')