# SWEA_5688_d3-세제곱근을찾아라

def binary(N, key):
    start = 1
    end = N
    while start <= end:
        if end**3 == key:
            return end
        middle = (start + end) // 2
        if middle ** 3 == key:
            return middle
        elif middle ** 3 > key:
            end = middle - 1
        else:
            start = middle + 1
    return -1

for t in range(int(input())):
    N = int(input())
    length = int(N**(0.5))
    # if N % 2 == 0 and length % 2 != 0:
    #     length += 1
    # elif N % 2 == 1 and length % 2 != 1:
    #     length += 1
    sol = binary(length, N)
    print(f'#{t+1} {sol}')

