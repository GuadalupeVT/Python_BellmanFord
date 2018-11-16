'''
Created on 16/11/2018

@author: GVT
'''
def bellmanFord(V,E):
    dist = [float('inf')] * V
    prev = [None] * V
    dist[0] = 0

    for i in range(V-1):
        for edge in E:
            relax(edge[0],edge[1],edge[2],dist,prev)

    #revisa ciclos negativos       
    for e in E:
        u = e[0]
        v = e[1]
        w = e[2]
        if dist[u]+w < dist[v]:
            return 1

    return 0