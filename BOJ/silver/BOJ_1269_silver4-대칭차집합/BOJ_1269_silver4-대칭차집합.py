# BOJ_1269_silver4-대칭차집합


n, m = map(int,input().split())

s1 = set(list(map(int, input().split())))
s2 = set(list(map(int,input().split())))
cnt = len(s1&s2)
print(len(s1)+ len(s2) - 2*cnt)