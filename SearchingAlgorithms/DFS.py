class DFS:
    def DFSUtil(self, v, visited, graph):
        visited[v] = True
        print(v)
        #Percorre o grafo e verifica se o lugar não foi visitado, e retorna pro mesmo método até ser visitados todos
        for i in graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)


    def DFS(self, v, graph):
        visited = [False] * (len(graph))
        self.DFSUtil(v, visited, graph)