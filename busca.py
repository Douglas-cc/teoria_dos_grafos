from collections import defaultdict


class Grafo:
    '''
    Este metodo tem o papael de criar um objeto de lista 
    para adicionar as arestas que vão compor o nosso grafo
    '''
    def __init__(self):
        self.grafo = defaultdict(list)

    # Adiciona os vertices anterior e posterior na lista para formar o grafo
    def adiciona_vertices(self, anterior, posterior):
        self.grafo[anterior].append(posterior)
        
    def exibir_grafo(self):
        return self.grafo
    
    def bfs(self, vertice_atual):
        # Marcar os vertices como não visitados
        visitado = [False] * (len(self.grafo))

        # fila vazia para busca em largura
        fila = []

        # Guardar vertice de origem/atual e marca como visitado e insere na fila
        fila.append(vertice_atual)
        visitado[vertice_atual] = True

        while fila:     
            # Retira o utimo vertice 
            vertice_atual = fila.pop(0)
            print(vertice_atual)

            # Obter todos os vertices adjacentes dos vertices desenfilerados
            for i in self.grafo[vertice_atual]:
                # print(visitado[i])
                if visitado[i] == False:
                    fila.append(i)
                    visitado[i] = True


    def dfs(self, raiz):
        visitados = [] # lista para armazenar os vertices visitados
        visitados.append(raiz) # e obviamente a raiz é o primeiro vertice a ser visitado
        
        '''
        Na lista pegamos aqueles vertices não visitados e enquanto não visitarmos 
        todos os vetices o loop continua fazendo a busca do nosso vertice final
        '''
        nao_visitado = [raiz] 
        while nao_visitado:
            '''
            quando o vertice for visitado nos excluimos ele da lista de não vistados
            e atuaçozamos na variavel vertice para imprimir nossa rota na tela
            '''
            vertice = nao_visitado.pop()
            # resposta da nossa busca!!1
            print(vertice)

            '''
            Varremos os vizinhos de dos vertices e verificamos se eles já foram visitados 
            se já foram visitados fazemos o appende na lista correspondente caso o contrario
            executamos a operação inversa.
            '''
            for i in self.grafo[vertice]:
                if i not in visitados:
                    visitados.append(i)
                    nao_visitado.append(i)