# API de Gerenciamento de Notícias

## Descrição
Esta é uma API REST desenvolvida com Django REST Framework para gerenciar notícias. A API permite criar, listar, atualizar, e deletar notícias, utilizando boas práticas de desenvolvimento e design.

## Tecnologias Utilizadas
- Python 3.9+
- Django 5.1.5
- Django REST Framework 3.15.2
- Docker 27.4.0

## Funcionalidades
**Para o banco SQL**
- **Listar todas as notícias**: `GET /api/api_noticias/`
- **Obter uma notícia por ID**: `GET /api/api_noticias/{id}/`
- **Criar uma nova notícia**: `POST /api/api_noticias/`
- **Atualizar uma notícia**: `PUT /api/api_noticias/{id}/`
- **Deletar uma notícia**: `DELETE /api/api_noticias/{id}/`

**Para o banco de memoria**
- **Listar todas as notícias**: `GET /api/memoria/api_noticias/`
- **Obter uma notícia por ID**: `GET /api/memoria/api_noticias/{id}/`
- **Criar uma nova notícia**: `POST /api/memoria/api_noticias/`
- **Atualizar uma notícia**: `PUT /api/memoria/api_noticias/{id}/`
- **Deletar uma notícia**: `DELETE /api/memoria/api_noticias/{id}/`

## Como Rodar o Projeto

### Localmente com Python

1. **Clone o repositório**:
   ```bash
   git clone <url-do-repositorio>
   cd <nome-do-repositorio>
   ```

2. **Crie um ambiente virtual e ative-o**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate   # Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplique as migrações**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Rode o servidor**:
   ```bash
   python manage.py runserver
   ```

6. **Acesse a API**:
   
    **Banco de Dados SQL**
   - URL base: `http://127.0.0.1:8000/api/api_noticias`

   **Banco de memória**
   - URL base: `http://127.0.0.1:8000/api/memoria/api_noticias`

### Usando Docker

1. **Certifique-se de ter Docker instalado**.

2. **Construa e inicie os containers**:
   ```bash
   docker build -t api_docker .

   docker run -d -p 8000:8000 --name api  api_docker
   ```

   **Para iniciar o servidor Docker**
   ```bash
   docker start api
   ```

   **Para parar o servidor Docker**
   ```bash
   docker stop api
   ```


3. **Banco de Dados SQL**
   - URL base: `http://127.0.0.1:8000/api/api_noticias`

   **Banco de memória**
   - URL base: `http://127.0.0.1:8000/api/memoria/api_noticias`

### Utilizando o arquivo .http
   Você também pode utilizar um arquivo `.http` para interagir com a API sem precisar usar o navegador. Os arquivos "api_memoria.http" e "api_SQL.http" vão conter as seguintes requisições de exemplo:

   **utilizado o aquivo "api_SQL.http"**

    
    GET http://127.0.0.1:8000/api/api_noticias/

    ###

    POST  http://127.0.0.1:8000/api/api_noticias/
    Content-Type: application/json

    {   
        "titulo": "Novas vagas na GovOne para Desenvolvedor Python Junior",
        "conteudo": "Descrição da Vaga",
        "autor": "Teste"
    }

    ###

    GET http://127.0.0.1:8000/api/api_noticias/<id>/

    ###

        PUT http://127.0.0.1:8000/api/api_noticias/<id>/
        Content-Type: application/json

    {
        "titulo": "Desenvolvedor Java Pleno",
        "conteudo": "Descrição da Vaga",
        "autor": "Teste"
        "ativo": true
    }

    ###

    DELETE http://127.0.0.1:8000/api/api_noticias/<id>/
    

Você pode executar esse arquivo diretamente em editores como o VS Code, usando uma extensão como o [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).

## Testes

Para rodar o teste automatizado:
```bash
python manage.py test
```

## Estrutura do Projeto
```
testepratico/
|-- api_noticias/
|   |-- migrations/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- memoria.py
|   |-- models.py
|   |-- serializers.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|
|-- http/
|   |-- api_memoria.http
|   |-- api_SQL.http
|
|-- setup/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|
|-- db.sqlite3
|-- manage.py
|-- requirements.txt
|-- Readme.md
|-- Dockerfile
```

## Endpoints

### **Listar todas as notícias**
- **URL**: `/api/api_noticias/` ou `/api/memoria/api_noticias`
- **Método**: `GET`
- **Resposta**:
  ```json
  [
    {
      "id": 1,
      "titulo": "Exemplo de Notícia",
      "conteudo": "Este é um conteúdo de exemplo",
      "autor": "Autor Exemplo",
      "ativo" true
      "data_publicacao": "2025-01-23T10:00:00Z"
    }
  ]
  ```

### **Criar uma nova notícia**
- **URL**: `/api/api_noticias/` ou `/api/memoria/api_noticias`
- **Método**: `POST`
- **Body**:
  ```json
  {
    "titulo": "Nova Notícia",
    "conteudo": "Conteúdo da notícia",
    "autor": "Autor da Notícia"
    "ativo" true
  }
  ```
- **Resposta**:
  ```json
  {
    "id": 2,
    "titulo": "Nova Notícia",
    "conteudo": "Conteúdo da notícia",
    "autor": "Autor da Notícia",
    "ativo" true
    "data_publicacao": "2025-01-23T10:15:00Z"
  }
  ```

### **Atualizar uma notícia**
- **URL**: `/api/api_noticias/{id}/` ou `/api/memoria/api_noticias/{id}`
- **Método**: `PUT` 
- **Body**
  ```json
  {
    "titulo": "Título Atualizado"
  }
  ```
- **Resposta**:
  ```json
  {
    "id": 2,
    "titulo": "Título Atualizado",
    "conteudo": "Conteúdo da notícia",
    "autor": "Autor da Notícia",
    "ativo" true
    "data_publicacao": "2025-01-23T10:15:00Z"
  }
  ```

### **Deletar uma notícia**
- **URL**: `/api/noticias/{id}/`
- **Método**: `DELETE`
- **Resposta**:
  ```json
  {
    "detail": "Notícia removida permanentemente."
  }
  ```
**O método alternativo para deletar uma publicação é usando a função ativo ou inativo, caso ativo = True, as noticias serão listadas com todas as notícias, caso contrario, a noticia estará inativa, mas poderar ser editada usando o id**

## Contato
Caso tenha dúvidas ou precise de suporte, envie um e-mail para mateus_sbatista@hotmail.com.

