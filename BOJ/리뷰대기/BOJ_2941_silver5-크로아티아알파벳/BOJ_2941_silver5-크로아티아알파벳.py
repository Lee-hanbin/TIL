#BOJ_2941_silver-크로아티아알파벳

lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input().strip()
tmp = str()
cnt = 0
for i in lst:
    if s.find(i) != -1:
        s2 = s.replace(i,'1')
        s = s2
cnt += len(s)
print(cnt)

