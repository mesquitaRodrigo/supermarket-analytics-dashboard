import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import queries as q
import datetime

# ===== CONFIG =====
load_dotenv()
st.set_page_config(layout="wide", page_title="Analytics Supermarket")

engine = create_engine(os.getenv("DATABASE_URL"))

# ===== CSS MODERNO =====
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.main {
    background-color: #0B0F19;
}

.metric-card {
    background: linear-gradient(145deg, #111827, #0B0F19);
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #1F2937;
}

.metric-title {
    font-size: 14px;
    color: #9CA3AF;
}

.metric-value {
    font-size: 28px;
    font-weight: 600;
}

.metric-delta-up {
    color: #10B981;
}

.metric-delta-down {
    color: #EF4444;
}
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown("## 🏪 Supermarket Analytics")
st.caption("Plataforma de monitoramento de vendas em tempo real")

# ===== FILTROS =====
with st.sidebar:
    st.header("⚙️ Filtros")
    data_inicio = st.date_input("Data início", datetime.date(2024, 1, 1))
    data_fim = st.date_input("Data fim", datetime.date.today())

# ===== CACHE =====
@st.cache_data(ttl=300)
def load(query):
    with engine.connect() as conn:
        return pd.read_sql(query, conn)

# ===== KPIs =====
df = load(q.kpis_comparativo(data_inicio, data_fim))

receita = df["receita"][0] or 0
vendas = df["total_vendas"][0] or 0
ticket = df["ticket_medio"][0] or 0
receita_ant = df["receita_anterior"][0] or 0

crescimento = ((receita - receita_ant) / receita_ant * 100) if receita_ant else 0

# ===== KPIs CUSTOM =====
def metric_card(title, value, delta):
    cor = "metric-delta-up" if delta >= 0 else "metric-delta-down"

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{value}</div>
        <div class="{cor}">{delta:.1f}%</div>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    metric_card("Receita", f"R$ {receita:,.0f}", crescimento)

with col2:
    metric_card("Vendas", f"{int(vendas)}", 0)

with col3:
    metric_card("Ticket Médio", f"R$ {ticket:,.0f}", 0)

with col4:
    metric_card("Crescimento", f"{crescimento:.1f}%", crescimento)

st.markdown("##")

# ===== GRÁFICO PRINCIPAL =====
st.markdown("### 📈 Performance de Receita")

df_vendas = load(q.vendas_por_dia(data_inicio, data_fim))

if not df_vendas.empty:
    st.area_chart(df_vendas.set_index("data"))
else:
    st.warning("Sem dados")

st.markdown("##")

# ===== GRID =====
col1, col2 = st.columns([1.3, 1])

# ===== TOP PRODUTOS =====
with col1:
    st.markdown("### 🏆 Produtos que geram receita")

    df_top = load(q.top_produtos_percentual(data_inicio, data_fim))

    st.dataframe(
        df_top,
        column_config={
            "total": st.column_config.NumberColumn("Receita", format="R$ %.0f"),
            "percentual": st.column_config.NumberColumn("%", format="%.1f%%"),
        },
        width="stretch",
        hide_index=True
    )

# ===== INSIGHTS =====
with col2:
    st.markdown("### 🧠 Inteligência de negócio")

    if not df_top.empty:
        top_nome = df_top.iloc[0]["nome"]
        top_pct = df_top.iloc[0]["percentual"]

        tendencia = "crescendo" if crescimento > 0 else "caindo" if crescimento < 0 else "estável"

        st.markdown(f"""
        #### 🔍 Diagnóstico

        • Receita está **{tendencia}**  
        • Produto líder: **{top_nome}**  
        • Participação: **{top_pct:.1f}%**

        ---
        💡 **Recomendação**

        Foque em aumentar o volume de **{top_nome}**  
        ou diversificar para reduzir dependência.
        """)

st.markdown("##")

# ===== TABELA =====
st.markdown("### 📋 Últimas transações")

df_rec = load(f"""
    SELECT id, data_venda, valor_total
    FROM vendas
    ORDER BY data_venda DESC
    LIMIT 10
""")

st.dataframe(df, width="stretch")