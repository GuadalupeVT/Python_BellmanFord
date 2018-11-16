'''
Created on 16/11/2018

@author: GVT
'''
from collections import defaultdict 
  
class Grafo: 
  
    def __init__(self,vertices): 
        self.V= vertices 
        self.grafo = []  
   
    
    def agregarEdge(self,u,v,w): 
        self.grafo.append([u, v, w]) 
          
    
    def imprimir(self, distancia): 
        print("Vertice    Distancia desde el origen") 
        for i in range(self.V): 
            print("%d \t\t %d" % (i, distancia[i])) 
      
    
    def BellmanFord(self, src): 
        distancia = [float("Inf")] * self.V 
        distancia[src] = 0 
  
        for i in range(self.V - 1): 
            for u, v, w in self.grafo: 
                if distancia[u] != float("Inf") and distancia[u] + w < distancia[v]: 
                        distancia[v] = distancia[u] + w 
  
  
        for u, v, w in self.grafo: 
                if distancia[u] != float("Inf") and distancia[u] + w < distancia[v]: 
                        print "El grafo contiene algun peso negativo"
                        return
                          
        self.imprimir(distancia) 
  
g = Grafo(5) 
print "Se creara un grafo de 0-4"
a1=int(raw_input("Distancia de 0-1"))
a2=int(raw_input("Distancia de 0-2"))    
a3=int(raw_input("Distancia de 1-2"))  
a4=int(raw_input("Distancia de 1-3"))  
a5=int(raw_input("Distancia de 1-4"))  
a6=int(raw_input("Distancia de 3-2"))  
a7=int(raw_input("Distancia de 3-1"))
a8=int(raw_input("Distancia de 4-3"))    

g.agregarEdge(0, 1, a1) 
g.agregarEdge(0, 2, a2) 
g.agregarEdge(1, 2, a3) 
g.agregarEdge(1, 3, a4) 
g.agregarEdge(1, 4, a5) 
g.agregarEdge(3, 2, a6) 
g.agregarEdge(3, 1, a7) 
g.agregarEdge(4, 3, a8) 

print "-------------Camino mas corto desde el origen---------------"
  
g.BellmanFord(0) 