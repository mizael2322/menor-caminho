from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo_lista_adj import MeuGrafo
from bibgrafo.aresta import Aresta
from grafo_lista_adj_test import TestGrafo

paraiba2 = TestGrafo()
paraiba2.setUp()


g_p_com_peso = MeuGrafo()
g_p_com_peso.adiciona_vertice("J")
g_p_com_peso.adiciona_vertice("C")
g_p_com_peso.adiciona_vertice("E")
g_p_com_peso.adiciona_vertice("P")
g_p_com_peso.adiciona_vertice("T")
g_p_com_peso.adiciona_vertice("M")
g_p_com_peso.adiciona_vertice("Z")
g_p_com_peso.adiciona_vertice("A")

g_p_com_peso.adiciona_aresta("a1", "J", "C", 3)
g_p_com_peso.adiciona_aresta("a2", "C", "E", 5)
g_p_com_peso.adiciona_aresta("a3", "C", "E", 1)
g_p_com_peso.adiciona_aresta("a4", "C", "P", 3)
g_p_com_peso.adiciona_aresta("a5", "C", "P", 3)
g_p_com_peso.adiciona_aresta("a6", "C", "T", 4)
g_p_com_peso.adiciona_aresta("a7", "C", "M", 3)
g_p_com_peso.adiciona_aresta("a8", "T", "M", 1)
g_p_com_peso.adiciona_aresta("a9", "T", "Z", 6)
g_p_com_peso.adiciona_aresta("a10", "P", "Z", 13)
g_p_com_peso.adiciona_aresta("a12", "P", "A", 1)
g_p_com_peso.adiciona_aresta("a13", "A", "C", 2)
g_p_com_peso.adiciona_aresta("a14", "C", "Z", 10)

print(g_p_com_peso.dfs('AAA'))












