from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id': '0', 'nome': 'Antonio',
     'habilidades': ['Python', 'Flask']},
    {'id': '1', 'nome': 'Bigas',
     'habilidades': ['Python', 'Django']},
]


# devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor

#diferenca de utilização de restful para flask simples.

#dessa forma é possivel coloco os metodos dentro das classes

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return response
#Atualizar ou criar
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
#deletar
    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status':'sucesso', 'mensagem':'Registro excluído'}

# Lista todos os desenvolvedor e permite registrar um novo desenvolvedor

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

#aqui definimos a rota a ser utilizada.

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)