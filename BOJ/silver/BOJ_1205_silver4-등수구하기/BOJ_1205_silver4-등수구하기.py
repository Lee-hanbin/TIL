# BOJ_1205_silver4-등수구하기

n, score, p = map(int,input().split())
if n == 0:                          # 랭킹리스트에 아무도 없으면 1등
    print(1)
else:
    lst = sorted(list(map(int,input().split())) + [score], reverse=True)        # 태수 값 넣어서 내림차순 정렬
    lst2 = sorted(lst)              # 오름차순 정렬
    T = lst.index(score)            # 가장 먼저오는 score의 인덱스 찾기
    T2 = lst2.index((score))        # 가장 나중에 오는 score의 인덱스 찾기
    T2 = n - (T2-1)                 # 등수로 반환 ==> 동점자는 큰 등수
    T = T + 1                       # 등수로 반환 ==> 문제에서 요구하는 동점자는 작은 등수
    # print(lst, T)
    # print(lst2, T2)
    if p < T:                       # 태수의 등수가 랭킹리스트에서 벗어나면 -1
        print(-1)
    else:                           # 등수 안에 있을 때
        if T2 > p:                  # 동점자가 등수 밖에도 존재하면 -1
            print(-1)
        else:                           # 동점자가 등수 안에 있으면 태수의 등수 출력
            print(T)
