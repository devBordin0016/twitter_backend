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

## Instalação

Clone o repositório e entre na pasta do projeto:

```bash
git clone https://github.com/seu-usuario/twitter-backend.git
cd twitter-backend
```

### Banco de Dados (PostgreSQL)

Este projeto utiliza PostgreSQL como banco de dados no ambiente de produção.

## Rodando com Docker

```bash
docker build -t twitter-backend .
docker run -p 8000:8000 twitter-backend
```

A API estará disponível em: `http://localhost:8000/api/`

---

## Rodando com Poetry (sem Docker)

```bash
poetry install
poetry shell
python manage.py migrate
python manage.py runserver
```

---

## Endpoints Principais

- `POST /api/users/` - Criação de usuários
- `POST /api/token/` - Obtenção do token JWT
- `GET /api/tweets/` - Lista todos os tweets
- `POST /api/tweets/` - Cria um novo tweet
- `PATCH /api/tweets/<id>/like/` - Curte/Descurte um tweet
- `GET /api/tweets/following/` - Lista tweets de usuários seguidos
- `POST /api/follows/` - Segue um usuário
- `GET /api/follows/` - Lista quem você está seguindo

---

## Testes

Os testes automatizados estão organizados por app, dentro das pastas `tests/`.

Para rodar:

```bash
pytest
```

---

## Estrutura

O projeto está organizado por apps: `users`, `tweets` e `follows`, com suas próprias rotas, serializers, views e testes.

---

## Observações

- O modelo de usuário foi customizado a partir do `AbstractUser`.
- O campo de curtidas utiliza uma relação ManyToMany entre usuários e tweets.
