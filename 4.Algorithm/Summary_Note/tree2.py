# tree 응용

# 0913

'''
정점 번호 V : 1 ~ (E+1)
간선 수
부모-자식 순
4
1 2 1 3 3 4 3 5
'''

def find_root(V):
    for i in range(1, V+1):
        if par[i] == 0:	# 부모가 없으면 root
            return i

def preorder(n):
    global cnt
    cnt+=1
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

def f(n):           # global cnt 없이 순회한 정점 수를 리턴하는 함수
    if n == 0:   # 서브트리가 비어있으면
        return 0
    else:
        L = f(ch1[n])
        R = f(ch2[n])
        return L + R + 1

E = int(input())                        # 정점 개수, 마지막 정점번호
arr = list(map(int, input().split()))
V = E + 1
cnt = 0

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
print(f(3))

# preorder(root)
# print()
# inorder(root)
# print()
# postorder(root)
# print()
