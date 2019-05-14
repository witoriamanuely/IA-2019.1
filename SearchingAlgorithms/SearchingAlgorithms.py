from collections import defaultdict



class SearchingAlgorithms:

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

    def BFS(self, s, graph):
        visited = [False] * (len(graph))
        row = []
        row.append(s)
        visited[s] = True
        # Percorre o grafo e verifica se o lugar não foi visitado, adiciona na fila uma codição boleana na posição que
        # ainda não foi visitada
        while row:
            s = row.pop(0)
            print(s, end=" ")
            for i in graph[s]:
                if visited[i] == False:
                    row.append(i)
                    visited[i] = True
