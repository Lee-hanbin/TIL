# # BOJ_1068_gold5-트리
#
# from collections import defaultdict
# import sys
# input = sys.stdin.readline
#
# # 전위 순회
# def pre_order(root):
#     global cnt
#     if len(ch_dict[root]) == 0:
#         cnt += 1
#     else:
#         while ch_dict[root]:
#             pre_order(ch_dict[root][-1])
#             ch_dict[root].pop()
#
#
# ch_dict = defaultdict(list)         # 자식을 연결한 딕셔너리
# p_dict = defaultdict(list)          # 부모를 연결한 딕셔너리
# cnt = 0                             # 리프노드의 개수 담기
# n = int(input())
# tree = map(int, input().split())    # 트리 입력받기
# rmv = int(input())                  # 끊을 자식
# # 모든 잎에 value 리스트 부여
# for i in range(n):
#     ch_dict[i] = []
# # root를 확인하고 트리를 연결해준다.
# for j, e in enumerate(tree):
#     if e == -1:
#         root = j
#     else:
#         ch_dict[e] += [j]
#         p_dict[j] += [e]
# # 끊어내는 노드의 부모가 있다면
# if len(p_dict[rmv]) > 0:
#     live_node = p_dict[rmv][0]              # 끊어내는 노드의 부모노드 찾기
#     idx = ch_dict[live_node].index(rmv)     # 그 부모노드에서 끊어내는 노드의 인덱스 찾기
#     del(ch_dict[rmv])                       # 해당 노드를 root로 하는 트리 지워버리기
#     ch_dict[live_node].pop(idx)             # 부모노드에서 해당 노드 찾아서 지우기
#     pre_order(root)                         # 순회하면서 리프노드 카운트
# # 끊어내는 노드의 부모가 없다면 0을 출력한다
# print(cnt)
#
#

import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

def bfs(start):
    global cnt
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        if graph.get(now):
            for next in graph[now]:
                q.append(next)
        else:
            cnt += 1

n = int(input())
p = list(map(int, input().split()))
del_node = int(input())
graph = {}

for i,v in enumerate(p):
    if i == 0:
        continue
    if v in graph:
        graph[v].append(i)
    else:
        graph[v] = [i]

# 노드 삭제하기
del_parent = p[del_node]
if del_parent == -1:     # 루트를 삭제할 경우
    print(0)
else:
    graph[del_parent].remove(del_node)
    cnt = 0
    bfs(p.index(-1))
    print(cnt)
