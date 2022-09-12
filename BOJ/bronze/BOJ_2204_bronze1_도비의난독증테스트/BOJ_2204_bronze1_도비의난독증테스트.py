#BOJ_2204_bronze1_도비의난독증테스트

while 1:
    N = int(input())
    if N == 0:
        break
    lst1 = []
    for _ in range(N):
        lst1.append(input())
    lst2 = lst1[::]
    for i, e in enumerate(lst2):
        lst2[i] = e.lower()
    lst3 = lst2[::]
    lst2.sort()
    sol = lst2[0]
    k = lst3.index(sol)
    print(lst1[k])
