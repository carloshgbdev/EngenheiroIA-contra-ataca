# Gateway API
API central para orquestração e comunicação entre os microserviços da plataforma de gestão de academias.

**Versão:** 1.0.0

---

## Endpoints

### `/cliente/alunos`

#### GET
**Resumo:**  
Retorna a lista completa de alunos cadastrados.

**Respostas:**

| Código | Descrição                  |
| ------ | -------------------------- |
| 200    | Lista retornada com sucesso |

#### POST
**Resumo:**  
Cadastra um novo aluno no sistema.

**Respostas:**

| Código | Descrição                      |
| ------ | ------------------------------ |
| 200    | Aluno cadastrado com sucesso   |
| 422    | Erro de validação nos dados    |

---

### `/cliente/alunos/{aluno_id}`

#### GET
**Resumo:**  
Consulta os detalhes de um aluno específico pelo seu ID.

**Parâmetros:**

| Nome     | Localização | Descrição         | Obrigatório | Tipo    |
| -------- | ----------- | ----------------- | ----------- | ------- |
| aluno_id | path        | ID único do aluno | Sim         | integer |

**Respostas:**

| Código | Descrição                               |
| ------ | --------------------------------------- |
| 200    | Dados do aluno retornados com sucesso   |
| 422    | Erro de validação no parâmetro `aluno_id` |

#### PUT
**Resumo:**  
Atualiza as informações de um aluno existente.

**Parâmetros:**

| Nome     | Localização | Descrição         | Obrigatório | Tipo    |
| -------- | ----------- | ----------------- | ----------- | ------- |
| aluno_id | path        | ID único do aluno | Sim         | integer |

**Respostas:**

| Código | Descrição                                  |
| ------ | ------------------------------------------ |
| 200    | Dados do aluno atualizados com sucesso     |
| 422    | Erro de validação nos dados ou no `aluno_id` |

#### DELETE
**Resumo:**  
Remove um aluno do sistema pelo ID.

**Parâmetros:**

| Nome     | Localização | Descrição         | Obrigatório | Tipo    |
| -------- | ----------- | ----------------- | ----------- | ------- |
| aluno_id | path        | ID único do aluno | Sim         | integer |

**Respostas:**

| Código | Descrição                          |
| ------ | ---------------------------------- |
| 200    | Aluno removido com sucesso         |
| 422    | Erro de validação no parâmetro `aluno_id` |

---

### `/churn/`

#### POST
**Resumo:**  
Realiza a previsão de churn (cancelamento) com base no perfil do aluno.

**Respostas:**

| Código | Descrição                    |
| ------ | ---------------------------- |
| 200    | Previsão gerada com sucesso  |
| 422    | Erro de validação nos dados  |

---

### `/chatbot/`

#### POST
**Resumo:**  
Assistente virtual para responder dúvidas relacionadas a treino e saúde com base no perfil do usuário.

**Respostas:**

| Código | Descrição                    |
| ------ | ---------------------------- |
| 200    | Resposta gerada com sucesso  |
| 422    | Erro de validação nos dados  |

---

## Modelos

### AlunoCreate
Dados necessários para cadastrar um novo aluno.

| Nome              | Tipo    | Obrigatório |
| ----------------- | ------- | ----------- |
| nome              | string  | Sim         |
| frequencia_semanal| integer | Sim         |
| tipo_plano        | integer | Sim         |

### AlunoResponse
Representação dos dados de um aluno.

| Nome              | Tipo    | Obrigatório |
| ----------------- | ------- | ----------- |
| id                | integer | Sim         |
| nome              | string  | Sim         |
| frequencia_semanal| integer | Sim         |
| ultimo_checkin_id |         | Não         |
| tipo_plano        | integer | Sim         |

### AlunoUpdate
Dados opcionais para atualizar informações de um aluno.

| Nome              | Tipo | Obrigatório |
| ----------------- | ---- | ----------- |
| nome              |      | Não         |
| frequencia_semanal|      | Não         |
| tipo_plano        |      | Não         |
| ultimo_checkin_id |      | Não         |

### ChurnInput
Informações necessárias para gerar uma previsão de churn.

| Nome              | Tipo    | Obrigatório |
| ----------------- | ------- | ----------- |
| frequencia_semanal| integer | Sim         |
| total_checkins    | integer | Sim         |
| tipo_plano        | integer | Sim         |

### FitnessQuery
Consulta enviada para o assistente virtual.

| Nome         | Tipo   | Obrigatório |
| ------------ | ------ | ----------- |
| question     | string | Sim         |
| user_profile | string | Sim         |

### GenericResponse_AlunoResponse_
Resposta genérica contendo os dados de um aluno.

| Nome        | Tipo    | Obrigatório |
| ----------- | ------- | ----------- |
| success     | boolean | Sim         |
| message     | string  | Sim         |
| status_code | integer | Sim         |
| data        |         | Não         |

### GenericResponse_list_AlunoResponse__
Resposta genérica contendo uma lista de alunos.

| Nome        | Tipo    | Obrigatório |
| ----------- | ------- | ----------- |
| success     | boolean | Sim         |
| message     | string  | Sim         |
| status_code | integer | Sim         |
| data        |         | Não         |

### HTTPValidationError
Erro retornado em caso de falha na validação dos dados.

| Nome   | Tipo                                   | Obrigatório |
| ------ | -------------------------------------- | ----------- |
| detail | Lista de [ValidationError](#validationerror) | Não         |

### ValidationError
Detalhes sobre um erro de validação.

| Nome | Tipo  | Obrigatório |
| ---- | ----- | ----------- |
| loc  | Lista | Sim         |
| msg  | string| Sim         |
| type | string| Sim         |
