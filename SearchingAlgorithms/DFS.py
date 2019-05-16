from collections import defaultdict

class DFS:
    def __init__(self, grafo):
        self.grafo = grafo
        self.encontrouCaminho = False
        self.caminho = []

    
    def imprimeCaminho(self):
        print("Caminho achado utilizando DFS:")
        for i in range(len(self.caminho)):
            if i+1 == len(self.caminho):
                print(self.caminho[i])
            else:
                print(self.caminho[i], "->", end=" ")

    
    def DFS(self, origem, destino):
        visitados = {}
        vertice = origem

        for indice in self.grafo.nodes:
            visitados[indice] = False
   
        pilha = []
    
        pilha.append(vertice)
    
        while not len(pilha) == 0:
            vertice = pilha.pop(); 

            if vertice == destino:
                self.caminho.append(vertice)
                self.imprimeCaminho()
                return

            if not visitados[vertice]:
                self.caminho.append(vertice)
                visitados[vertice] = True

            for vizinhos in self.grafo.neighbors(vertice):
                if not visitados[vizinhos]
                    pilha.append(vizinhos)