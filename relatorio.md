# Relatório 
Aluno: Joaquim Chianca
## Introdução
As apostas esportivas têm uma história longa no Brasil, começando no período colonial com jogos trazidos pelos europeus. Ao longo dos anos, o mercado passou por diversas mudanças, com momentos de legalização e proibição. Atualmente, as apostas esportivas estão em alta, especialmente nas plataformas online, que oferecem uma grande variedade de opções para os brasileiros, de futebol a reality shows. Esse crescimento é impulsionado pela tecnologia digital, que trouxe novas formas de interagir com o mercado.

Machine Learning (ML), ou aprendizado de máquina, é uma área da inteligência artificial que permite que sistemas aprendam a partir de dados e tomem decisões automaticamente. Desde os primeiros testes nos anos 1950, o ML evoluiu muito e hoje é utilizado em diversas aplicações, como recomendações de conteúdo e carros autônomos. O ML é essencial para analisar grandes volumes de dados e identificar padrões sem intervenção humana, tornando-se cada vez mais presente em nossas vidas.

A união entre apostas esportivas e Machine Learning está transformando o setor. No mercado de apostas, ML é usado para criar modelos preditivos que ajudam os apostadores a fazer previsões mais precisas sobre os resultados dos jogos. Algoritmos analisam dados históricos e desempenho dos jogadores, permitindo uma análise mais detalhada das probabilidades.

Este projeto visa utilizar Machine Learning para prever a quantidade de pontos que um jogador da NBA, a liga de basquete mais famosa do mundo, fará em uma partida. Focando no desempenho de LeBron James, o objetivo é desenvolver modelos que possam prever com precisão se ele marcará mais ou menos que 26.5 pontos em um jogo (isso é um exemplo, o modelo pode ser usado com qualquer jogador da liga e com qualquer quantidade de pontos). Essa análise busca aplicar técnicas de aprendizado de máquina em um contexto esportivo, oferecendo insights sobre o desempenho de jogadores e auxiliando em decisões baseadas em dados.

## Metodologia
A pergunta motivadora do estudo: **O Lebron James ultrapassa ou não a quantidade de 26.5 pontos na próxima partida?**

Essa pergunta caracteriza como um problema de classificação, já que o jogador estará em um grupo (ultrapassa a quantidade de pontos) ou noutro (não ultrapassa a quantidade de pontos definida).

