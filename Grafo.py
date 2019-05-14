import csv
from pprint import pprint

def retornaGrafo():
    grafo = {}

    with open("csv/arestas.csv", "r") as csv_file:
        tabela = csv.reader(csv_file)
        for linha in tabela:
            if linha[0] in grafo:
                grafo[linha[0]].append(linha[1])
            else:
                grafo[linha[0]] = [linha[1]]

    return grafo


def retornaGrafoCusto():
    grafo = {}

    with open("csv/arestas.csv", "r") as csv_file:
        tabela = csv.reader(csv_file)
        for linha in tabela:
            if linha[0] in grafo:
                grafo[linha[0]].append((linha[1], linha[2]))
            else:
                grafo[linha[0]] = [(linha[1], linha[2])]

    return grafo


def heuristicaDistancia():
    heuristica_csv = open("csv/heuristicaDistancia.csv")
    matDistancia = []

    for j in heuristica_csv:
        sep = j.split(',')
        sep[len(sep) - 1] = sep[len(sep) - 1].replace('\n', '')
        sep.remove(sep[0])
        matDistancia.append(sep)

    ordenacaoCidades = matDistancia[0]
    matDistancia.remove(matDistancia[0])

    for i in range(len(matDistancia)):
        for j in range(len(matDistancia[i])):
            if j >= i:
                matDistancia[i][j] = float(matDistancia[i][j])
            else:
                matDistancia[i][j] = None

    return ordenacaoCidades, matDistancia


pprint(retornaGrafoCusto())