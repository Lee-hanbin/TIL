# BOJ 1181 silver5 단어정렬

dict1 = {}
for _ in range(int(input())):
    s = input()
    if len(s) not in dict1.keys():
        dict1[len(s)] = {s}
    else:
        dict1[len(s)].add(s)
dict2 = sorted(dict1.keys())
print(dict2)
for i in dict2:
    lst = sorted(list(dict1[i]))
    for j in lst:
        print(j)
