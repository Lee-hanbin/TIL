# BOJ_1697_silver1-숨바꼭질
<<<<<<< HEAD
import sys
input = sys.stdin.readline
from collections import deque

def bfs(n, m):
    queue = deque()
    queue.append([n,0])             # [수빈이 위치, second]
    visited = set()
    visited.add(n)              # 방문 표시
    while queue:
        v, sec = queue.popleft()    # v: 수빈이 위치 , sec : 걸린 시간
        if v == m:                  # 수빈이가 동생에게 도착하면 끝
            return sec
        sec += 1
        if 2*v not in visited and 0 <= 2*v <= 100000:    # 2*v 에 방문한 적이 없고 max값보다 작을때
            queue.append([2*v,sec])
            visited.add(2*v)
        if v-1 not in visited and v-1 >= 0:         # v-1 에 방문한 적이 없고 0보다 클때
            queue.append([v-1,sec])
            visited.add(v-1)
        if v+1 not in visited and 0<= v+1 <= m:    # v+1 에 방문한 적이 없고 max값보다 작을때
            queue.append([v+1,sec])
            visited.add(v+1)


n, m = map(int, input().split())


print(bfs(n,m))
=======

n, m = map(int, input().split())

if n > m:
    n, m = m, n
if m % 2 == 1:
    num_1 = m -1
    i = 1
    num_2 = m +1
    j = 1
    while num_1 > n:
        num_1 //= 2
        i += 1
    while num_2 > n:
        num_2 //= 2
        j += 1

    while num_1 ==n or num_2 ==n:
        if num_1 > n:
            num_1 -= 1
            i+=1
        else:
            num_1 += 1
            i+=1

        if num_2 > n:
            num_2 -= 1
            j+=1
        else:
            num_2 += 1
            j+=1
    if num_1 == n:
        print(i)
    else:
        print(j)
else:
    num_1 = 0
    i = 0
    while num_1 > n:
        num_1 //= 2
        i += 1
    while num_1 ==n:
        if num_1 > n:
            num_1 -= 1
            i+=1
        else:
            num_1 += 1
            i+=1
    print(i)

>>>>>>> 6013d647a11a57e075f9e22c3102e8c03e17b215
