import json
import pandas as pd
import os
import sys

# CONFIGURAÇÃO
ARQUIVO_JSON = "dados.json"
ARQUIVO_CSV = "vendas.csv" # Ou vendas.xlsx

def carregar_dados():
    print(">>> Lendo arquivos de dados...")
    dados = []
    
    if os.path.exists(ARQUIVO_JSON):
        print(f"   -> Encontrado JSON: {ARQUIVO_JSON}")
        with open(ARQUIVO_JSON, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            
    elif os.path.exists(ARQUIVO_CSV):
        print(f"   -> Encontrado CSV: {ARQUIVO_CSV}")
        df = pd.read_csv(ARQUIVO_CSV)
        # Padronização básica de nomes
        df.columns = [c.lower().replace(' ', '_') for c in df.columns]
        dados = df.to_dict('records')
    
    else:
        print("❌ ERRO: Nenhum arquivo encontrado (dados.json ou vendas.csv).")
        return None
        
    return dados

def main():
    print("=== IMPORTADOR DE DADOS (MODO ARQUIVO) ===")
    dados = carregar_dados()

    if not dados:
        return

    print(f"✅ SUCESSO! {len(dados)} registros lidos e validados.")
    print(">>> O sistema usará este arquivo localmente para a IA.")
    print(">>> Não é necessário MongoDB instalado.")

if __name__ == "__main__":
    main()