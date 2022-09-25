# BOJ_1991_silver1-트리순회

from collections import defaultdict
import sys
input = sys.stdin.readline

def in_order(root):
    if root != '.':
        in_order(tree[root][0])
        print(root,end='')
        in_order(tree[root][1])
def pre_order(root):
    if root != '.':
        print(root, end='')
        pre_order(tree[root][0])
        pre_order(tree[root][1])


def post_order(root):
    if root != '.':
        post_order(tree[root][0])
        post_order(tree[root][1])
        print(root, end='')


n = int(input())
tree = defaultdict()
for i in range(n):
    node, l_node, r_node = input().split()
    tree[node] = l_node + r_node
pre_order('A')
print()
in_order('A')
print()
post_order('A')
