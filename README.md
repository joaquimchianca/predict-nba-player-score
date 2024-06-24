# Projeto de Machine Learning - Unidade 03

## Descrição do projeto
O projeto contém nesse repositório um Jupyter Notebook, com objetivo de descobrir qual o modelo com mais acurácia a fim de aplicá-lo num app de CLI (Command Line Interface)
que responde a seguinte pergunta: **Dada uma certa quantia de pontos, um jogador escolhido consegue marcar mais ou menos pontos do que essa quantia?**

Para isso, foram treinados diferentes modelos, seguindo os algoritmos: kNN, Árvores de Decisão, Random Forest Tree, Gradient Boosting Machine. Para cada um desses algoritmos, testamos
conjuntos de hiperparâmetros diferentes. Por meio da experimentação, descobrimos um modelo com 95.83% de acurácia, usando o Random Forest Tree Algorithm para treinamento.
Mais detalhes do modelo usado no app está no arquivo `models/random_forest.py`.

## Estrutura de diretórios
```
.
├── cli_app.py                       # App interativo
├── database_csv.csv                 # Base de dados obtidos a partir do Kaggle
├── model/                          
│   ├── random_forest.py             # Modelo usado no cli_app.py
│   └── setup.py                     # Funções de leitura e processamento de dados, assim como uma função auxiliar para listar jogadores
├── projeto_joaquim_chianca.ipynb    # Projeto no Jupyter Notebook que define o modelo de maior acurácia, usando no `cli_app.py`
└── requirements.txt                 # Dependência do cli_app.py
```

## Executar o programa

1. Clone este repositório

`git clone git@github.com:joaquimchianca/predict-nba-player-score.git`

2. Se necessário, instale as dependências do projeto:

`pip install -r requirements.txt`

3. Entenda o fluxo de execução do app:

```
usage: app [-h] [--name NAME] [--points POINTS] [--list-players]

options:
  -h, --help                   show this help message and exit
  --name NAME, -n NAME         Nome do jogador
  --points POINTS, -p POINTS   Limite de pontos
  --list-players               Listar todos os jogadores
```

## Exemplos de uso
1. Quero descobrir se o LeBron James marcará mais do que 26.5 pontos

`python3 cli_app.py -n "LeBron James" -p 26.5`

2. Quero descobrir se o Kevin Durant vai marcar mais do que 24.5 pontos

`python3 cli_app.py -p 24.5 -n "Kevin Durant"`

3. Quero listar todos os jogadores na minha base de dados

`python3 cli_app.py --list-players`

## Considerações finais

A temporada de basquete atualmente (24/06/2024) terminou recentemente, então o modelo é treinado com todos os jogos da base de dados, com exceção do último jogo. O último jogo
assume um papel de "teste" final, num cenário hipotético em que o jogador ainda não tenha jogado seu último jogo ainda. Assim, conseguimos deixar o programa verossímil, uma vez
que não teremos jogos da liga até outubro de 2024.

[Kaggle utilizado para dados](https://www.kaggle.com/datasets/eduardopalmieri/5555555)

Trabalho feito por Joaquim Chianca em 2024.
