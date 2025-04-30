# Plataforma Inteligente de Gestão para Rede de Academias

**Desafio Técnico**: Desenvolver uma plataforma inteligente de gestão, processamento de linguagem natural e análise preditiva para otimizar operações e melhorar a experiência dos clientes.

## 1. Visão Geral
Este repositório contém:
- Código-fonte dos microserviços: **_api_gateway_**, **_client_service_**, **_analytics_service_** (churn), **_chatbot_service_** e **_log_service_**.
- Notebooks dos agentes: **_churn_agent_**, **_fitness_assistant_agent_**.

## 2. Microserviços

- **Chatbot Service**: Permite que o cliente se comunique e peça dicas de treinamento de acordo com o seu perfil.
- **Analytics Service (Churn Prediction)**: Recebe informações de um aluno (total de checkins, tipo de plano, frequência semanal) e retorna a probabilidade de churn.
- **Client Service**: CRUD de alunos (consulta geral, detalhe, criação, atualização e remoção).
- **Log Service**: Armazena logs de ações no Client Service (sucesso/erro de cadastro, edição e remoção).
- **API Gateway**: Porta de entrada REST para comunicação com todos os serviços.

## 3. Arquitetura do Sistema

### 3.1 Tecnologias
- **PostgreSQL**: Dados de alunos, planos e checkins.
- **MongoDB**: Armazenamento de logs de ações.
- **RabbitMQ**: Mensageria assíncrona entre serviços.
- **REST**: Comunicação síncrona via API Gateway.

### 3.2 Componentes
- **api_gateway**: Entrada única para chamadas REST.
- **client_service**: Serviço transacional de alunos.
- **analytics_service**: Serviço de predição de churn.
- **chatbot_service**: Serviço de processamento de linguagem natural.
- **log_service**: Armazenamento de logs.

## 4 Fluxos de Dados

### 4.1. Gestão de Cliente
1. Usuário faz requisição via API Gateway.
2. Gateway envia REST para Client Service.
3. Client Service executa operação no PostgreSQL.
4. Client Service publica evento no RabbitMQ.
5. Log Service consome evento e grava no MongoDB.
6. Client Service retorna resposta ao Gateway.
7. Gateway devolve resposta ao usuário.

### 4.2. Chatbot
1. Usuário envia mensagem ao Gateway.
2. Gateway encaminha REST ao Chatbot Service.
3. Chatbot Service processa via agente Phi2.
4. Retorna resposta ao Gateway.
5. Gateway devolve mensagem ao usuário.

### 4.3. Predição de Churn
1. Usuário envia os dados de aluno (frequência semanal, quantidade de checkins e tipo de plano) ao Gateway.
2. Gateway encaminha REST ao Chatbot Service.
3. Chatbot Service processa utilizando um agente de Árvore de Decisão.
4. Retorna resposta ao Gateway.
5. Gateway devolve a probabilidade de churn e explicabilidade (LIME) ao usuário.

## 5 Documentação da API
A documentação completa está disponível [neste arquivo separado](./API_DOC.md).

## 6. Modelos de IA

### 6.1 Predição de Churn
- **Algoritmo**: Árvore de Decisão, escolhida pela sua interpretabilidade e eficiência em ambientes de produção.
- **Métrica principal**: Recall, priorizando a identificação de todos os alunos com alto risco de churn, conforme evidenciado pela matriz de confusão.
- **Explicabilidade**: Implementada com LIME para fornecer insights claros sobre os fatores que influenciam cada previsão individual.

### 6.2 Chatbot
- **Framework**: Agente open-source Phi2, selecionado por seu equilíbrio entre desempenho e baixo consumo de recursos.
- **Objetivo**: Oferecer atendimento automatizado e personalizado, mantendo a operação leve e eficiente, mesmo em ambientes com infraestrutura limitada.

## 7. Diagrama do BD PostgreSQL

![Diagrama ERD](./assets/bd_diagram.png)

## 8. Demonstração do Sistema

[Vídeo de Demonstração](https://drive.google.com/file/d/1OAaGae2JhwIgalD7FdHxViA3fbRsD3gB/view?usp=sharing)

## 9. Como Executar Localmente
Pré-requisitos:
- Docker e Docker Compose

```bash
git clone <https://github.com/carloshgbdev/EngenheiroIA-contra-ataca.git>
cd .\microservices_plataform\
docker-compose up --build
```

Isso inicializará os bancos de dados e os microserviços, seguindo o docker-compose:

```yml
services:
  api_gateway:
    build: ./services/api_gateway
    ports:
      - "8000:8000"
    depends_on:
      - client_service
      - analytics_service
      - chatbot_service

  client_service:
    build: ./services/client_service
    ports:
      - "8001:8001"
    environment:
      RABBITMQ_HOST: "rabbitmq"
      RABBITMQ_PORT: 5672
      RABBITMQ_USER: "carlos"
      RABBITMQ_PASSWORD: "12345"
      DATABASE_URL: postgresql+asyncpg://carlos:12345@postgres:5432/pacto_academia
    depends_on:
      - postgres
      - rabbitmq

  analytics_service:
    build: ./services/analytics_service
    ports:
      - "8002:8002"
    volumes:
      - ./data:/app/data

  chatbot_service:
    build: ./services/chatbot_service 
    ports:
      - "8003:8003"
  
  log_service:
    build: ./services/log_service
    ports:
      - "8004:8004"
    environment:
      RABBITMQ_HOST: "rabbitmq"
      RABBITMQ_PORT: 5672
      RABBITMQ_USER: "carlos"
      RABBITMQ_PASSWORD: "12345"
      MONGO_URL: "mongodb://carlos:12345@mongodb:27017/"
      MONGO_DB_NAME: "logdb"
    depends_on:
      - mongodb
      - rabbitmq
  
  rabbitmq:
    image: rabbitmq:3-management
    container_name: rabbitmq
    ports:
      - "5672:5672"
      - "15672:15672"
    environment:
      RABBITMQ_DEFAULT_USER: carlos
      RABBITMQ_DEFAULT_PASS: 12345

  postgres:
    image: postgres:14
    container_name: postgres
    restart: always
    environment:
      POSTGRES_USER: carlos
      POSTGRES_PASSWORD: 12345
      POSTGRES_DB: pacto_academia
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./db/init_tables.sql:/docker-entrypoint-initdb.d/init_tables.sql

  mongodb:
    image: mongo:latest
    container_name: mongodb
    restart: always
    environment:
      MONGO_INITDB_ROOT_USERNAME: carlos
      MONGO_INITDB_ROOT_PASSWORD: 12345
      MONGO_INITDB_DATABASE: logdb
    ports:
      - "27017:27017"
    volumes:
      - mongodb_data:/data/db

volumes:
  postgres_data:
  mongodb_data:
```
