
class BFS:
    def BFS(self, s, grafo):
        visitado = [False] * (len(grafo))
        fila = []
        fila.append(s)
        visitado[s] = True
        # Percorre o grafo e verifica se o lugar não foi visitado, adiciona na fila uma codição boleana na posição que
        # ainda não foi visitada
        while fila:
            s = fila.pop(0)
            print(s, end=" ")
            for i in grafo[s]:
                if visitado[i] == False:
                    fila.append(i)
                    visitado[i] = True

