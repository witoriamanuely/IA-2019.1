from prioridade

class AStarSearch:
     def heuristica(a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    def aEstrela(self, grafo, inicio, destino):
        fila = prioridadeFila()
        fila.put(inicio, 0)
        vindo_de = {}
        custo_ate_agora = {}
        vindo_de[inicio] = None
        custo_ate_agora[inicio] = 0

        while not fila.empty():
            atual = fila.get()

            if atual == destino:
                break

            for proximo in grafo.retornaGrafo(atual):
                novo_custo = custo_ate_agora[atual] + grafo.retornaGrafoCusto(atual, proximo)
                if proximo not in custo_ate_agora or novo_custo < custo_ate_agora[next]:
                    custo_ate_agora[next] = novo_custo
                    prioridade = novo_custo + self.heuristica(destino, proximo)
                    fila.put(proximo, prioridade)
                    vindo_de[proximo] = atual

        return vindo_de, custo_ate_agora