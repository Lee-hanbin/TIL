# BOJ-1978_silver5-소수찾기

N = int(input())
lst2 = list(map(int, input().split()))


start, end = min(lst2), max(lst2)
lst = [0] * (end+1)

for i in range(2, int(end**0.5)+1):               # 2부터 끝까지
    if lst[i] == 0:                     # 숫자가 초기화 되어 있을때
        for j in range(i*i, end+1, i):  # 배수가 되려면 적오도 2배가 필요
            lst[j] = 1                  # 소수가 아닌 숫자 1 넣기
cnt = 0
for i in lst2:                          # 찾으려는 값이 소수이면 카운팅
    if i != 1 and lst[i] == 0:
        cnt += 1
print(cnt)
