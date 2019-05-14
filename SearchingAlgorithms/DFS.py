class DFS:
    def DFSUtil(self, v, visitado, grafo):
        visitado[v] = True
        print(v)
        #Percorre o grafo e verifica se o lugar não foi visitado, e retorna pro mesmo método até ser visitados todos
        for i in grafo[v]:
            if visitado[i] == False:
                self.DFSUtil(i, visitado)


    def DFS(self, v, grafo):
        visitado = [False] * (len(grafo))
        self.DFSUtil(v, visitado, grafo)