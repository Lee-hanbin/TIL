# BOJ_10809_bronze5-알파벳찾기
dict1 = {}
for i in range(26):
    dict1[i+97] = -1
s = input()
cnt = 0
set1 = set()
for i in s:
    ck = len(set1)
    set1.add(i)
    if ck < len(set1):
        dict1[ord(i)] = cnt
    cnt += 1
for i in dict1.values():
    print(i,end=' ')