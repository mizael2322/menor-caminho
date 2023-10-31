from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *
from bibgrafo.aresta import Aresta


class MeuGrafo(GrafoListaAdjacencia):

    def dfs(self, V=''):
       arvore_dfs = MeuGrafo()
       self.dfs_rec(V, arvore_dfs)
       
    def dfs_rec(self, V='', arvore_dfs):
        arvore_dfs.adiciona_vertice(V)
        # Pega próxima aresta
        

    
    def bfs(self, V=''):
        pass
    
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
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

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