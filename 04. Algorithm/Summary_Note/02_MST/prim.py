


###### prim #######################################################################################

'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

from collections import defaultdict

V, E = map(int,input().split())
graph_list = defaultdict(list)
graph_matrix = [[0]*(V+1) for _ in range(V+1)]

for _ in range(E):
    s, e, weight = map(int,input().split())
    graph_list[s].append((weight,s,e))
    graph_list[e].append((weight,e,s))

    graph_matrix[s][e] = weight
    graph_matrix[e][s] = weight




# prim

def prim(node):
    visited = [0]*(V+1)
    key = [float('inf')]*(V+1)
    parent = [-1]*(V+1)
    key[node] = 0
    for _ in range(V+1):
        min_val = float('inf')

        for i in range(V+1):
            if visited[i]==0 and key[i] < min_val:
                s = i
                min_val = key[i]
        visited[s] = 1

        for e in range(V+1):
            if visited[e] == 0 and graph_matrix[s][e]>0:
                key[e] = min(key[e], graph_matrix[s][e])
                if key[e] > graph_matrix[s][e]:
                    key[e] = graph_matrix[s][e]
                    parent[e] = s
    return sum(key)






# prim, 우선순위 큐


import heapq

def prim2(node):
    
    mst = []

    visited = {node}

    candidate = graph_list[node]
    heapq.heapify(candidate)

    while len(visited) < V+1 and candidate :
        weight, s, e = heapq.heappop(candidate)

        if e not in visited:
            visited.add(e)
            mst.append((weight,s,e))

            for route in graph_list[e]:
                if route[2] not in visited:
                    heapq.heappush(candidate, route)

    return sum(map(lambda x : x[0], mst))