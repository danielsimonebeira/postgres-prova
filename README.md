# Objetivo do projeto

1 – Crie um banco de dados no postgres com o nome prova e com a tabela
música. Faça a persistência de dois registros do tipo música no postgres
através do python. Deve conter pelo menos três campos na coleção: id, nome,
autor, gênero (1,5 ponto)


## Pré-requisitos para executar o projeto
### Base de dados:
* Docker
* docker-compose

### Projeto
* Python 3.8

## Iniciar a base

Na raiz do projeto executar o comando abaixo:

``docker-compose up -d``

Após subir a base é possivel acessar pelo navegador http://localhost:8080

- **Servidor:** prova
- **Usuario:** teste
- **Senha:** teste
- **Base de dados:** musica