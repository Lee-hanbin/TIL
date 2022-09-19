#BOJ_11866_silver5-요세푸스문제0

from collections import deque as dq

N, M = map(int, input().split())

lst = dq(range(1,N+1))
lst2 = []
while lst:
    for i in range(M-1):
        lst.rotate(-1)
    lst2.append(lst.popleft())

sol = str(lst2).replace('[', '<')
sol = sol.replace(']', '>')
print(sol)