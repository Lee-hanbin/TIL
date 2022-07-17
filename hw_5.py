for i in list(range(0,int(input()))):
    sol = ''
    print(f'#{i+1}')
    for j in range(0,int(input())):
        alp ,num = input().split()
        num = int(num)
        sol += alp*num
    for k in range(0, len(sol),10):
        print(sol[k:k+10])