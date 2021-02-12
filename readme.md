[![GitHub license](https://img.shields.io/badge/implemented%20by-Andy-blue)](https://www.linkedin.com/in/andy-kiaka-76a983110/)

## Abordagem

1. Ambiente virtual
   
    Cada desenvolvedor tem suas preferências na eleição de ferramentas para definir um ambiente virtual, para esta implementação optei em usar o pipenv que usa o Pipfile em vez do requirements.txt, no entanto será fornecido um arquivo requirements.txt para facilitar outros desenvolvedores a usar esta implementação.

## Pré-requisitos

1. Bibliotecas
   
   Como descrito nos arquivos Pipfile e requirements.txt, as bibliotecas necessárias para rodar esta implementação são:

    * django = "~=3.1.6"
    * djangorestframework = "~=3.12.2"
    * drf-yasg = "~=1.20.0"
    * drf-toolbox
    * dj-rest-auth
    * django-allauth
    * psycopg2-binary

## Como usar

1. Construir as imagens executando
    ```
    $ docker-compose up -d --build
    ```
2. Faça as migrações
   A implementação já vem com a migração de app pages feita, o dev só precisa fazer a "migrate"
   ```
   $ docker-compose exec web python manage.py migrate
   ``` 
3. Cria um super user
   ```
   $ docker-compose exec web python manage.py createsuperuser
   ```

   Para inserir novos valores na base de dados o usuário precisa logado após criar um usuário como demostrado acima.

### Endpoints

Todos os endpoints disponíveis junto com uma documentação auto gerada podem ser via o link 

*   http://localhost:8000/swagger/

O acesso na api possui o seguinte prefixo : http://localhost:8000/api/...

Exemplo:

* http://localhost:8000/api/parent/
* http://localhost:8000/api/child/

## Autor ✒️

* **Andy Kiaka** - *Job Completo* - [detona115](https://github.com/detona115)

---
⌨️ com ❤️ por [detona115](https://github.com/detona115) 😊