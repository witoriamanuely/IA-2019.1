import heapq
import numpy as np

class prioridadeQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, prioridade):
        heapq.heappush(self.elements, (prioridade, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

class AStarSearch:
    def __init__(self, grafo, heuristica):
        self.grafo = grafo
        self.heuristica = heuristica


    def backtracking(self, dicionario, destino):
        vertice = destino
        caminho = []
        
        while True:
            if vertice == None:
                break
            caminho.append(vertice)
            vertice = dicionario[vertice]
        return caminho

    
    def imprimirCaminho(self, caminho):
        print("Caminho achado utilizando A*:")
        for i in range(len(caminho)-1, -1, -1):
            if i == 0:
                print(caminho[i])
            else:
                print(caminho[i], "->", end=" ")


    def aStarSearch(self, origem, destino):
        filaPrioridade = prioridadeQueue()
        filaPrioridade.put(origem, 0)
        vindoDe = {}
        custoAteAgora = {}
        vindoDe[origem] = None
        custoAteAgora[origem] = 0

        while not filaPrioridade.empty():
            atual = filaPrioridade.get()

            if atual == destino:
                break

            for vizinho in self.grafo.neighbors(atual):
                novo_custo = custoAteAgora[atual] + self.grafo[atual][vizinho]["weight"]
                if vizinho not in custoAteAgora or novo_custo < custoAteAgora[vizinho]:
                    custoAteAgora[vizinho] = novo_custo
                    prioridade = novo_custo + self.menorValorHeuristica(vizinho, destino)
                    filaPrioridade.put(vizinho, prioridade)
                    vindoDe[vizinho] = atual

        self.imprimirCaminho(self.backtracking(vindoDe, destino))


    def menorValorHeuristica(self, vertice, objetivo):
        visitado = [vertice]
        
        vizinhos = list(set(self.grafo[vertice]) - set(visitado))
        menor = vizinhos[0]
        menorValor = 0

        for i in vizinhos[1:]:
            valoresHeuristica = self.heuristica[objetivo][i]
            if np.isnan(valoresHeuristica):
                valoresHeuristica = self.heuristica[i][objetivo]

            heuristicaMin = self.heuristica[objetivo][menor]
            if np.isnan(heuristicaMin):
                heuristicaMin = self.heuristica[menor][objetivo]

            if self.grafo[vertice][i]["weight"] + valoresHeuristica < self.grafo[vertice][menor]["weight"] + heuristicaMin:
                menorValor = self.grafo[vertice][i]["weight"] + valoresHeuristica

        return menorValor