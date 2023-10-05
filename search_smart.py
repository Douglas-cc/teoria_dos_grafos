class Euristica:
    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo
        self.visitado = False
        self.distancia_acumulada = 0
        self.distancia_objetivo = distancia_objetivo
        self.adjacentes = []
        self.caminho_a_estrela = []

    def adiciona_adjacente(self, vertice_adjacente, custo):
        self.adjacentes.append((vertice_adjacente, custo))

    def mostra_adjacentes(self):
        for adjacente, custo in self.adjacentes:
            print(adjacente.rotulo, custo)
            
        
    def insere_adjacente_ordenado(self, vertice, custo):
        self.adjacentes.append((vertice, custo))

    def imprime(self):
        print("Rotulo:", self.rotulo)
        print("Distancia para o objetivo:", self.distancia_objetivo)
        

    def busca_gulosa(self, objetivo):
        fila = []  # Usando uma lista como fila
        fila.append(self)

        while fila:
            fila.sort(key=lambda x: x.distancia_objetivo)  # Ordena a fila pelo valor da distância até o objetivo
            atual = fila.pop(0)  # Remove o primeiro elemento da fila (menor distância)

            print(f"vertice { atual.rotulo} distancia do obejtivo {atual.distancia_objetivo}")
            if atual == objetivo:
                return f"Objetivo atingido {atual.rotulo}"

            atual.visitado = True

            for adjacente, _ in atual.adjacentes:
                if not adjacente.visitado:
                    fila.append(adjacente)
                    
        return "Objetivo não encontrado"
    
    
    def busca_a_estrela(self, objetivo):
        if self == objetivo:
            return f"Objetivo encontrado:{self.rotulo}"

        self.visitado = True
        vetor_ordenado = []

        for adjacente, custo in self.adjacentes:
            print(f"vertice {adjacente} distancia do obejtivo {custo}")
            if not adjacente.visitado:
                adjacente.distancia_acumulada = self.distancia_acumulada + custo
                vetor_ordenado.append(adjacente)
                
        vetor_ordenado.sort(key=lambda x: x.distancia_acumulada + x.distancia_objetivo)

        for adjacente in vetor_ordenado:
            if not adjacente.visitado:
                adjacente.visitado = True
                adjacente.caminho = self.caminho_a_estrela + [self]
                adjacente.busca_a_estrela(objetivo)
