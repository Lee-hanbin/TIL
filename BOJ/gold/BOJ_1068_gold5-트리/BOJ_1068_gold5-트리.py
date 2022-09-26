# BOJ_1068_gold5-트리

from collections import defaultdict
import sys
input = sys.stdin.readline

# 전위 순회
def pre_order(root):
    global cnt
    if len(ch_dict[root]) == 0:
        cnt += 1
    else:
        while ch_dict[root]:
            pre_order(ch_dict[root][-1])
            ch_dict[root].pop()


ch_dict = defaultdict(list)         # 자식을 연결한 딕셔너리
p_dict = defaultdict(list)          # 부모를 연결한 딕셔너리
cnt = 0                             # 리프노드의 개수 담기
n = int(input())
tree = map(int, input().split())    # 트리 입력받기
rmv = int(input())                  # 끊을 자식
# 모든 잎에 value 리스트 부여
for i in range(n):
    ch_dict[i] = []
# root를 확인하고 트리를 연결해준다.
for j, e in enumerate(tree):
    if e == -1:
        root = j
    else:
        ch_dict[e] += [j]
        p_dict[j] += [e]
# 끊어내는 노드의 부모가 있다면
if len(p_dict[rmv]) > 0:
    live_node = p_dict[rmv][0]              # 끊어내는 노드의 부모노드 찾기
    idx = ch_dict[live_node].index(rmv)     # 그 부모노드에서 끊어내는 노드의 인덱스 찾기
    del(ch_dict[rmv])                       # 해당 노드를 root로 하는 트리 지워버리기
    ch_dict[live_node].pop(idx)             # 부모노드에서 해당 노드 찾아서 지우기
    pre_order(root)                         # 순회하면서 리프노드 카운트
# 끊어내는 노드의 부모가 없다면 0을 출력한다
print(cnt)


