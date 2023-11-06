from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *
from bibgrafo.aresta import Aresta


class MeuGrafo(GrafoListaAdjacencia):

    def dfs(self, V=''):
       arvore_dfs = MeuGrafo()
       arvore_dfs.adiciona_vertice(V)
       dic_pais = {V: 0}
       self.dfs_rec(arvore_dfs, dic_pais, V)
       return arvore_dfs
       
    def dfs_rec(self, arvore_dfs, dic_pais, V=''):
        arestas_sobre_vertice = list(self.arestas_sobre_vertice(V))
        arestas_sobre_vertice.sort()
        for i in arestas_sobre_vertice:
            v1 = self.get_aresta(i).v1.rotulo
            v2 = self.get_aresta(i).v2.rotulo
            if (not arvore_dfs.existe_rotulo_aresta(i)) and not(arvore_dfs.existe_rotulo_vertice(v1) and arvore_dfs.existe_rotulo_vertice(v2)):
                aresta_a_seguir = i
                break
            if i == arestas_sobre_vertice[-1]:
                pai = dic_pais[V]
                if pai == 0:
                    return arvore_dfs
                return self.dfs_rec(arvore_dfs, dic_pais, pai)
        if self.arestas[aresta_a_seguir].v1.rotulo == V:
            v2 = self.arestas[aresta_a_seguir].v2.rotulo
        else:
            v2 = self.arestas[aresta_a_seguir].v1.rotulo
        arvore_dfs.adiciona_vertice(v2)
        dic_pais[v2] = V
        arvore_dfs.adiciona_aresta(aresta_a_seguir, V, v2)
        return self.dfs_rec(arvore_dfs, dic_pais, v2)
    
    def vertices_nao_adjacentes(self):
        
        vert_adj = {}
        saida = set()
        for i in self.arestas.keys():
            x = self.arestas[i].v1
            y = self.arestas[i].v2
            if str(x) not in vert_adj:
                vert_adj[str(x)] = []
            vert_adj[str(x)].append(str(y))
            if str(y) not in vert_adj:
                vert_adj[str(y)] = [] 
            vert_adj[str(y)].append(str(x))
        for i in self.vertices:
            if str(i) not in vert_adj:
                 vert_adj[str(i)] = []
            for j in self.vertices:
                if (str(j) not in vert_adj[str(i)]) and ((f"{str(j)}-{str(i)}") not in saida) and (str(j) != str(i)):
                    saida.add(f"{str(i)}-{str(j)}")
        return saida

    def ha_laco(self):

        for i in self.arestas.keys():
            x = self.arestas[i].v1
            y = self.arestas[i].v2
            if x == y:
                return True
        return False
        
    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError()
        grau = 0
        arestas = self.arestas

        for a in arestas:
            if arestas[a].v1.rotulo == V:
                grau += 1
            if arestas[a].v2.rotulo == V:
                grau += 1
        return grau

        # vert_adj = {}
        # for i in self.arestas.keys():
        #     x = self.arestas[i].v1
        #     y = self.arestas[i].v2
        #     if str(x) not in vert_adj:
        #         vert_adj[str(x)] = []
        #     vert_adj[str(x)].append(str(y))
        #     if str(y) not in vert_adj:
        #         vert_adj[str(y)] = []
        #     vert_adj[str(y)].append(str(x))
        
        # if self.existe_rotulo_vertice(V) == False:
        #     raise VerticeInvalidoError()
        # if V not in vert_adj:
        #     return 0
        # return len(vert_adj[V])

    def ha_paralelas(self):
        
        vert_adj = {}
        for i in self.arestas.keys():
            x = self.arestas[i].v1
            y = self.arestas[i].v2
            if str(x) not in vert_adj:
                vert_adj[str(x)] = []
            vert_adj[str(x)].append(str(y))
            if str(y) not in vert_adj:
                vert_adj[str(y)] = []
            vert_adj[str(y)].append(str(x))
            if vert_adj[str(x)].count(str(y)) > 1:
                return True
        return False
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''

    def arestas_sobre_vertice(self, V):

        if self.existe_rotulo_vertice(V) == False:
            raise VerticeInvalidoError()
        arestas_v = set()
        for i in self.arestas.keys():
            x = self.arestas[i].v1
            y = self.arestas[i].v2
            if str(x) == str(V):
                arestas_v.add(i)
            if str(y) == str(V):
                arestas_v.add(i)
        return arestas_v

    def eh_completo(self):

        vert_adj = {}
        for i in self.arestas.keys():
            x = self.arestas[i].v1
            y = self.arestas[i].v2
            if x == y:
                return False
            if str(x) not in vert_adj:
                vert_adj[str(x)] = []
            vert_adj[str(x)].append(y)
            if str(y) not in vert_adj:
                vert_adj[str(y)] = []
            vert_adj[str(y)].append(x)
        for i in self.vertices:
            if str(i) not in vert_adj:
                vert_adj[str(i)] = []
            for x in self.vertices:
                if x not in vert_adj[str(i)] and x != i:
                    return False
        return True