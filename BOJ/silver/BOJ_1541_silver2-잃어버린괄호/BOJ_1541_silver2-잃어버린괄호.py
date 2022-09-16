#BOJ_1541_silver2-잃어버린괄호


lst = list(input())
lst_num = []
lst_ar = []

num = str()
for i, e in enumerate(lst):             # 숫자와 연산자를 각각 리스트로 받는다.
    if e.isdigit():                     # 숫자의 경우 연산자가 나오기 전까지가 한 숫자
        num += e
    else:                               # 연산자가 나오면
        lst_ar.append(e)                # 연산자를 리스트에 넣고
        lst_num.append(int(num))        # 숫자도 리스트에 넣는다
        num = str()                     # 숫자로 받을 문자열을 초기화한다.
        continue
    if i == len(lst)-1:                 # 마지막은 무조건 숫자이므로 따로 리스트에 넣는다.
        lst_num.append(int(num))

lst_num = lst_num[::-1]                 # pop을 이용하기 위해 슬라이싱한다.
lst_ar = lst_ar[::-1]

num = lst_num.pop()                     # 첫 값을 먼저 팝한다.
while len(lst_num) > 0:                 # 숫자를 담은 스택이 남아있을 때까지 반복
    tmp = 0                                         # - 연산자가 나오면 - ( tmp ) 로 + 연산자가 나오면 모두 더한다.
    if len(lst_ar) > 0 and lst_ar.pop() == '-':     # 연산자를 담은 스택이 남아있고 그 연산자가 - 일때
        if len(lst_ar) > 0 and lst_ar[-1] == '+':           # 연산자 스택의 top이 +이면
            while len(lst_ar) > 0 and lst_ar[-1] == '+':    # 연산자 스택의 top이 + 일때까지 반복해라
                lst_ar.pop()                                # 스택에서 + 연산자를 꺼내고
                if tmp == 0:                                # 처음 연산되는 + 이면
                    tmp = lst_num.pop() + lst_num.pop()     # 숫자 스택에서 2개의 숫자를 뽑아서 더하고
                else:                                       # 두번째 이후에 연산되는 +이면
                    tmp += lst_num.pop()                    # 숫자 스택에서 1개의 숫자를 뽑아서 더해라
            num -= tmp                                      # 연산이 다 되면 그 합을 빼준다.
        else:
            num -= lst_num.pop()                            # + 연산자가 안나오면 그냥 빼라
    else:                                              # 연산자 스택에 연산자를 pop했을때, +이면
        num += lst_num.pop()                           # 그냥 더해라
        while len(lst_ar) > 0 and lst_ar[-1] == '+':   # 만약 연산자 스택의 top에 + 연산자가 있으면
            lst_ar.pop()                               # 연산자를 pop하고
            num += lst_num.pop()                       # 숫자를 하나 pop해서 더해라
print(num)