Para tal, usaremos algoritmos de treinamento destinados à criação de modelos que abordam esse problema de classifição. A ideia é usar um [conjunto de dados](https://www.kaggle.com/datasets/eduardopalmieri/5555555) disponibilizados no Kaggle.

O projeto será feito no ambiente do [Jupyter Notebook](https://www.alura.com.br/artigos/conhecendo-o-jupyter-notebook?srsltid=AfmBOoqcqW3XyAtJpAk5TAKvH8tokP0Mb89rS8GJZ_CmG5OFFe7F0j6P), portanto, são utilizadas bibliotecas conceituadas da linguagem de programação Python.

### Condução do projeto
O projeto segue os seguintes passos:

1. Limpeza e pré-processamento dos dados
2. Treinamento de modelos a partir de 4 algoritmos e combinação de modelos em um Ensemble
3. Visualização e interpretação dos resultados

Além disso, o modelo com melhor desempenho é utilizado em um programa escrito em Python, para que o modelo seja utilizado por um usuário final, com intuito de responder a mesma pergunta motivadora para os demais jogadores e com quaisquer limite de pontos estabelecido.

### Limpeza e tratamento dos dados
O dataset possui informações sobre todas partidas de todos os jogadores da temporada 23/24 da NBA. Dentre algumas informações temos pontos na partida, arremessos tentados (de 2 e 3 pontos), rebotes, assistências, roubos de bola, tocos e eficiência de um jogador. 

Os dados foram lidos por meio da biblioteca `pandas` e a limpeza deles seguem a seguinte lógica:

- Remoção de jogadores com menos de 16 jogos, já que uma temporada regular de basquete possui 82 jogos.
- Remoção de colunas irrelevantes, como data do jogo e time de um jogador, pois não influenciam de fato na pontuação de um jogador em quadra. 

### Algoritmos utilizados
- **k-Nearest Neighbors (kNN):** um algoritmo de aprendizado de máquina supervisionado que não faz suposições sobre a distribuição dos dados. Baseia-se na ideia de que pontos de dados semelhantes estão próximos um do outro. O KNN usa a proximidade para classificar ou prever o valor de um novo ponto de dados, considerando os 'k' pontos mais próximos.
- **Árvores de Decisão:** algoritmo preditivo que utiliza uma estrutura de árvore ou lógica condicional (if-else) para tomar decisões. Começando pela raiz da árvore, cada nível representa uma decisão que divide os dados com base em um critério específico, conduzindo a folhas que representam as classificações ou previsões finais.
- **Random Forest:** [ensemble](https://medium.com/dados-e-saude/machine-learning-e-ensembles-780f3a8aa36d) de árvores de decisão. Funciona treinando múltiplas árvores de decisão com subconjuntos dos dados de treinamento e então agregando suas previsões. Esse método melhora a precisão e controla o overfitting, sendo eficaz para grandes conjuntos de dados.
- **Gradient Boost Machine (GBM):** técnica de boosting que constrói modelos de forma sequencial, onde cada novo modelo tenta corrigir os erros do modelo anterior. Baseia-se em otimização gradiente, ajustando-se iterativamente para minimizar uma função de perda.

Por fim, é feita uma tentativa de combinar os vários modelos treinados num processo de criação de Ensemble (combinação de vários modelos), usando o `VotingClassifier` da biblioteca `sklearn`. O VotingClassifier é um modelo que combina as previsões de diversos modelos para determinar a saída final com base na classe que mais frequentemente é escolhida pelos modelos individuais.

### Visualização de respostas
Visualizar números e texto não é a maneira mais intuitiva de entender informação para os humanos, portanto, foram criados gráficos utilizando a biblioteca `matplotlib.pyplot` do ecossistema Python.

### Métricas de avaliação dos modelos
Os modelos são avaliados a partir de quatro principais métricas: acurácia, precisão, recall e F1-Score. Essas métricas ajudam a medir o desempenho dos algoritmos de machine learning no contexto do projeto, que busca prever se um jogador da NBA, como LeBron James, fará mais de 26.5 pontos em uma partida.

No projeto, o resultado previsto pode ser classificado como True (quando o modelo prevê que o jogador fará mais de 26.5 pontos) ou False (quando o modelo prevê que o jogador fará menos de 26.5 pontos).

- **Acurácia**: Representa a proporção de todas as previsões corretas em relação ao total de previsões feitas. Ou seja, quantas vezes o modelo acertou, tanto quando previu que LeBron faria mais de 26.5 pontos, quanto quando previu que ele não ultrapassaria essa marca.

- **Precisão**: Mede a confiabilidade das previsões de que LeBron fará mais de 26.5 pontos. Ela responde à pergunta: “Das vezes que o modelo previu que ele faria mais de 26.5 pontos, quantas vezes isso realmente aconteceu?”.

- **Recall**: Avalia a capacidade do modelo de identificar corretamente os jogos em que LeBron realmente marcou mais de 26.5 pontos. Em outras palavras, das vezes que ele de fato ultrapassou essa pontuação, quantas vezes o modelo foi capaz de prever corretamente?

- **F1-Score**: É a média harmônica entre precisão e recall. O F1-Score é importante para equilibrar essas duas métricas, especialmente em situações onde o modelo pode errar ao prever tanto para mais quanto para menos. Um F1-Score alto indica que o modelo tem um bom desempenho geral.

## Resultados
### K-Nearest Neighbors (kNN)
Para este algoritmo, foram criados diversos modelos, buscando entender qual seria o número ótimo de vizinhos (k) para cada métrica (Euclidiana ou Manhattan). Feito isso, consideramos a melhor acurácia dentre os números testados (3, 5, 7, 9, 11, 13).

O algoritmo K-Nearest Neighbors (KNN) é uma abordagem simples e intuitiva, especialmente eficaz em problemas de classificação, como no caso deste projeto. Os resultados obtidos para o KNN com as distâncias Euclidean e Manhattan, ambos com acurácia de 87.50%, mostram que este algoritmo pode ser uma escolha robusta para a tarefa de prever se LeBron James marcará mais de 26.5 pontos em uma partida.

Os pontos fortes do KNN ficam evidentes na alta acurácia e precisão para a classe "True" (quando LeBron ultrapassa os 26.5 pontos), com valores de 1.00 em ambos os relatórios de classificação. Isso indica que, quando o KNN prevê que LeBron ultrapassará a marca, ele acerta todas as vezes, o que é crucial para decisões onde esses acertos são prioritários. Além disso, a simplicidade do algoritmo e sua natureza não-paramétrica, que não requer suposições sobre a distribuição dos dados, contribuem para sua eficácia em diferentes contextos de dados.

No entanto, o KNN também apresenta fraquezas. O recall para a classe "True" é relativamente baixo, em 0.62, o que significa que o modelo deixa de identificar corretamente 38% dos casos em que LeBron realmente faz mais de 26.5 pontos. Esse aspecto é crucial, pois em cenários onde é importante não perder nenhuma ocorrência positiva, essa limitação pode ser um problema. Além disso, o KNN pode se tornar ineficiente em grandes conjuntos de dados, pois ele precisa calcular a distância de cada ponto de teste em relação a todos os pontos de treino, o que pode levar a um alto custo computacional.

Assim, enquanto o KNN apresenta bons resultados em termos de acurácia e precisão, sua limitação em recall e o custo computacional em cenários com grandes volumes de dados podem ser fatores a considerar ao decidir sobre o uso desse algoritmo em problemas similares.



## Conclusão

## Referências
- [História das apostas no Brasil](https://ibjr.org/historia-apostas-brasil/)
- [Machine Learning: Conceitos, definição e mais](https://blog.neoway.com.br/machine-learning/)