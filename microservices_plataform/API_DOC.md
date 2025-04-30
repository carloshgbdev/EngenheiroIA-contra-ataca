# Gateway API
Gateway central para comunicação entre microserviços

## Version: 1.0.0

### /cliente/alunos

#### GET
##### Summary:

List Alunos

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |

#### POST
##### Summary:

Add Aluno

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

### /cliente/alunos/{aluno_id}

#### GET
##### Summary:

Get Aluno

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| aluno_id | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

#### PUT
##### Summary:

Update Aluno

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| aluno_id | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

#### DELETE
##### Summary:

Delete Aluno

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| aluno_id | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

### /churn/

#### POST
##### Summary:

Make Prediction

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

### /chatbot/

#### POST
##### Summary:

Fitness Assistant

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

### Models


#### AlunoCreate

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| nome | string |  | Yes |
| frequencia_semanal | integer |  | Yes |
| tipo_plano | integer |  | Yes |

#### AlunoResponse

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | Yes |
| nome | string |  | Yes |
| frequencia_semanal | integer |  | Yes |
| ultimo_checkin_id |  |  | No |
| tipo_plano | integer |  | Yes |

#### AlunoUpdate

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| nome |  |  | No |
| frequencia_semanal |  |  | No |
| tipo_plano |  |  | No |
| ultimo_checkin_id |  |  | No |

#### ChurnInput

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| frequencia_semanal | integer |  | Yes |
| total_checkins | integer |  | Yes |
| tipo_plano | integer |  | Yes |

#### FitnessQuery

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| question | string |  | Yes |
| user_profile | string |  | Yes |

#### GenericResponse_AlunoResponse_

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| success | boolean |  | Yes |
| message | string |  | Yes |
| status_code | integer |  | Yes |
| data |  |  | No |

#### GenericResponse_list_AlunoResponse__

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| success | boolean |  | Yes |
| message | string |  | Yes |
| status_code | integer |  | Yes |
| data |  |  | No |

#### HTTPValidationError

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| detail | [ [ValidationError](#validationerror) ] |  | No |

#### ValidationError

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| loc | [  ] |  | Yes |
| msg | string |  | Yes |
| type | string |  | Yes |