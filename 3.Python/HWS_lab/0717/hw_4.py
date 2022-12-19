N = int(input())
data = []

for i in list(range(0,N)):
    s = input()
    data.append(s)

for i in list(range(0,N)):
    if data[i][::-1] == data[i]:
        print(f'#{i+1} 1')
    else:
        print(f'#{i+1} 0')
