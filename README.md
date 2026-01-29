# Solucionador de Labirinto (Python)

Este é um simulador de resolução de labirintos que programei, desenvolvido em Python e executado diretamente no terminal. O usuário define o tamanho do tabuleiro e a quantidade de obstáculos, e um algoritmo de busca (backtracking) tenta encontrar, automaticamente, um caminho entre o ponto de partida e a saída.

## Funcionalidades
* **Tabuleiro Customizável:** O jogador pode escolher o número de linhas e colunas para criar mapas de diversos tamanhos.
* **Geração Aleatória:** Os bloqueios (paredes) são posicionados aleatoriamente pelo mapa a cada execução.
* **Lógica de Backtracking:** O código utiliza um algoritmo recursivo que "anda" pelo campo, marcando o caminho percorrido e retornando caso encontre um beco sem saída, até achar o destino.

## Objetivo da Simulação:
* O algoritmo deve traçar uma rota válida do ponto 'R' (Início) até o ponto 'S' (Saída).
* O caminho não pode passar por bloqueios ('#') ou sair dos limites do mapa.

## Como Executar
    Para testar, você precisa ter o Python 3 instalado em sua máquina. É necessário baixar o arquivo do código (ex: Labirinto.py), abrir o terminal, navegar até o diretório do arquivo e executar o script com Bash python Labirinto.py

### Como configurar

    • Ao iniciar, o programa solicitará que você defina:
        A quantidade de linhas do Tabuleiro
        A quantidade de colunas do Tabuleiro
        A quantidade de bloqueios (paredes) que deseja adicionar

    • O programa então irá:
        1) Gerar o mapa com os bloqueios aleatórios.
        2) Tentar encontrar o caminho automaticamente.
        3) Exibir o resultado final no terminal.


| Símbolo no Mapa            | Significado                                              | 
| :-------------------------:| :-------------------------------------------------------:|
|   R                        | Ponto de Partida (Robô/Início)                           | 
|   S                        | Ponto de Chegada (Saída/Sucesso)                         | 
|   #                        | Bloqueio/Parede (Não é possível atravessar)              | 
|   *                        | Rastro do caminho percorrido pelo algoritmo              | 
|   -                        | Espaço vazio não visitado                                | 


## Condições de Vitória e Derrota

### Vitória (Caminho Encontrado)
```bash
O algoritmo consegue traçar uma linha contínua de '*' do ponto 'R' até o ponto 'S'.

O programa exibe: "Parabens voce ganhou".
```

### Derrota (Sem Saída)
```bash
* Os bloqueios gerados aleatoriamente fecharam todos os caminhos possíveis.
* O algoritmo não encontra rota e o programa exibe: "VOCE PERDEU".
```

### Descrição Final

Este projeto utiliza apenas bibliotecas padrão do Python, sem necessidade de instalação de pacotes externos.

random (para a geração aleatória das posições dos bloqueios)
