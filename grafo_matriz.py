class Grafo:
    def __init__(self, vertices, direcionado=False):
        self.vertices = vertices
        self.direcionado = direcionado
        self.matriz_adj = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.matriz_pesos = [[float('inf') for _ in range(vertices)] for _ in range(vertices)]
        self.arestas = 0

    def adicionar_aresta(self, origem, destino, peso=1):
        if origem < 0 or origem >= self.vertices or destino < 0 or destino >= self.vertices:
            raise ValueError("Vértice inválido.")
        
        if self.matriz_adj[origem][destino] == 0:
            self.arestas += 1

        self.matriz_adj[origem][destino] = 1
        self.matriz_pesos[origem][destino] = peso

        if not self.direcionado:
            self.matriz_adj[destino][origem] = 1
            self.matriz_pesos[destino][origem] = peso

    def remover_aresta(self, origem, destino):
        if origem < 0 or origem >= self.vertices or destino < 0 or destino >= self.vertices:
            raise ValueError("Vértice inválido.")

        if self.matriz_adj[origem][destino] == 1:
            self.arestas -= 1

        self.matriz_adj[origem][destino] = 0
        self.matriz_pesos[origem][destino] = float('inf')

        if not self.direcionado:
            self.matriz_adj[destino][origem] = 0
            self.matriz_pesos[destino][origem] = float('inf')

    def matriz_adj_complementar(self):
        matriz_complementar = [[0 for _ in range(self.vertices)] for _ in range(self.vertices)]

        for i in range(self.vertices):
            for j in range(self.vertices):
                if i != j and self.matriz_adj[i][j] == 0:
                    matriz_complementar[i][j] = 1

        return matriz_complementar

    def imprimir_matriz_adj(self):
        print("Matriz de Adjacência:")
        for linha in self.matriz_adj:
            print(linha)

    def imprimir_ordem_e_tamanho(self):
        print(f"Ordem: {self.vertices}")
        print(f"Tamanho: {self.arestas}")

    def vizinhos_e_grau(self):
        print("Vértice | Vizinhos | Grau")
        for i in range(self.vertices):
            vizinhos = [j for j in range(self.vertices) if self.matriz_adj[i][j] == 1]
            grau = len(vizinhos)
            print(f"   {i}   |   {vizinhos}    |   {grau}")

    def executar(self):
        while True:
            print("\nMENU:")
            print("1. Adicionar Aresta")
            print("2. Remover Aresta")
            print("3. Imprimir Matriz de Adjacência")
            print("4. Imprimir Ordem e Tamanho")
            print("5. Imprimir Vizinhos e Grau")
            print("6. Imprimir Matriz de Adjacência Complementar")
            print("7. Sair")

            escolha = int(input("Digite sua escolha: "))
            match escolha:
                case 1:
                    origem = int(input("Digite o vértice de origem: "))
                    destino = int(input("Digite o vértice de destino: "))
                    peso = float(input("Digite o peso (padrão 1 se não ponderado): "))
                    self.adicionar_aresta(origem, destino, peso)
                case 2:
                    origem = int(input("Digite o vértice de origem: "))
                    destino = int(input("Digite o vértice de destino: "))
                    self.remover_aresta(origem, destino)
                case 3:
                    self.imprimir_matriz_adj()
                case 4:
                    self.imprimir_ordem_e_tamanho()
                case 5:
                    self.vizinhos_e_grau()
                case 6:
                    matriz_complementar = self.matriz_adj_complementar()
                    print("Matriz de Adjacência Complementar:")
                    for linha in matriz_complementar:
                        print(linha)
                case 7:
                    break
                case _:
                    print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    vertices = int(input("Digite o número de vértices: "))
    direcionado = input("O grafo é direcionado? (s/n): ").lower() == 's'
    grafo = Grafo(vertices, direcionado)
    grafo.executar()
