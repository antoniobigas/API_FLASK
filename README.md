# API_FLASK 

#curso DIO - rest api com flask.

Professor: Rafael Galleani

Módulos do curso:

#    Configuração de ambiente virtual e introdução ao POSTMAN.

python -m venv .\.virtualenvs\minha_virtualenv

.\.virtualenvs\minha_virtualenv\Scripts\activate

pip install flask

pip freeze (lista tudo que você tem instalado no ambiente)

documentação do flask: https://flask.palletsprojects.com/en/2.2.x/quickstart/



#    Utilização dos metodos, biblioteca Request e JSON


Teste utilizado no POSTMAN  {"valores":[10,10,10]}

Utilização do JSONIFY 
import json
import requests

Teste usado no postman no segundo app
{
    "nome": "Neto",
    "habilidades": [
        "Java",
        "PHP",
        "ruby"
    ]
 
}


#    Desenvolvimento de uma REST API completa



#    Desenvolvimento de uma rest api com Flask-RESTful

Instalação
pip install flask-restful

Documentação referente a flask RESTFul-API.

https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api

#    Manipulação de um banco de dados com SQLAlchemy


#    Autenticação, e rest api com persistencia em  banco de dados




















Observe o seguinte trecho de código:
return USUARIO.get(login) == senha

O que esse trecho de código está fazendo?

![image](https://user-images.githubusercontent.com/100382731/202871347-b9e0af76-1733-454f-99a1-5df62f8d1e70.png)
