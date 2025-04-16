# Twitter Clone - Back-end

Este é o back-end de um projeto estilo Twitter, desenvolvido com Django e Django REST Framework. A API permite funcionalidades como cadastro, login, criação de tweets, curtir/descurtir, seguir e visualizar tweets de usuários seguidos.

## Tecnologias Utilizadas

- Python 3.8
- Django
- Django REST Framework
- Poetry
- SQLite (ambiente de desenvolvimento)
- Docker (opcional)
- Pytest + Factory Boy (para testes)

### Autenticação com JWT

O sistema utiliza JWT (JSON Web Token) para autenticação. Para obter o token JWT, é necessário fazer login com o endpoint `POST /api/token/`, fornecendo o `username` e `password` do usuário.


## Instalação

Clone o repositório e entre na pasta do projeto:

```bash
git clone https://github.com/VitorBri/twitter_back.git
cd twitter_back
```

### Banco de Dados (PostgreSQL)

Este projeto utiliza PostgreSQL como banco de dados no ambiente de produção.

## Rodando com Docker

```bash
docker build -t twitter_back .
docker run -p 8000:8000 twitter_back
```

A API estará disponível em: `http://localhost:8000/api/`

---

## Endpoints Principais

- `POST /api/users/` - Criação de usuários
- `POST /api/token/` - Obtenção do token JWT
- `GET /api/tweets/` - Lista todos os tweets
- `POST /api/tweets/` - Cria um novo tweet
- `GET /api/tweets/following/` - Lista tweets de usuários seguidos
- `POST /api/follows/` - Segue um usuário
- `GET /api/follows/` - Lista quem você está seguindo

---

## Testes

Os testes automatizados estão organizados por app, dentro das pastas `tests/`.

Para rodar:

```bash
poetry run pytest
```

---

## Estrutura

O projeto está organizado por apps: `users`, `tweets` e `follows`, com suas próprias rotas, serializers, views e testes.

---

## Observações

- O modelo de usuário foi customizado a partir do `AbstractUser`.
- O campo de curtidas utiliza uma relação ManyToMany entre usuários e tweets.
