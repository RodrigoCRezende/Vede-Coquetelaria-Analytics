import pandas as pd
import json
import os

# --- CONFIGURAÇÃO CORRIGIDA ---
# Verifica se é xlsx ou csv automaticamente no código abaixo
ARQUIVO_ENTRADA = "vendas.xlsx" 

# SEUS NOMES DE COLUNA EXATOS:
COL_NOME = "Nome"
COL_VALOR = "Valor_Total"  # <--- Corrigido (Com underline)
COL_QTD = "Quantidade"

def converter():
    print(f">>> Lendo arquivo: {ARQUIVO_ENTRADA}...")
    
    try:
        # 1. Tenta ler o arquivo (Excel ou CSV)
        if ARQUIVO_ENTRADA.endswith('.csv'):
            try:
                df = pd.read_csv(ARQUIVO_ENTRADA, sep=',')
            except:
                df = pd.read_csv(ARQUIVO_ENTRADA, sep=';')
        else:
            # Tenta ler Excel. Se der erro de engine, avisa.
            try:
                df = pd.read_excel(ARQUIVO_ENTRADA)
            except ImportError:
                print("❌ ERRO: Faltou instalar a biblioteca do Excel.")
                print("Rode no terminal: pip install openpyxl")
                return

        print(f">>> Arquivo lido! Processando {len(df)} linhas...")
        
        # 2. Verifica se as colunas existem mesmo
        if COL_NOME not in df.columns or COL_VALOR not in df.columns:
            print("❌ ERRO CRÍTICO: Nomes das colunas não batem!")
            print(f"O script buscou: '{COL_NOME}' e '{COL_VALOR}'")
            print(f"O arquivo tem: {list(df.columns)}")
            return

        lista_produtos = []
        
        # 3. Processa cada linha
        for index, row in df.iterrows():
            
            # Limpeza do Valor (Tira R$, troca vírgula por ponto)
            val_str = str(row[COL_VALOR])
            val_limpo = val_str.replace('R$', '').replace(' ', '').replace('.', '').replace(',', '.')
            
            try:
                valor_final = float(val_limpo)
            except:
                valor_final = 0.0
            
            # Limpeza da Quantidade
            try:
                qtd_final = int(row[COL_QTD])
            except:
                qtd_final = 1 # Se não tiver número, assume 1

            # Limpeza do Nome
            nome_prod = str(row[COL_NOME]).strip()

            # Só adiciona se o valor for válido
            if valor_final > 0:
                prod = {
                    "produto": nome_prod,
                    "valor_total": valor_final,
                    "quantidade": qtd_final,
                    # Calcula ticket médio para ajudar a IA
                    "ticket_medio": valor_final / qtd_final if qtd_final > 0 else valor_final
                }
                lista_produtos.append(prod)

        # 4. Salva o arquivo JSON final
        with open("dados.json", "w", encoding='utf-8') as f:
            json.dump(lista_produtos, f, ensure_ascii=False, indent=4)
            
        print("==================================================")
        print(f"✅ SUCESSO! 'dados.json' gerado com {len(lista_produtos)} produtos.")
        print(">>> AGORA RODE NO TERMINAL: python importador.py")
        print("==================================================")

    except FileNotFoundError:
        print(f"❌ ERRO: O arquivo '{ARQUIVO_ENTRADA}' não está nesta pasta.")
    except Exception as e:
        print(f"❌ ERRO GERAL: {e}")

if __name__ == "__main__":
    converter()