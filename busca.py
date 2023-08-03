import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict


class Grafo:
    def __init__(self, eh_direcionado):
        self.tempo = 1
        self.grafo = defaultdict(list)
        self.eh_direcionado = eh_direcionado
        self._vertices = []
        self._num_vertices = 0
        self._pre_ordem = [0] * self._num_vertices
        self._pos_ordem = [0] * self._num_vertices
        

    @property
    def num_vertices(self):
        return self._num_vertices


    @num_vertices.setter
    def num_vertices(self, value):
        self._num_vertices = value
        self._pre_ordem = [0]*value
        self._pos_ordem = [0]*value


    @property
    def pre_ordem(self):
        return self._pre_ordem
    
    @property
    def pos_ordem(self):
        return self._pos_ordem
        
    @property
    def vertices(self):
        return set(self._vertices)
    
    
    @vertices.setter
    def vertices(self, value):
        self._vertices.append(value)
        

    def adiciona_vertices(self, origem, destino):
        self.vertices = origem
        self.vertices = destino
        self.num_vertices = len(self.vertices)
        
        self.grafo[origem].append(destino)
        if not self.eh_direcionado:
            self.grafo[destino].append(origem)
            

    def exibir_grafo(self):
        for origem, destinos in self.grafo.items():
            for destino in destinos:
               print(f'Origem {origem} -> Destino {destino}')
    
    
    def max_arestas(self):
        return self.num_vertices*(self.num_vertices - 1)/2
    
    
    def total_arestas(self):
        total = 0
        for origem, destinos in self.grafo.items():
            for destino in destinos:
                total += 1
        return total
    

    def plot_grafo(self, color_vertices='lightblue'):
        G = nx.DiGraph() if self.eh_direcionado else nx.Graph()
        for origem, destinos in self.grafo.items():
            for destino in destinos:
               G.add_edge(origem, destino)
        plt.figure(figsize=(6, 4))
        pos = nx.spring_layout(G)  
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_size=1000,
            node_color=color_vertices,
            arrowsize=20
        )
        plt.title('Grafo')
        plt.show()
    

    def pre_pos_ordem(self):                
        print("Tempo de visita da pré e pós-ordem:")
        for i in range(self.num_vertices):
            print(f"Vértice {i} ({self.pre_ordem[i]}/{self.pos_ordem[i]})")     
              
                                                                                              
    def busca_profunda(self, vertice_origem, logs=True):
        resultado = []
        visitados = [] 
        visitados.append(vertice_origem)         
        nao_visitado = [vertice_origem] 
        
        if logs:   
            print('Buscam em Profundidade: ')
            
        while nao_visitado:
            vertice = nao_visitado.pop()
            self._pre_ordem[vertice - 1] = self.tempo
            self.tempo += 1
            
            if logs:
                print(vertice)
            resultado.append(vertice)
            
            for i in self.grafo[vertice]:
                if i not in visitados:
                    visitados.append(i)
                    nao_visitado.append(i)
                    
                self._pos_ordem[vertice - 1] = self.tempo
                self.tempo += 1
        return resultado
                    
                                    
    # def busca_largura(self, vertice_atual):
    #     # Marcar os vertices como não visitados
    #     visitado = [False] * (len(self.grafo))

    #     # fila vazia para busca em largura
    #     fila = []

    #     # Guardar vertice de origem/atual e marca como visitado e insere na fila
    #     fila.append(vertice_atual)
    #     visitado[vertice_atual] = True

    #     while fila:     
    #         # Retira o utimo vertice 
    #         vertice_atual = fila.pop(0)
    #         print(vertice_atual)

    #         # Obter todos os vertices adjacentes dos vertices desenfilerados
    #         for i in self.grafo[vertice_atual]:
    #             # print(visitado[i])
    #             if visitado[i] == False:
    #                 fila.append(i)
    #                 visitado[i] = True