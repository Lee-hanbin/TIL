#SWEA_14142_d2-이진수2

for t in range(int(input())):
    N = float(input())
    sol = ""
    i = 1
    while N > 0 and i < 13:
        if N // (2**(-i)):      # 몫이 존재하면
            N -= (2**(-i))      # 해당 값을 빼주고
            sol += '1'          # 이진수 체크
        else:                   # 몫이 존재하지 않으면
            sol += '0'          # 이진수 체크
        i += 1                  # 다음 자리수
    if N == 0:                  # N이 2진수 12자리수 안으로 해결되면
        print(f'#{t+1} {sol}')  # 2진수 출력
    else:
        print(f'#{t+1} overflow')   # 아니면 overflow 체크
