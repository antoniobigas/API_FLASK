from flask import Flask, jsonify, request
import json
app = Flask(__name__)

#lista base de exemplo

desenvolvedores = [
    {'id':'0','nome': 'Antonio',
      'habilidades' : ['Python', 'Flask']},
    {'id':'1','nome': 'Bigas',
      'habilidades': ['Python', 'Django']},
]

#devolve um desenvolvedor pelo id, também altera e deleta um registro.

@app.route('/dev/<int:id>/', methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de Id {} não existe'.format(id)
            response =  {'Status':'Erro', 'Mensagem':mensagem}
        except Exception:
            mensagem = 'Erro Desconhecido. Procure o ADM da API'
            response = {'status':'Erro', 'mensagem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'Registro Excluido'})


#lista todos desenvolvedores e permite registrar um novo.
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)
