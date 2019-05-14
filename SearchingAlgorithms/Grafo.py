import csv
import networkx as nx
import pandas as pd

def retornaGrafo():
    grafo = nx.Graph()

    with open("csv/arestas.csv", "r") as csv_file:
        tabela = csv.reader(csv_file)
        for linha in tabela:
            grafo.add_edge(linha[0], linha[1], weight=float(linha[2]))

    return grafo


def heuristicaDistancia():
    return pd.read_csv("csv/heuristicaDistancia.csv", header=0, index_col=0)