from flask import Flask, request, jsonify
from flask_cors import CORS

# Configura o servidor na porta 5000 (Igual ao Node.js antigo)
app = Flask(__name__)
CORS(app) 

# Rota de Login
@app.route('/login', methods=['POST'])
def login():
    dados = request.json
    usuario = dados.get('usuario')
    senha = dados.get('senha')
    
    print(f"Tentativa de Login: {usuario}")
    
    if usuario == 'admin' and senha == '123':
        return jsonify({'auth': True, 'nome': 'Gerente'})
    else:
        return jsonify({'auth': False}), 401

# Rota de Vendas
@app.route('/vendas', methods=['POST'])
def registrar_venda():
    dados = request.json
    print(f"💰 VENDA REGISTRADA: {dados['produto']} - R$ {dados['valor']}")
    return jsonify({'msg': 'Sucesso'})

if __name__ == '__main__':
    print(">>> SERVIDOR BACKEND (PYTHON) ONLINE NA PORTA 5000")
    app.run(port=5000, debug=True)