from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo_lista_adj import MeuGrafo
from bibgrafo.aresta import Aresta
from grafo_lista_adj_test import TestGrafo

paraiba = MeuGrafo()

paraiba = MeuGrafo()
paraiba.adiciona_vertice("J")
paraiba.adiciona_vertice("C")
paraiba.adiciona_vertice("E")
paraiba.adiciona_vertice("P")
paraiba.adiciona_vertice("M")
paraiba.adiciona_vertice("T")
paraiba.adiciona_vertice("Z")
paraiba.adiciona_aresta('a1', 'J', 'C')
paraiba.adiciona_aresta('a2', 'C', 'E')
paraiba.adiciona_aresta('a3', 'C', 'E')
paraiba.adiciona_aresta('a4', 'P', 'C')
paraiba.adiciona_aresta('a5', 'P', 'C')
paraiba.adiciona_aresta('a6', 'T', 'C')
paraiba.adiciona_aresta('a7', 'M', 'C')
paraiba.adiciona_aresta('a8', 'M', 'T')
paraiba.adiciona_aresta('a9', 'T', 'Z')


paraiba2 = TestGrafo()

paraiba2.setUp()
paraiba2.test_grau()

paraiba3 = MeuGrafo()
paraiba3.adiciona_vertice("J")
paraiba3.adiciona_vertice("C")
paraiba3.adiciona_vertice("E")
paraiba3.adiciona_aresta('a1', 'J', 'C')
paraiba3.adiciona_aresta('a2', 'C', 'E')
paraiba3.adiciona_aresta('a3', 'E', 'J')








