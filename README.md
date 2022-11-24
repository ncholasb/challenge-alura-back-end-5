# challenge-alura-back-end-5

4 semanas de desafios propostos pela Alura com o objetivo de praticar construindo um projeto. A cada semana são disponibilizados novos desafios.

___


| :placard: Vitrine.Dev |                                                |
| --------------------- | ---------------------------------------------- |
| :sparkles: Nome       | **Challenge Backend 5 - Alura**                |
| :label: Tecnologias   | FastAPI, Python, Docker, PostgreSQL            |
| :rocket: URL          | 🚧                                              |
| :fire: Desafio        | https://www.alura.com.br/challenges/back-end-5 |

___
<!-- Inserir imagem com a #vitrinedev ao final do link -->


### Desafios de cada semana
- [X] <b>1ª semana</b> - CRUD de videos e testes de api utilizando Postman
   - [X] Retornar vídeos
   - [X] Retornar um vídeo
   - [X] Cadastrar vídeo
   - [X] Atualizar vídeo
   - [X] Deletar vídeo
   - [X] Testes Postman

- [x] <b>2ª semana</b> - CRUD de categorias e testes de unidade e integração.
   - [X] Retornar categorias
   - [X] Retornar um categoria
   - [X] Cadastrar categoria
   - [X] Atualizar categoria
   - [X] Deletar categoria
   - [X] Atribuir vídeo a categoria
   - [X] Retornar vídeos por categoria
   - [X] Utilizar query parameters em vídeo
   - [x] Testes de unidade
   - [x] Testes de integração

- [ ] <b>3ª e 4ª semana</b> - Paginação, autenticação e deploy da aplicação.
   - [X] Paginação
   - [X] Autenticação
   - [ ] Deploy

Extra:
  - [ ] Enviar e-mails HTML para confirmação de cadastro.
___
___
# Rotas
| <span style="color:lightblue">Auth</span> |                               |               |
| ----------------------------------------- | ----------------------------- | ------------- |
| POST                                      | /api/auth/register            | Create User   |
| POST                                      | /api/auth/login               | Login         |
| GET                                       | /api/auth/refresh             | Refresh Token |
| GET                                       | /api/auth/logout              | Logout        |
| GET                                       | /api/auth/verifyemail/{token} | Verify user   |
|                                           |

| <span style="color:lightblue">Users</span> |               |             |
| :----------------------------------------: | :-----------: | :---------: |
|                    GET                     | /api/users/me | Get my info |
|                                            |

| <span style="color:lightblue">Videos</span> |                              |                   |
| :-----------------------------------------: | :--------------------------: | :---------------: |
|                     GET                     |         /api/videos          |    Get Videos     |
|                    POST                     |         /api/videos          |    Post Videos    |
|                     GET                     |       /api/videos/{id}       | Get Videos By Id  |
|                     PUT                     |       /api/videos/{id}       |    Put Videos     |
|                   DELETE                    |       /api/videos/{id}       |   Delete Video    |
|                     GET                     | /api/videos/?search={search} | Get Videos Search |
|                                             |

| <span style="color:lightblue">Categorias</span> |                             |                        |
| :---------------------------------------------: | :-------------------------: | :--------------------: |
|                       GET                       |       /api/categorias       |     Get Categorias     |
|                      POST                       |       /api/categorias       |    Post Categorias     |
|                       GET                       |    /api/categorias/{id}     |  Get Categorias By Id  |
|                       PUT                       |    /api/categorias/{id}     |     Put Categorias     |
|                     DELETE                      |    /api/categorias/{id}     |    Delete Categoria    |
|                       GET                       | /api/categorias/{id}/videos | Get Videos By Category |