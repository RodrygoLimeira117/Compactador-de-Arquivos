# Compactador de Arquivos

Projeto desenvolvido para análise e comparação de algoritmos de compressão de arquivos utilizando Python. O sistema implementa compressão com LZW e Zlib, além de ferramentas auxiliares para geração de arquivos de teste, criação de GIFs e visualização gráfica de desempenho.

## 📌 Objetivo

O projeto tem como objetivo estudar o desempenho de diferentes técnicas de compressão, analisando fatores como:

* Tempo de execução
* Consumo de memória
* Redução de tamanho dos arquivos
* Eficiência dos algoritmos

Além disso, o projeto também inclui ferramentas para geração de dados e visualização dos resultados obtidos.

---

## 🚀 Tecnologias Utilizadas

* Python 3
* Zlib
* Pickle
* Tracemalloc
* Matplotlib
* Pillow (PIL)
* ImageIO

---

## 📂 Estrutura do Projeto

```bash
Projeto_Final/
│
├── Descompactador_arquivos.py
├── Gerador_Gif.py
├── Gerador_texto.py
└── grafico.py
```

---

## 📖 Descrição dos Arquivos

### 📄 `Descompactador_arquivos.py`

Responsável pela compressão e descompressão de arquivos utilizando:

* Algoritmo LZW
* Biblioteca Zlib

Também realiza:

* Medição de tempo de execução
* Medição de uso de memória
* Salvamento e carregamento de arquivos comprimidos

#### Funcionalidades:

* Compressão de texto
* Descompressão
* Benchmark de desempenho
* Serialização com Pickle

---

### 🖼️ `Gerador_Gif.py`

Cria GIFs a partir de uma sequência de imagens.

#### Funcionalidades:

* Leitura automática de imagens em uma pasta
* Conversão para GIF animado
* Controle de duração dos frames

---

### 📝 `Gerador_texto.py`

Gera arquivos de texto aleatórios para testes de compressão.

#### Funcionalidades:

* Criação de palavras aleatórias
* Geração de arquivos grandes para benchmark
* Simulação de cenários reais de compressão

---

### 📊 `grafico.py`

Gera gráficos comparativos utilizando Matplotlib.

#### Métricas analisadas:

* Tempo médio de compressão
* Redução média de tamanho
* Consumo médio de memória

---

## ⚙️ Como Executar

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/Compactador-de-Arquivos.git
```

---

### 2️⃣ Instale as dependências

```bash
pip install matplotlib pillow imageio
```

---

### 3️⃣ Execute os arquivos

#### Compressão e descompressão

```bash
python Descompactador_arquivos.py
```

#### Gerar arquivo de teste

```bash
python Gerador_texto.py
```

#### Criar GIF

```bash
python Gerador_Gif.py
```

#### Gerar gráficos

```bash
python grafico.py
```

---

## 📈 Resultados Esperados

O projeto permite comparar diferentes métodos de compressão observando:

| Método | Tempo        | Redução   | Memória |
| ------ | ------------ | --------- | ------- |
| LZW    | Rápido       | Boa       | Baixa   |
| Zlib   | Muito rápido | Excelente | Média   |

---

## 🎯 Possíveis Melhorias

Alguns pontos que podem evoluir no projeto:

* Interface gráfica
* Compressão de múltiplos formatos
* Compressão de imagens diretamente
* Relatórios automáticos
* Integração web
* Comparação com mais algoritmos

---

## 🧠 Conceitos Trabalhados

Este projeto aborda diversos conceitos importantes da computação:

* Estrutura de dados
* Compressão de arquivos
* Algoritmos
* Medição de desempenho
* Manipulação de arquivos
* Visualização de dados
* Processamento de imagens

---

## 👨‍💻 Autor

Desenvolvido por Rodrigo Limeira durante os estudos de Engenharia da Computação e análise de desempenho de algoritmos em Python.
