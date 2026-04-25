# 🏪 Supermarket Analytics Dashboard

Dashboard interativo para análise de vendas de supermercado, desenvolvido com foco em **tomada de decisão orientada a dados**.

🔗 **Acesse o projeto online:**
https://supermarket-analytics-dashboard-gacdai8ni45fjihtfjabed.streamlit.app/

---

## 📊 Visão Geral

Este projeto simula um cenário real de negócio onde dados transacionais são transformados em **insights estratégicos**.

A aplicação permite:

* Monitorar desempenho de vendas
* Identificar tendências ao longo do tempo
* Entender quais produtos geram mais receita
* Apoiar decisões com base em dados reais

---

## 🎯 Principais Funcionalidades

* 💰 KPIs de negócio (Receita, Vendas, Ticket Médio, Crescimento)
* 📈 Evolução de vendas ao longo do tempo
* 🏆 Ranking de produtos com participação percentual
* 🎛️ Filtros por período (data início/fim)
* 🧠 Insights automáticos com recomendações
* ⚡ Cache para otimização de performance

---

## 🧠 Insights de Negócio

O dashboard não apenas exibe dados, mas gera interpretações como:

* Produto com maior contribuição de receita
* Tendência de crescimento ou queda
* Sugestões de ação baseadas na performance

👉 O foco é transformar dados em **decisão estratégica**.

---

## 🧱 Arquitetura

```text
Streamlit (Frontend + Backend)
        ↓
SQLAlchemy (conexão com banco)
        ↓
PostgreSQL (Supabase)
```

---

## 🛠️ Tecnologias Utilizadas

* Python
* Streamlit
* Pandas
* SQLAlchemy
* PostgreSQL
* Supabase

---

## 📂 Estrutura do Projeto

```bash
├── app.py              # Dashboard principal
├── queries.py          # Queries SQL organizadas
├── requirements.txt    # Dependências do projeto
├── .env                # Variáveis de ambiente (não versionado)
├── images/             # Prints do dashboard
```

---

## ⚙️ Como Executar Localmente

```bash
git clone https://github.com/mesquitaRodrigo/supermarket-analytics-dashboard
cd supermarket-analytics-dashboard

pip install -r requirements.txt
streamlit run app.py
```

---

## 🔐 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=postgresql://usuario:senha@host:porta/database
```

⚠️ Nunca compartilhe credenciais no repositório.

---

## 📸 Preview

![Dashboard](images/dashboard.png)

---

## 🚀 Próximos Passos

* 🔥 Versão frontend com React + ApexCharts
* 🧠 Insights avançados com Machine Learning
* 📊 Previsão de vendas
* 👥 Análise de clientes (segmentação, LTV)
* 🔐 Autenticação e multiusuário

---

## 🎯 Objetivo do Projeto

Demonstrar habilidades em:

* Análise de dados
* Construção de dashboards
* Integração com banco de dados
* Desenvolvimento de aplicações analíticas
* Pensamento orientado a produto

---

## 👨‍💻 Autor

**Rodrigo Mesquita**

---

## ⭐ Considerações

Este projeto representa um passo inicial na construção de soluções de dados mais avançadas, evoluindo de um MVP analítico para um **produto de dados completo**.
