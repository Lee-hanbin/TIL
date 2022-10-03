# 0913

'''
첫 줄에는 트리의 정점의 총 수 V가 주어짐
다음 줄에는 V-1개 간선이 나열
간선은 그것을 이루는 두 정점을 표기
간선은 항상 '부모 자식' 순서로 표기

전위 순회하여 정점의 번호를 출력
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def find_root(V):
    for i in range(1, V+1):
        if par[i] == 0:	# 부모가 없으면 root
            return i

def preorder(n):
    if n:
        print(n, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])


def inorder(n):
    if n:
        inorder(ch1[n])
        print(n, end=' ')
        inorder(ch2[n])


def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end=' ')

V = int(input())                        # 정점 개수, 마지막 정점번호
arr = list(map(int, input().split()))
E = V - 1

ch1 = [0] * (V+1)
ch2 = [0] * (V+1)
par = [0] * (V+1)
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p
root = find_root(V)
print(root)
root = 3
preorder(root)
print()
inorder(root)
print()
postorder(root)
print()
