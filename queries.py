def kpis_gerais(data_inicio, data_fim):
    return f"""
    SELECT 
        SUM(valor_total) AS receita,
        COUNT(*) AS total_vendas,
        AVG(valor_total) AS ticket_medio,
        COUNT(DISTINCT id_cliente) AS clientes
    FROM vendas
    WHERE data_venda BETWEEN '{data_inicio}' AND '{data_fim}';
    """


def vendas_por_dia(data_inicio, data_fim):
    return f"""
    SELECT data_venda::date as data, SUM(valor_total) as total
    FROM vendas
    WHERE data_venda BETWEEN '{data_inicio}' AND '{data_fim}'
    GROUP BY data
    ORDER BY data;
    """


def top_produtos(data_inicio, data_fim):
    return f"""
    SELECT p.nome, SUM(s.quantidade * s.preco_unitario) as total
    FROM itens_venda s
    JOIN produtos p ON s.id_produto = p.id
    JOIN vendas v ON v.id = s.id_venda
    WHERE v.data_venda BETWEEN '{data_inicio}' AND '{data_fim}'
    GROUP BY p.nome
    ORDER BY total DESC
    LIMIT 10;
    """

def kpis_comparativo(data_inicio, data_fim):
    return f"""
    WITH atual AS (
        SELECT 
            SUM(valor_total) AS receita,
            COUNT(*) AS total_vendas,
            AVG(valor_total) AS ticket_medio
        FROM vendas
        WHERE data_venda BETWEEN '{data_inicio}' AND '{data_fim}'
    ),
    anterior AS (
        SELECT 
            SUM(valor_total) AS receita
        FROM vendas
        WHERE data_venda BETWEEN 
            '{data_inicio}'::date - ('{data_fim}'::date - '{data_inicio}'::date)
            AND '{data_inicio}'
    )
    SELECT 
        a.receita,
        a.total_vendas,
        a.ticket_medio,
        b.receita AS receita_anterior
    FROM atual a, anterior b;
    """


def top_produtos_percentual(data_inicio, data_fim):
    return f"""
    SELECT 
        p.nome,
        SUM(s.quantidade * s.preco_unitario) as total,
        ROUND(
            SUM(s.quantidade * s.preco_unitario) * 100.0 / 
            SUM(SUM(s.quantidade * s.preco_unitario)) OVER (),
        2) AS percentual
    FROM itens_venda s
    JOIN produtos p ON s.id_produto = p.id
    JOIN vendas v ON v.id = s.id_venda
    WHERE v.data_venda BETWEEN '{data_inicio}' AND '{data_fim}'
    GROUP BY p.nome
    ORDER BY total DESC
    LIMIT 10;
    """