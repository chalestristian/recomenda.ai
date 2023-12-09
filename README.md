<div align="center">  
  <p>
    <img src="readme_img/logo.png" alt="Logo" width="80" height="80">
  </p>
  <h2>RECOMENDA.AI</h2>
  <p>
    <span>Modelo inteligente de recomendação de conteúdo.</span>
    <br/>
    <br/>
    <a href="/modelos/"><strong>Explorar source code</strong></a>
    <br/>
    <br/>
    <span>Bem-vindo ao <b>recomenda.ai</b><span>
    <br/>
  </p>
  
  <details>      
  <summary><b>Sumário</b></summary>

  [Sobre o Projeto](#sobre)

  [Dataset](#dataset)

  [Design](#design)

  [Pipeline](#pipeline)

  [Relatorio](#artefatos)

  [Instalar & Executar](#instalar)

  [Desenvolvido Com](#desenvolvidocom)

  [Considerações Finais](#consideracoesfinais)

  [Fontes](#fontes)

  </details>
  <br/>
</div>

# Sobre o projeto
<div align="center" id="sobre">

![Product Name ScreenShot][product-screenshot] 

</div>

<div>
  <span>
    Sua empresa foi contratada pela Netflix para construir o novo sistema de recomendação da plataforma de streaming mais famosa do mundo.
    A área de negócio responsável na Netflix fez algumas observações na reunião de Kick-Off que deverão ser consideradas durante o processo:
  </span> 


  <br/>  
  <br/> 

  <b>Considerações:</b>

  * A recomendação deve ocorrer de duas formas. 
    * [x] A primeira deve ser uma recomendação baseada no histórico do usuário.

      - [item_based_collaborative_filtering](/modelos/item_based_collaborative_filtering/)

    * [x] A segunda deve ser uma recomendação baseada no perfil pessoal do usuário.

      - [content_based_filtering](/modelos/content_based_filtering/)


  <br/>
  <b>Exigências:</b>

  * [x] O desenvolvimento deve ser feito em Python (versão 3.8 ou superior)
  * [x] O ambiente de desenvolvimento deve ser capaz de ser reproduzido a qualquer momento.
  * [x] O dataset será fornecido pela Netflix.
  * [x] Sua equipe deverá fornecer insights relevantes sobre a base de dados:
    * Estes insights também serão utilizados pela Netflix para melhorar seu processo de Engenharia de Dados. 
    * Para seu time, os insights serão os guias no desenho dos modelos de recomendação.
  * [x] Deverão ser criados pelo menos 2 modelos com abordagens diferentes.
    * [x] [item_based_collaborative_filtering](/modelos/item_based_collaborative_filtering/)
    * [x] [content_based_filtering](/modelos/content_based_filtering/)

  * [x] Todas as decisões de modelagem, definição de hiperparâmetros e etc devem ser documentadas e justificadas do porquê da utilização.
  * [x] Deverá ser apresentado relatório completo do desempenho dos modelos treinados, considerando métricas relevantes para a análise destes desempenhos.
  * [x] A equipe deverá criar um pipeline teórico de deploy completo do projeto em alguma plataforma de nuvem (ex: Google Cloud Platform, AWS, Microsoft Azure).
  * [x] O Projeto deverá ser publicado em repositório GIT.
  <br/>
</div>

# Dataset
<div id="dataset">

  O [dataset](/dataset/) fornecido pela Netflix contém informações relevantes e está dividido em:
  - [movies](/dataset/movies.csv)
  - [ratings](/dataset/ratings.csv)
  
  onde, movies contém informações relevantes sobre o filme sendo título e gênero, e ratings contendo informações referente as avaliações das obras.

  Para além dos insights fornecidos abaixo, o dataset pode ser considerado coerente. Apesar de não ser tão completo e abrangente, podemos afirmar que os dados são precisos, consistentes, padronizados, tendo como resultado pouco esforço necessário no pré-processamento dos dados.

  <br/>

  ### Insights

  Sugestões de melhoria detectados durante a preparação dos dados:
  * Movies:
    - **Título e Ano na mesma coluna:**
        
        No dataset, o título da obra e o ano estão na mesma coluna, separadas por parênteses como por exemplo:
        ````
        Bushwhacked (1995)
        ````
        Separar o título e o ano em colunas específicas ajuda a manter a consistência da base, melhora o processo de preparação dos dados retirando a necessidade de tratar o campo título/ano, e pode também ajudar na performance dos demais serviços da companhia que consomem esse dado.

        Considerando ainda que existem títulos onde há parênteses no nome, como por exemplo:

        ````
        Eat Drink Man Woman (Yin shi nan nu) (1994)
        ````

        A separação desses dados se torna ainda mais crucial, evitando que títulos sejam deformados caso a única validação no pré-processamento seja ignorar dados entre parêntese.

    - **Padronização na nomenclatura dos gêneros:**

        Os gêneros relacionados a Ficção Científica (Science Fiction) e Filme Negro (Noir) são os únicos abreviados com o simbolo - na base:
        ````
        Sci-Fi | Film-Noir
        ````
        Por fugirem do padrão e com o objetivo de simplificar a análise e garantir consistência nos dados, a sugestão seria que as nomenclaturas fossem:
        ````
        SciFi | Noir
        ````
    - **Gêneros ausentes:**

        Quando um filme não possui o gênero especificado, na base a coluna gênero recebe o termo:
        ````
        (no genres listed)
        ````
        O ideal seria deixar a coluna nula. A validação por nulo é bem mais simples e é uma rotina padrão na análise de dados, facilitando a validação nos serviços que consomem esse dado, e também o pré-processamento descartando a necessidade de procurar por um termo específico.

    - **Ausência de dados gerais:**
      Em sistemas de streaming, comumente os usuários podem configurar/tender (a) certas preferências que podem incluir:
      
        - Classificação indicativa
        - Elenco
        - Duração
        - País de origem

      Essas informações poderiam enriquecer a análise de dados e resultaria em recomendações mais acuradas e precisas, porém, são informações que não estão disponíveis nas bases fornecidas.
    
    Não foram identificados pontos de melhorias significativos na base ratings.

  <br/>
</div>


# Design
<div id="design">

### Modelos:

No cenário de recomendação de filmes, com base nos conjuntos de dados fornecidos que incluem títulos, gêneros e avaliações dos usuários, várias abordagens foram consideradas, e optamos pelos modelos:

[Filtragem Colaborativa Baseada em Itens(Item-Based Collaborative Filtering)](/modelos/item_based_collaborative_filtering/)

[Filtragem Baseada em Conteúdo(Content-Based Filtering)](/modelos/content_based_filtering/)

Ambos os modelos possuem vantagens específicas baseadas no cenário de uso, e esses pontos foram considerados para a tomada de decisão:

**Filtragem Colaborativa Baseada em Itens:**

   - **Vantagens:**
     - Eficaz em situações onde as preferências do usuário são dinâmicas ou podem mudar com o tempo. 
     - Pode lidar com a popularidade e dinâmica de itens novos, pois se baseia nas interações entre usuários e itens.
     - Não requer informações detalhadas sobre os itens.

   - **Cenários de uso:**
     - Quando há um grande conjunto de dados de interações usuário-item.
     - Quando as preferências dos usuários são influenciadas pelas escolhas de usuários semelhantes.

**Filtragem Baseada em Conteúdo:**

   - **Vantagens:**
     - Eficaz quando há informações detalhadas sobre os itens.
     - Pode lidar bem com a novidade, sugerindo itens com base em características intrínsecas.
     - Pode ser mais explicativo, pois recomenda com base em características específicas dos itens.

   - **Cenários de uso:**
     - Quando há informações detalhadas sobre os itens, como descrições, gêneros, diretores, etc.
     - Quando as preferências dos usuários estão fortemente ligadas às características dos itens.

O detalhamento acima resume o motivo da nossa escolha nos modelos apresentados. Com a filtragem colaborativa baseada em itens as avaliações são consideradas, são dados que mudam com o tempo, mudam conforme a interação dos usuários e as preferências são influenciadas pela escolha de usuários semelhantes. Já a filtragem baseada em conteúdo exige informações complementares como os gêneros dos filmes, fazendo assim a recomendação com base na característica específica do item, característica essas que o usuário já demonstrou interesse.


### Hiperparâmetros:

Buscando uma abordagem mais orientada ao cliente, optamos por disponibilizar uma ampla variedade de possibilidades e combinações de hiperparâmetros. Essa flexibilidade tem como objetivo atender às diversas necessidades do negócio, proporcionando uma experiência mais rica e adaptada às preferências individuais ou coletivas no cenário atual. Reconhecemos que a base de dados está sujeita a mudanças e crescimento, e novas regras de negócios podem surgir. A intenção por trás dessa escolha é dotar o sistema de recomendações da máxima flexibilidade possível, permitindo uma resposta ágil a essas mudanças em prazos reduzidos e com o mínimo esforço necessário.

Cada um dos modelos foi configurado com hiperparâmetros específicos, dando ao cliente a liberdade de escolher aquele que melhor se adequa às suas necessidades. Contudo, estabelecemos valores padrões para casos em que a especificação não esteja presente. Essa abordagem visa simplificar o processo de configuração, garantindo que o sistema continue operando de maneira eficiente mesmo quando uma escolha personalizada não for feita.


### Filtragem Colaborativa Baseada em Itens:

  - **n_neighbors:**
    
    - *Especificações:*
      - Aceita valores a partir de 3 até o tamanho da lista (valor padrão: 9).
      - Aceita apenas valores ímpares para evitar empates nas votações.
      - Caso inserido valores pares, o arredondamento será realizado para baixo (-1).
    
    - *Definições:*
      - Define o número de vizinhos considerados durante a recomendação. O algoritmo k-NN recomenda itens com base na votação dos vizinhos mais próximos. O número de vizinhos afeta a influência de pontos de dados próximos na recomendação. Valores mais altos podem levar a recomendações mais conservadoras, enquanto valores mais baixos podem ser mais sensíveis a variações nos dados.

  - **metric:**

    - *Especificações:*
      - Aceita como valores: cosine, euclidean, manhattan (valor padrão: cosine).

    - *Definições:*
      - Define a métrica de distância utilizada para calcular a distância entre pontos no espaço. As opções são:
        
        - *cosine*: Mede o cosseno do ângulo entre dois vetores no espaço. No contexto de recomendação, os vetores representam os perfis de avaliação dos usuários. Dois itens ou usuários com avaliações semelhantes, mesmo que em escalas diferentes, terão uma alta similaridade de cosseno.

        - *euclidean*:  A distância euclidiana é a distância geométrica direta entre dois pontos em um espaço. No contexto de recomendação, representa a dissimilaridade entre avaliações de usuários ou itens. Avaliações mais distantes em termos de magnitude terão uma distância euclidiana maior.

        - *manhattan*: A distância de Manhattan é a soma das diferenças absolutas entre as coordenadas dos pontos. Em um contexto de recomendação, é uma métrica de dissimilaridade entre avaliações. É menos sensível a diferenças em uma dimensão específica em comparação com a euclidiana.

  - **algorithm:**

    - *Especificações:*
      - Aceita como valores:  brute, ball_tree, kd_tree, auto (valor padrão: brute).
    
    - *Definições:*
      - Define o algoritmo utilizado para calcular os vizinhos mais próximos. As opções são:

        - *brute*: Calcula diretamente a distância entre todos os pontos no espaço de características, identificando os vizinhos mais próximos. É eficaz para conjuntos de dados de pequena a média escala, mas pode se tornar computacionalmente caro para grandes conjuntos de dados.
        
        - *ball_tree*: Cria uma estrutura de árvore para representar o espaço de características, organizando os pontos em regiões esféricas. É eficiente para conjuntos de dados de alta dimensionalidade, mas pode exigir mais recursos de memória durante a construção da árvore.

        - *kd_tree*: Organiza os pontos em uma estrutura de árvore binária, dividindo recursivamente o espaço em regiões k-dimensionais.
          É eficiente para conjuntos de dados de baixa a média dimensionalidade, mas pode não ser ideal para conjuntos de dados de alta dimensionalidade.
        - *auto*: Organiza os pontos em uma estrutura de árvore binária, dividindo recursivamente o espaço em regiões k-dimensionais. É eficiente para conjuntos de dados de baixa a média dimensionalidade, mas pode não ser ideal para conjuntos de dados de alta dimensionalidade.

### Filtragem Baseada em Conteúdo:

  - **stopwords**
  
    - *Especificações:*
      - Aceita como valores:  english, none (valor padrão: english).
    
    - *Definições:*
      - Controla se e quais stopwords (palavras irrelevantes, como "and", "the", etc.) devem ser removidas durante o processamento de texto. A escolha entre "none" e "english" determina se stopwords são removidas ou não. No contexto de gêneros de filmes, palavras como "and", "the", etc., podem não ser informativas para distinguir diferentes gêneros.

  - **metric**

    - *Especificações:*
      - Aceita como valores:  linear_kernel, cosine_similarity (valor padrão: linear_kernel).

    - *Definições:*
      - Controla a métrica utilizada para calcular a similaridade entre itens. As opções são:

        - *linear_kernel*: É mais influenciado pela magnitude dos vetores de características, ou seja, gêneros com uma maior presença relativa podem ter um impacto mais significativo na similaridade.

        - *cosine_similarity*: É mais focado na orientação e é insensível à magnitude, ou seja, a presença absoluta de um gênero não influenciará tanto quanto a direção geral dos vetores de características.
      
  - **how_many**

    - *Especificações:*
      - Aceita valores a partir de 3 até o tamanho da lista (valor padrão: 5).

    - *Definições:*
      - Define a quantidade de recomendações a serem geradas. A Quantidade de recomendações pode afetar a experiência do usuário. Valores muito baixos podem não fornecer diversidade, enquanto valores muito altos podem sobrecarregar o usuário.

  <br/>
</div>

# Pipeline
<div id="pipeline">

Pipeline teórico de deploy:

![Product Deploy][product-deploy] 

Em resumo, esse modelo de deploy visa otimizar a entrega contínua, promover a automação em todas as etapas e garantir uma infraestrutura escalável e resiliente para os serviços de recomendações. Adotando essa abordagem, as equipes de desenvolvimento podem garantir uma implementação confiável, rápida e eficiente.


  <br/>
<div/>

# Relatório
<div id="artefatos">

[Relatório de desempenho dos modelos](https://docs.google.com/document/d/1-QmSaHaDGDmoHfN2vV1antKq7YPRROpmvfZnWiRDsGA/edit?usp=sharing)
  <br/>
</div>

# Instalar & Executar
<div id="instalar">

### Guia de Execução Local com Docker Compose

Este guia fornece instruções passo a passo sobre como executar a aplicação localmente usando o Docker Compose.

### Pré-requisitos

Certifique-se de ter os seguintes pré-requisitos instalados em sua máquina:

- [Docker](https://www.docker.com/get-started)

### Passos para Execução Local

#### 1. Clone o Repositório

```
git clone https://github.com/chalestristian/recomenda.ai.git
```

```
cd recomenda.ai/modelos
```

#### 2. Construa e Inicie os Contêineres

Execute o seguinte comando para construir e iniciar os contêineres da aplicação (certifique-se de que o Docker Desktop esteja aberto):

```
docker compose up --build
```

#### 3. Acesse a Aplicação

Uma vez que os contêineres estejam em execução, a aplicação deve estar acessível em:

- [http://localhost:5000](http://localhost:5000)

#### 4. Parar e Limpar

Para parar os contêineres e limpar os recursos, execute:

```
docker compose down
```

Isso encerrará a execução da aplicação e removerá os contêineres.

#### Problemas Comuns:

- **Porta Ocupada:** Se a porta 5000 já estiver em uso, ajuste a porta no arquivo `docker-compose.yml` ou encerre o processo que está usando a porta.

- **Erros na Compilação:** Certifique-se de que todas as dependências estejam instaladas e que o ambiente esteja configurado corretamente.

</br>

</div>


# Desenvolvido com
<div id="desenvolvidocom">

  [![Python][Python]][Python-url]

  <br/>
</div>

# Considerações finais
<div id="consideracoesfinais">

### Trabalho desenvolvido por: Thales Cristian e Neuber Tavares

É com grande satisfação que concluímos este projeto de Modelos de Recomendações, desenvolvido com empenho e dedicação ao longo da Unidade Curricular do curso de Ciências Da Computação - UNIBH.

Agradecemos ao professor Marco Calijorne por nos desafiar e orientar ao longo desse percurso, fornecendo insights valiosos e estimulando nossa busca pelo conhecimento.
  <br>
</div>

# Fontes
<div id="fontes">

  Fontes de pesquisas consultadas:

  * [Build a Recommendation Engine With Collaborative Filtering](https://realpython.com/build-recommendation-engine-collaborative-filtering/#the-dataset)

  * [Item-based Collaborative Filtering Recommendation Algorithms](https://www.researchgate.net/publication/2369002_Item-based_Collaborative_Filtering_Recommendation_Algorithms)

  * [How to Build a Recommendation System in Python](https://365datascience.com/tutorials/how-to-build-recommendation-system-in-python/)

  <br/>
</div>


<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: readme_img/screenshot.png
[product-deploy]: readme_img/deploy/pipeline-deploy.png

[Python]: https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/