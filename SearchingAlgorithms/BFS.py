
class BFS:
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

