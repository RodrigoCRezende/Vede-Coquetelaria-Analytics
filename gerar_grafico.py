import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuração Visual
sns.set(style="whitegrid")

# 1. Carrega Dados
if os.path.exists("dados.json"):
    with open("dados.json", 'r', encoding='utf-8') as f:
        dados = json.load(f)
else:
    print("❌ Erro: dados.json não encontrado.")
    exit()

df = pd.DataFrame(dados)

# Normaliza colunas
df.columns = [c.lower() for c in df.columns]
if 'valor_total' not in df.columns: df['valor_total'] = df['valor_total'] if 'valor_total' in df.columns else 0
if 'quantidade' not in df.columns: df['quantidade'] = df['quantidade'] if 'quantidade' in df.columns else 0
if 'produto' not in df.columns: df['produto'] = df['nome'] if 'nome' in df.columns else 'Item'

# 2. Classificação (A Mesma da IA)
media_qtd = df['quantidade'].mean()
media_val = df['valor_total'].mean()

def classificar(row):
    if row['quantidade'] >= media_qtd and row['valor_total'] >= media_val: return "Estrela"
    elif row['quantidade'] >= media_qtd: return "Burro de Carga"
    elif row['valor_total'] >= media_val: return "Quebra-Cabeça"
    else: return "Cão"

df['Categoria'] = df.apply(classificar, axis=1)

# Cores oficiais
paleta = {"Estrela": "#ffc107", "Burro de Carga": "#0dcaf0", "Quebra-Cabeça": "#fd7e14", "Cão": "#dc3545"}

# --- GRÁFICO 1: DISPERSÃO (O Clássico) ---
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='quantidade', y='valor_total', hue='Categoria', style='Categoria', s=150, palette=paleta)
plt.axvline(x=media_qtd, color='gray', linestyle='--', alpha=0.5)
plt.axhline(y=media_val, color='gray', linestyle='--', alpha=0.5)
plt.title('Matriz de Engenharia de Cardápio', fontsize=14, fontweight='bold')
plt.xlabel('Volume de Vendas (Qtd)')
plt.ylabel('Receita Total (R$)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("grafico_matriz.png", dpi=300)
print("✅ Gerado: grafico_matriz.png")
plt.close()

# --- GRÁFICO 2: FATURAMENTO POR GRUPO (Barras) ---
plt.figure(figsize=(8, 5))
faturamento = df.groupby('Categoria')['valor_total'].sum().sort_values(ascending=False).reset_index()
sns.barplot(data=faturamento, x='valor_total', y='Categoria', palette=paleta)
plt.title('Impacto Financeiro por Categoria', fontsize=14, fontweight='bold')
plt.xlabel('Faturamento Total (R$)')
plt.ylabel('')
plt.tight_layout()
plt.savefig("grafico_faturamento.png", dpi=300)
print("✅ Gerado: grafico_faturamento.png")
plt.close()

# --- GRÁFICO 3: MIX DE PRODUTOS (Pizza) ---
plt.figure(figsize=(7, 7))
contagem = df['Categoria'].value_counts()
plt.pie(contagem, labels=contagem.index, autopct='%1.1f%%', colors=[paleta.get(x, '#333') for x in contagem.index], startangle=140)
plt.title('Distribuição do Mix de Produtos', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig("grafico_pizza.png", dpi=300)
print("✅ Gerado: grafico_pizza.png")
plt.close()p