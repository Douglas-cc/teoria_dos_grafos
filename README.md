# Algoritmos de Busca 

- Busca em Largura
- Busca em Profundidade
- Busca Aestrela
- Busca Gulosa
- Dijkstra


## Busca em Largura 
Na teoria dos grafos, busca em largura (ou busca em amplitude, também conhecido em inglês por Breadth-First Search - BFS) 
é um algoritmo de busca em grafos utilizado para realizar uma busca ou travessia num grafo e estrutura de dados do tipo árvore. 
Intuitivamente, você começa pelo vértice raiz e explora todos os vértices vizinhos. Então, para cada um desses vértices mais 
próximos, exploramos os seus vértices vizinhos inexplorados e assim por diante, até que ele encontre o alvo da busca.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Breadth-First-Search-Algorithm.gif/250px-Breadth-First-Search-Algorithm.gif" />
</p>

## Busca em Profunda
O algoritmo de busca em profundidade varre (= scans) um grafo e visita todos seus vértices e todos seus arcos. À medida que varre o 
grafo, o algoritmo pinta cada vértice de cinza e depois de preto. Quando descobre um novo vértice, o algoritmo pinta o vértice de cinza; 
quando termina de visitar todos os vizinhos do vértice, o algoritmo pinta o vértice de preto. Os vértices cinza são considerados ativos 
e os pretos são considerados mortos.

<p align="center">
  <img src="https://www.ime.usp.br/~pf/algoritmos_para_grafos/aulas/figs/mine/rtree6c.png" />
</p>

## Aestrela

O algoritmo de busca A* (A-Star) é um algoritmo de busca heurística utilizado para encontrar o caminho mais curto entre um nó inicial e um nó de destino em um grafo ponderado. Ele é amplamente usado em problemas de busca em inteligência artificial, como em sistemas de roteamento de mapas e jogos.

A ideia principal do algoritmo A* é encontrar um equilíbrio entre a busca em largura (busca de todos os caminhos possíveis) e a busca em profundidade (busca em direção ao destino). Ele utiliza duas funções para determinar a prioridade de expansão dos nós:

1. Função de custo g(n): Essa função calcula o custo acumulado de alcançar um nó específico a partir do nó inicial. Ela rastreia a distância percorrida até o nó atual.

2. Função heurística h(n): Essa função estima o custo restante para alcançar o nó de destino a partir do nó atual. Ela fornece uma estimativa heurística do custo futuro.

O algoritmo A* calcula uma pontuação F(n) para cada nó visitado, que é a soma da função de custo g(n) e da função heurística h(n):

F(n) = g(n) + h(n)

O algoritmo mantém uma lista de nós a serem explorados, chamada de "fronteira", ordenada por F(n). Em cada iteração, o nó com a menor pontuação F(n) é escolhido para expansão. A expansão de um nó envolve a geração de seus nós vizinhos e o cálculo das pontuações F(n) para esses nós. O processo continua até que o nó de destino seja alcançado ou até que a fronteira esteja vazia (o que significa que não existe um caminho válido).

O algoritmo A* tem a garantia de encontrar o caminho mais curto, desde que a função heurística h(n) seja admissível (nunca superestime o custo real) e consistente (satisfaz a desigualdade triangular). A escolha da função heurística é crítica para o desempenho do algoritmo, pois influencia diretamente a eficiência da pesquisa.


<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/9/98/AstarExampleEn.gif" />
</p>


## Gulosa

A busca gulosa, também conhecida como busca heurística ou busca de melhor escolha, é um algoritmo de busca utilizado em problemas de otimização. Ela funciona de forma bastante simples, seguindo os seguintes passos:

1. Inicialização: Comece a partir de um estado inicial.

2. Avaliação: Avalie todos os estados vizinhos do estado atual com base em uma função heurística, que fornece uma estimativa de quão próximo cada estado está do objetivo. Quanto menor o valor da função heurística, melhor.

3. Escolha: Escolha o estado vizinho com a menor estimativa da função heurística como próximo estado.

4. Atualização: Faça o estado escolhido no passo anterior se tornar o novo estado atual.

5. Repita os passos 2 a 4 até que um critério de parada seja atendido (por exemplo, encontrar o estado objetivo ou não ter mais estados para explorar).

É importante notar que a busca gulosa pode não encontrar a solução ótima, pois ela tende a seguir rapidamente em direção a estados que parecem promissores com base na função heurística, sem considerar completamente a possibilidade de caminhos alternativos que podem levar a soluções melhores. Portanto, a busca gulosa é adequada para problemas em que a solução aproximada é suficiente ou quando o tempo de execução é um fator crítico.

<p align="center">
  <img src="https://i.ytimg.com/vi/Axmq9sQ9U08/sddefault.jpg" />
</p>

## Dijkstra
O Algoritmo de Dijkstra (E.W. Dijkstra) é um dos algoritmos que calcula o caminho de custo mínimo entre vértices de um grafo. Escolhido um vértice como raiz da busca, este algoritmo calcula o custo mínimo deste vértice para todos os demais vértices do grafo. Ele é bastante simples e com um bom nível de performance. Ele não garante, contudo, a exatidão da solução caso haja a presença de arcos com valores negativos.

Este algoritmo parte de uma estimativa inicial para o custo mínimo e vai sucessivamente ajustando esta estimativa. Ele considera que um vértice estará fechado quando já tiver sido obtido um caminho de custo mínimo do vértice tomado como raiz da busca até ele. Caso contrário ele dito estar aberto.

<p align="center">
  <img src="https://www.ic.unicamp.br/~meidanis/courses/mo417/2010s1/pool/ra_033072_img/grafo_dijkstra.jpg" />
</p>

# Como instalar as dependências do projeto

- Instalando versão python com pyenv 
```bash
pyenv install 3.10.0
```

- Definindo versão local do projeto
```bash
pyenv local 3.10.0
```

- Criando um ambiente virtual com versão de cima do Python
```bash 
poetry env use 3.10
```

- Iniciar o ambiente virtual
```bash 
poetry shell
```
- Instalar bibliotecas python .toml
```bash 
poetry install
```
