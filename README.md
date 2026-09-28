# Exemplos Básicos com FastAPI

Este repositório foi criado com o objetivo de dar os **primeiros passos no FastAPI**, um framework web moderno, rápido (de alto desempenho) e fácil de usar para construir APIs com Python.

Aqui você encontrará exemplos simples e práticos para entender o funcionamento básico da ferramenta.

## Tecnologias Utilizadas

* [Python](https://python.org)
* [FastAPI](https://fastapi.tiangolo.com/pt/)
* [Uvicorn](https://uvicorn.org) (Servidor ASGI para rodar a aplicação)

## Pré-requisitos

Antes de começar, você precisa ter o Python instalado na sua máquina. É recomendável utilizar um ambiente virtual (`venv`).

## Como Rodar o Projeto

Siga os passos abaixo para clonar o repositório e executar os exemplos localmente:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com
   cd NOME_DO_REPOSITORIO
   ```

2. **Crie e ative um ambiente virtual:**
   * No Linux/macOS:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   * No Windows:
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```
   * Ou use o atalho do seu ambiente de desenvolvimento. 

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o servidor local:**
   Substitua `main.py` pelo nome do arquivo do exemplo que deseja testar (caso mude o nome):
   ```bash
   uvicorn main:app --reload
   ```

Depois disso, abra o seu navegador e acesse: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Documentação Automática

Uma das maiores vantagens do FastAPI é a geração automática da documentação da sua API. Com o servidor rodando, você pode acessá-la por dois caminhos:

* **Swagger UI:** [http://127.0.0](http://127.0.0) (Interface interativa para testar as rotas)
