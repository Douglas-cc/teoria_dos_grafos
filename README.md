# Algoritmos de Busca

- Busca em Largura
- Busca em Profundidade
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
