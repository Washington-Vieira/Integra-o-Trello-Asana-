# Integração Trello ↔ Asana - Projeto MVC com Streamlit

Este projeto realiza a sincronização de quadros (boards) do Trello com projetos no Asana, convertendo listas em seções e cards em tarefas. Foi desenvolvido usando arquitetura MVC com interface visual em Streamlit.

---

## Índice

1. [Clonar o Repositório](#clonar-o-repositório)  
2. [Obter Chaves de API](#obter-chaves-de-api)  
3. [Configurar Ambiente e Variáveis](#configurar-ambiente-e-variáveis)  
4. [Executar o Projeto Localmente](#executar-o-projeto-localmente)  
5. [Executar com Docker](#executar-com-docker)  
6. [Fluxo de Funcionamento](#fluxo-de-funcionamento)  
7. [Como a Sincronização Funciona](#como-a-sincronização-funciona)  

---

## Clonar o Repositório

git clone https://github.com/Washington-Vieira/Integra-o-Trello-Asana-.git
cd seu-repositorio


---

## Obter Chaves de API

### Trello

1. Acesse [https://trello.com/app-key](https://trello.com/app-key) para obter sua **API Key**.  
2. Clique no link de geração de token na mesma página para criar seu **Token** com permissão de leitura e escrita.

### Asana

1. Acesse [https://app.asana.com](https://app.asana.com).  
2. Clique no seu avatar > "My Profile Settings" > Aba "Apps".  
3. Clique em "Manage Developer Apps" e crie um **Personal Access Token (PAT)**.

---

## Configurar Ambiente e Variáveis

1. Copie o arquivo `config.py` e insira suas chaves:

TRELLO_KEY = "Sua_Trello_API_Key"
TRELLO_TOKEN = "Seu_Trello_Token"
ASANA_TOKEN = "Seu_Asana_PAT"


2. Você pode optar por usar `.env` e `python-dotenv` para gerenciar variáveis de ambiente (opcional).

---

## Executar o Projeto Localmente

Instale as dependências:

pip install -r requirements.txt

text

Execute a aplicação:

python run.py


Abra seu navegador em [http://localhost:8501](http://localhost:8501) para interagir com a interface.

---

## Executar com Docker

Para rodar via Docker:

1. Monte as variáveis no arquivo `config.py` (normalmente não use `.env` com este exemplo).  
2. Execute:

docker-compose up --build


3. Acesse [http://localhost:8501](http://localhost:8501) para usar a aplicação.

---

## Fluxo de Funcionamento

flowchart TD
    UI[Usuário acessa a interface Streamlit]
    UI --> Select[Seleciona Board Trello e Workspace Asana]
    Select --> Controller[Controller recebe IDs selecionados]
    Controller --> TrelloAPI[Model Trello: obtém listas e cards via API]
    Controller --> AsanaAPI[Model Asana: criação de projeto e seções via API]
    TrelloAPI --> Controller
    Controller --> ForEachList[Para cada lista no Trello]
    ForEachList --> AsanaAPI_CreateSection[Criar seção no Asana]
    ForEachList --> ForEachCard
    ForEachCard[Para cada card na lista]
    ForEachCard --> AsanaAPI_CreateTask[Criar tarefa no Asana]
    AsanaAPI_CreateSection --> Controller
    AsanaAPI_CreateTask --> Controller
    Controller --> UI[Exibe status e logs na interface]

    style UI fill:#f9f,stroke:#333,stroke-width:2px
    style Controller fill:#bbf,stroke:#333,stroke-width:2px


---

## Como a Sincronização Funciona

- O app lê via API todos os boards disponíveis do Trello do usuário autenticado.  
- Exibe os nomes desses boards para que o usuário escolha qual sincronizar.  
- Também busca os workspaces do usuário no Asana para seleção do destino.  
- Após o usuário escolher, o sistema:  
  - Cria um projeto novo no Asana com o nome do board Trello.  
  - Para cada lista do board Trello, cria uma seção correspondente no projeto Asana.  
  - Para cada card da lista, cria uma tarefa no Asana associada à seção correspondente.  
- Mensagens e logs são mostrados em tempo real na interface Streamlit.  

---