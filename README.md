# 🍸 Vedê Analytics

> **Sistema de Suporte à Decisão (DSS) baseado em Inteligência Artificial para gestão de bares e restaurantes.**

Este projeto foi desenvolvido como parte do **Projeto Integrador**, visando solucionar a falta de previsibilidade e análise estratégica de dados no estabelecimento *Vedê Coquetelaria & Arte*.

---

## 🚀 Sobre o Projeto

O **Vede Analytics** é uma plataforma que integra operações de vendas (PDV) com análise de dados avançada. Diferente de sistemas tradicionais que apenas registram o passado, este sistema utiliza algoritmos de **Machine Learning (Clustering)** para qualificar o mix de produtos e sugerir estratégias de estoque e marketing.

### 🧠 Diferencial: IA de Engenharia de Cardápio
O sistema não utiliza regras fixas. Ele aplica o algoritmo **K-Means** sobre os dados históricos para classificar os produtos na **Matriz de Engenharia de Menu**:
* ⭐ **Estrelas:** Alta Venda / Alta Receita.
* 🐮 **Burros de Carga:** Alta Venda / Baixa Receita.
* 🧩 **Quebra-Cabeças:** Baixa Venda / Alta Receita.
* 🐕 **Cães:** Baixa Venda / Baixa Receita.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído sobre uma arquitetura de microsserviços robusta e unificada em Python:

* **Frontend:** HTML5, CSS3, JavaScript (Vanilla).
* **Backend API:** Python Flask (Gerenciamento de Autenticação e Transações).
* **Módulo de IA:** Python Flask + Scikit-Learn + Pandas (Processamento Estatístico).
* **Banco de Dados:** MongoDB (NoSQL).
* **Automação:** Scripts Python para ETL (Extração, Transformação e Carga) de dados.

---

## 📂 Estrutura do Projeto

```text
/
├── backend/           # API de Gestão (Porta 5000)
│   └── servidor.py
├── ia/                # API de Inteligência (Porta 5002)
│   └── inteligencia.py
├── frontend/          # Interface do Usuário
│   └── index.html
├── conversor.py       # Script ETL: Converte Planilhas Excel para JSON
├── importador.py      # Script ETL: Carrega dados no MongoDB
└── dados.json         # Base de Conhecimento (Dataset)
