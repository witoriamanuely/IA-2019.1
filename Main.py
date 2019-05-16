from SearchingAlgorithms.DFS import DFS
from SearchingAlgorithms.BFS import BFS
from SearchingAlgorithms.AStarSearch import AStarSearch
import SearchingAlgorithms.Grafo as Grafo

def main():
    while True:
        print("\n\n1-DFS\n2-BFS\n3-A*\n4-Sair")
        escolha = input("Opção: ")
        if escolha != "1" and escolha != "2" and escolha != "3" and escolha != "4":
            print("Escolha uma das opções acima.")
        else:
            if escolha == "4":
                quit(0)
            else:
                grafo = Grafo.retornaGrafo()
                while True:
                    origem = input("\nCidade Origem: ")
                    if origem not in grafo.nodes:
                        print("Cidade não existente")
                    else:
                        break
                while True:
                    destino = input("\nCidade Destino: ")
                    if destino not in grafo.nodes:
                        print("Cidade não existente")
                    else:
                        break
                print("\n")
                if escolha == "1":
                    dfs = DFS(grafo)
                    dfs.DFS(origem, destino)
                elif escolha == "2":
                    bfs = BFS(grafo)
                    bfs.BFS(origem, destino)
                elif escolha == "3":
                    astar = AStarSearch(grafo, Grafo.heuristicaDistancia())
                    astar.aStarSearch(origem, destino)


if __name__ == '__main__':
    main()