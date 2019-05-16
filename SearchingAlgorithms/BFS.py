class BFS:
    def __init__(self, grafo):
        self.grafo = grafo
        self.caminho = []


    def imprimeCaminho(self):
        print("Caminho achado utilizando BFS:")
        for i in range(len(self.caminho)):
            if i+1 == len(self.caminho):
                print(self.caminho[i])
            else:
                print(self.caminho[i], "->", end=" ")


    def BFS(self, origem, destino):
        visitados = {}

        for indice in self.grafo.nodes:
            visitados[indice] = False

        fila = []
        fila.append(origem)
        visitados[origem] = True
        # Percorre o grafo e verifica se o lugar não foi visitado, adiciona na fila uma codição boleana na posição que
        # ainda não foi visitada
        while fila:
            origem = fila.pop(0)
            self.caminho.append(origem)
            if origem == destino:
                self.imprimeCaminho()
                return
            for i in self.grafo.neighbors(origem):
                if visitados[i] == False:
                    fila.append(i)
                    visitados[i] = True
