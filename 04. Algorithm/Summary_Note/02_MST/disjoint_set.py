
V = 10
parent = [-1]*(V+1)


def make_set(x):
    parent[x] = x

def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return parent[x]
    return x

def union(x,y):
    parent[find_set(y)] = find_set(x)
