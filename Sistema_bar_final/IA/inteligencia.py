from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.linear_model import LinearRegression

# Configura a IA na porta 5001
app = Flask(__name__)
CORS(app)

@app.route('/previsao', methods=['GET'])
def calcular():
    # Dados históricos simulados
    dados = {
        'dia': [0, 1, 2, 3, 4, 5, 6],
        'vendas': [1200, 1100, 1300, 2400, 5500, 6200, 4100]
    }
    df = pd.DataFrame(dados)
    
    modelo = LinearRegression()
    modelo.fit(df[['dia']], df['vendas'])
    
    previsoes = []
    # 4=Sex, 5=Sab, 6=Dom
    nomes = {4: 'Sexta-Feira', 5: 'Sábado', 6: 'Domingo'}
    
    for dia, nome in nomes.items():
        valor = modelo.predict([[dia]])[0]
        if valor > 5000: status = "ALTA (Reforçar Staff)"
        elif valor > 3500: status = "MÉDIA"
        else: status = "BAIXA"
        
        previsoes.append({
            'dia': nome,
            'valor': f"R$ {valor:.2f}",
            'status': status
        })
        
    return jsonify(previsoes)

if __name__ == '__main__':
    print(">>> MÓDULO IA (PYTHON) ONLINE NA PORTA 5001")
    app.run(port=5002, debug=True)