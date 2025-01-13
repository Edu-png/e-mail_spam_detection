# ✉️ Email Spam Classifier | SMS Spam Classifier ✉️

<p align="center">
  <a href="https://github.com/Edu-png">
    <img src="https://img.shields.io/badge/Autor-Eduardo%20Coqueiro-purple?style=flat&logo=github" alt="Autor">
  </a>
  <a href="mailto:eduardocoqueiro@gmail.com">
    <img src="https://img.shields.io/badge/Email-eduardocoqueiro%40gmail.com-purple?style=flat&logo=gmail" alt="Email">
  </a>
  <a href="https://linkedin.com/in/eduardocoqueiro/">
    <img src="https://img.shields.io/badge/LinkedIn-Eduardo%20Coqueiro-purple?style=flat&logo=linkedin" alt="LinkedIn">
  </a>
  <a href="https://kaggle.com/EduardoCoqueiro">
    <img src="https://img.shields.io/badge/Kaggle-Eduardo%20Coqueiro-blue?style=flat&logo=kaggle" alt="Kaggle">
  </a>
</p>

![CAPAS - PROJETOS (2)](https://github.com/user-attachments/assets/71e426af-daed-40a8-a7b5-1a1d83b76e43)

## Sumário 🎯


## 📄 Resumo  

Este projeto tem como objetivo desenvolver um **classificador de SPAM** para e-mails e SMS, utilizando técnicas de **Machine Learning**. O projeto envolve etapas como **análise exploratória de dados (EDA)**, **limpeza e pré-processamento de texto**, aplicação de **algoritmos de classificação**, e comparação entre diferentes modelos preditivos para identificar a abordagem mais eficaz. O dataset utilizado foi retirado do **Kaggle** e, ao final, a solução foi integrada com **Streamlit** para uma interface interativa de uso do modelo.

## ☀ Introdução  

O **Email Spam Classifier | SMS Spam Classifier** é um projeto focado na identificação de mensagens de **SPAM** em e-mails e SMS por meio de técnicas de **Machine Learning**. Utilizando bibliotecas como `Pandas`, `Scikit-learn`, e `NLTK`, o projeto realiza uma análise completa do dataset, passando por etapas de **limpeza de dados**, **pré-processamento de texto** e **treinamento de modelos preditivos**.  

O projeto busca fornecer uma abordagem prática para lidar com problemas de classificação de texto, identificando padrões que diferenciam mensagens legítimas (ham) de mensagens indesejadas (spam).  

### 🎯 Objetivo  

O objetivo principal deste projeto é desenvolver um sistema que:  
- **Identifique mensagens de SPAM** com alta precisão utilizando algoritmos de classificação.  
- **Aplique técnicas de NLP** (Processamento de Linguagem Natural) para transformar dados textuais em informações numéricas.  
- **Compare diferentes modelos de Machine Learning**, buscando aquele que oferece melhor desempenho.  
- **Implemente uma interface interativa** usando Streamlit para facilitar o uso do modelo por qualquer usuário.

## 🛠 Pipeline do Projeto  

A pipeline do projeto foi estruturada em etapas que vão desde a importação do dataset até a implementação de uma interface interativa para o classificador de SPAM. Cada etapa desempenha um papel fundamental na construção do modelo preditivo.

1. **Coleta de Dados**  
   - Dataset retirado do Kaggle com mensagens categorizadas como ham (legítimas) e spam (indesejadas).

2. **Limpeza de Dados**  
   - Remoção de colunas irrelevantes, conversão de rótulos para valores numéricos e remoção de duplicatas.

3. **Análise Exploratória (EDA)**  
   - Identificação da distribuição entre ham e spam, e geração de visualizações como gráficos e nuvens de palavras.

4. **Pré-processamento de Dados**  
   - Conversão para letras minúsculas, tokenização, remoção de caracteres especiais e aplicação de Stemming.

5. **Treinamento de Modelos**  
   - Teste de algoritmos como Naive Bayes, Random Forest, SVM e XGBoost com métricas de avaliação (acurácia e precisão).

6. **Comparação de Modelos**  
   - Seleção dos melhores modelos com base nos resultados de desempenho.

7. **Deploy com Streamlit**  
   - Criação de uma interface interativa para que o usuário classifique mensagens em tempo real.

## 🧪 Metodologia  

A metodologia aplicada no projeto **Email Spam Classifier | SMS Spam Classifier** foi organizada em etapas sequenciais para garantir uma análise eficiente, desde a coleta e limpeza dos dados até o treinamento de modelos de Machine Learning e a criação de uma interface interativa.

---

### 📂 1. Coleta de Dados  
O dataset utilizado foi retirado do **Kaggle** e contém mensagens categorizadas como **ham** (legítimas) e **spam** (indesejadas). A coleta foi feita diretamente via API utilizando um arquivo de autenticação do Kaggle. Após o download, os dados foram carregados em um DataFrame para análise.

---

### 🧹 2. Limpeza de Dados (Data Cleaning)  
Após a importação do dataset, foi realizada uma limpeza dos dados para garantir que as informações fossem consistentes e adequadas para análise.

**Operações realizadas:**  
- Remoção de colunas irrelevantes que não contribuíam para a análise.  
- Renomeação das colunas principais para facilitar a identificação das variáveis.  
- Conversão dos rótulos categóricos (ham e spam) em valores numéricos.  
- Identificação e remoção de registros duplicados, garantindo a unicidade das mensagens.

---

### 🔍 3. Análise Exploratória de Dados (EDA)  
Foi realizada uma análise exploratória para entender a distribuição dos dados e identificar padrões relevantes nas mensagens.

**Principais insights obtidos:**  
- O dataset contém 5169 mensagens, sendo 4516 classificadas como ham (legítimas) e 653 como spam (indesejadas).  
- As mensagens de spam tendem a ser mais longas do que as mensagens legítimas.  
- As palavras mais comuns em mensagens de spam incluem termos como "call", "free", "win", e "txt". Já nas mensagens legítimas, destacam-se palavras como "go", "come", "time", e "good".

**Visualizações geradas:**  
- Gráficos de pizza para mostrar a proporção entre mensagens ham e spam.  
- Nuvens de palavras (Word Clouds) para visualizar os termos mais frequentes em cada categoria.

---

### ✂ 4. Pré-processamento de Dados (Data Preprocessing)  
Para que os algoritmos de Machine Learning possam trabalhar com os dados textuais, foi necessário realizar várias transformações nas mensagens.

**Técnicas aplicadas:**  
- Conversão de todas as mensagens para letras minúsculas.  
- Tokenização das mensagens, separando-as em palavras individuais.  
- Remoção de caracteres especiais, stopwords (palavras comuns que não agregam valor) e pontuações.  
- Aplicação de Stemming, que reduz as palavras à sua raiz para facilitar o entendimento pelo modelo.

---

### 🤖 5. Treinamento do Modelo (Model Training)  
Após o pré-processamento, o texto foi transformado em matrizes numéricas usando técnicas como **CountVectorizer** e **TF-IDF Vectorizer**. Com isso, os dados foram divididos em conjunto de treino e teste para avaliar o desempenho dos modelos de classificação.

**Modelos testados:**  
- Naive Bayes (Multinomial, Gaussian e Bernoulli)  
- Random Forest  
- K-Nearest Neighbors (KNN)  
- Support Vector Machine (SVM)  
- XGBoost  

Cada modelo foi avaliado com base em métricas como **Acurácia**, **Precisão** e **Matriz de Confusão**.

---

### 📈 6. Comparação e Seleção de Modelos  
Foram comparados os resultados de diferentes modelos de Machine Learning para identificar aquele que apresentou o melhor desempenho.

**Principais resultados:**  
- O modelo **Multinomial Naive Bayes** apresentou um excelente equilíbrio entre acurácia e precisão.  
- O modelo **Random Forest** se destacou em precisão, sendo ideal para classificar mensagens de spam com alta confiança.  
- Modelos como **XGBoost** e **SVM** também apresentaram bons resultados, principalmente quando combinados em um **Voting Classifier**.

---

### 🖥 7. Deploy com Streamlit  
Por fim, o modelo foi integrado a uma interface interativa usando **Streamlit**. Essa aplicação permite que o usuário insira mensagens e receba uma classificação imediata, indicando se a mensagem é spam ou não.

**Funcionalidades da interface:**  
- Campo de entrada para texto livre.  
- Classificação da mensagem como ham ou spam.  
- Exibição da probabilidade de a mensagem ser spam, utilizando um modelo de votação combinado.

## 📈 Resultados e Conclusões  

### 📊 1. Proporção de Mensagens Ham e Spam  
O gráfico de pizza a seguir apresenta a distribuição das mensagens no dataset, destacando que **87,37% das mensagens** são classificadas como ham (legítimas) e **12,63% como spam**.

![1](https://github.com/user-attachments/assets/5e6bef75-fd88-4adb-83a0-b986c4da1bb2)

---

### 🖋 2. Distribuição do Número de Caracteres  
O gráfico de histograma mostra que as mensagens de spam tendem a ter mais caracteres em comparação com as mensagens legítimas.

![2](https://github.com/user-attachments/assets/78d01b26-33ea-4adb-beaa-1e6258a3e2b2)

---

### 🖋 3. Distribuição do Número de Palavras  
O histograma a seguir apresenta a contagem de palavras em mensagens ham e spam. Assim como na análise de caracteres, as mensagens de spam apresentam uma maior quantidade de palavras.

![3](https://github.com/user-attachments/assets/c56b48d0-bffd-4ecb-a2cb-914dd0ecc08c)

---

### 🖋 4. Distribuição do Número de Sentenças  
O histograma mostra a quantidade de sentenças nas mensagens. As mensagens de spam tendem a ter mais sentenças que as mensagens ham.

![4](https://github.com/user-attachments/assets/8b081a4b-9eda-4150-9dd8-c3a5dc800ce2)

---

### 🔍 5. Gráfico de Correlação Entre Variáveis  
O gráfico de pares a seguir mostra a relação entre as variáveis criadas (número de caracteres, palavras e sentenças) e a variável alvo (ham ou spam). É possível notar que mensagens mais longas estão mais associadas a spam.

![5](https://github.com/user-attachments/assets/e26f29d1-7707-4f6d-9aec-4f2bc4078bf8)

---

### 🔥 6. Mapa de Correlação  
O heatmap abaixo destaca a correlação entre as variáveis numéricas do dataset. Podemos observar uma alta correlação entre o número de caracteres, palavras e sentenças.

![6](https://github.com/user-attachments/assets/4423a988-12a9-4136-893a-5b5b4d8d30d8)

---

### ☁️ 7. Nuvem de Palavras (Spam)  
A nuvem de palavras para mensagens spam revela termos como **"call"**, **"free"**, **"txt"** e **"win"**, que são comuns em mensagens de spam que oferecem prêmios falsos e solicitam respostas rápidas.

![7](https://github.com/user-attachments/assets/5e39216e-7ebb-4c11-8fa6-a35ee82ce240)

---

### ☁️ 8. Nuvem de Palavras (Ham)  
A nuvem de palavras para mensagens ham mostra termos mais comuns em conversas legítimas, como **"go"**, **"come"**, **"time"**, **"good"** e **"love"**.

![8](https://github.com/user-attachments/assets/ffef36a7-0519-4194-8aa7-06b8a802351e)

---

### 📋 9. Palavras Mais Frequentes em Mensagens Spam  
O gráfico de barras apresenta as **30 palavras mais frequentes** em mensagens de spam, destacando termos relacionados a prêmios, promoções e solicitações urgentes.

![9](https://github.com/user-attachments/assets/041adb46-b1d0-4542-9256-750383a8a3b3)

---

### 📋 10. Palavras Mais Frequentes em Mensagens Ham  
O gráfico de barras a seguir apresenta as **30 palavras mais frequentes** em mensagens legítimas (ham), com destaque para palavras comuns em conversas do dia a dia, como **"u"**, **"go"**, **"get"**, e **"like"**.

![10](https://github.com/user-attachments/assets/cc298df5-3509-4d3c-a3b7-7792c279080c)

---

### 🤖 11. Comparação de Algoritmos - Acurácia e Precisão  
O gráfico compara diversos algoritmos de classificação utilizados no projeto, destacando suas **métricas de acurácia e precisão**. Algoritmos como **Naive Bayes** e **Random Forest** obtiveram excelentes resultados.

![11](https://github.com/user-attachments/assets/7d1654f1-1ffa-4259-9964-aa0588edea17)

---

### 📊 12. Comparação de Performance de Modelos  
Este gráfico apresenta uma **comparação detalhada de métricas** para cada algoritmo utilizado, considerando diferentes configurações e pré-processamentos aplicados.

![12](https://github.com/user-attachments/assets/d4f8f50b-adfb-409e-a6a0-4af613a17afd)

---

### 🔍 13. Interface de Usuário - Classificação de Spam  
A imagem abaixo mostra a **interface interativa** desenvolvida com **Streamlit**, onde o usuário pode inserir uma mensagem e receber a classificação como **spam** ou **not spam** em tempo real.

<img width="739" alt="13" src="https://github.com/user-attachments/assets/5e13348c-7024-4399-af02-95d33e7025a2" />

---

### 🔍 14. Interface de Usuário - Classificação de Not Spam  
Outra visualização da interface interativa, mostrando uma mensagem legítima sendo classificada como **not spam**.

<img width="442" alt="14" src="https://github.com/user-attachments/assets/d3f8cd08-c4af-4fb4-bbab-ea63c4bd90b5" />

## 🚀 Considerações Finais  

O projeto **Email/SMS Spam Classifier** demonstra como técnicas de **Machine Learning** podem ser aplicadas para resolver problemas de classificação de texto, especificamente na detecção de mensagens de spam. A construção de um pipeline completo, desde a coleta de dados até a criação de uma interface interativa, permite que o modelo seja utilizado de forma prática por usuários finais.

### 🧩 **Principais Aprendizados**  
- A importância do **pré-processamento de dados textuais** para garantir que os modelos de Machine Learning possam interpretar corretamente as mensagens.  
- A comparação de diferentes algoritmos de classificação, como **Naive Bayes**, **Random Forest** e **SVM**, mostrando como cada um se comporta com dados textuais.  
- O uso de **métricas de avaliação**, como acurácia, precisão e matriz de confusão, para medir o desempenho dos modelos.  
- A criação de uma **interface interativa com Streamlit**, tornando o modelo acessível para usuários sem conhecimentos técnicos.

### 📋 **Pontos de Destaque do Projeto**  
- **Precisão elevada na detecção de spam:** Modelos como Naive Bayes e Random Forest apresentaram excelentes resultados nas métricas de avaliação.  
- **Pipeline completo de Machine Learning:** Desde a análise exploratória de dados até o deploy do modelo em uma aplicação interativa.  
- **Uso de técnicas de NLP (Processamento de Linguagem Natural):** Como tokenização, remoção de stopwords e stemming para melhorar o desempenho do modelo.

### 🔧 **Possíveis Melhorias Futuras**  
1. **Aprimorar o pré-processamento:**  
   - Explorar outras técnicas de transformação de texto, como **Lemmatization** e **Word Embeddings** (ex: Word2Vec).  
2. **Implementar modelos avançados:**  
   - Testar algoritmos mais robustos, como **Transformers** e **Deep Learning** com redes neurais recorrentes (RNNs).  
3. **Atualização do dataset:**  
   - Adicionar novos dados para manter o modelo atualizado com padrões recentes de spam.  
4. **Integração com APIs:**  
   - Criar uma API para integrar o modelo em outras aplicações, como sistemas de e-mails ou aplicativos de mensagens.

### 📈 **Impacto do Projeto**  
Este projeto oferece uma solução prática para o problema de spam, que continua sendo um desafio em comunicações digitais. Com a implementação de um classificador eficiente, é possível minimizar o recebimento de mensagens indesejadas, protegendo usuários de golpes e fraudes.

---

Com este projeto, foi possível explorar técnicas fundamentais de Machine Learning e NLP, além de reforçar a importância da documentação e da criação de interfaces amigáveis para aplicações reais.

<div align="center">
  <img src="https://github.com/user-attachments/assets/54afb33c-97be-40b6-8c96-0f12852e946f" alt="thank-you" width="500">
</div>

## 📞 Contato
- **LinkedIn:** [Eduardo Coqueiro](https://www.linkedin.com/in/eduardocoqueiro/)
- **Site:** [Eduardo Coqueiro](https://dataguy.my.canva.site/eduardo-coqueiro)
- **Kaggle:** [Eduardo Coqueiro](https://www.kaggle.com/eduardocoqueiro)

