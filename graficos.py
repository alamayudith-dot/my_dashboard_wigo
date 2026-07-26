# GRÁFICOS DE BARRAS EN STREAMLIT:
# --------------------------------
import plotly.express as px


# ==============================
# GRÁFICO 1: VENTAS POR MARCA
# ==============================

def grafico_ventas(df):

    ventas = df.groupby("marca")["cantidad"].sum().reset_index()

    grafico01 = px.bar(
        ventas,
        x="marca",
        y="cantidad",
        color="marca",  # Colores diferentes por barra
        title="📈 Ventas por Marca",
        text="cantidad",
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    grafico01.update_traces(
        textposition="outside"
    )

    grafico01.update_layout(
        xaxis_title="Marca",
        yaxis_title="Cantidad vendida",
        template="plotly_white",
        showlegend=False
    )

    return grafico01



# ==============================
# GRÁFICO 2: PRECIO PROMEDIO
# ==============================

def grafico_promedio(df):

    promedio = df.groupby("marca")["precio_venta"].mean().reset_index()

    grafico02 = px.bar(
        promedio,
        x="marca",
        y="precio_venta",
        color="marca",  # Colores diferentes por barra
        title="💵 Precio promedio por marca",
        text="precio_venta",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )

    grafico02.update_traces(
        texttemplate="S/ %{text:,.0f}",
        textposition="outside"
    )

    grafico02.update_layout(
        xaxis_title="Marca",
        yaxis_title="Precio promedio (S/)",
        template="plotly_white",
        showlegend=False
    )

    return grafico02


# ==========================================
# GRÁFICO 3 - PARTICIPACIÓN POR MARCA
# ==========================================

def grafico_participacion(df):

    participacion = (
        df.groupby("marca")["cantidad"]
        .sum()
        .reset_index()
    )

    grafico03 = px.pie(
        participacion,
        names="marca",
        values="cantidad",
        title="🎯 Participación por Marca",
        hole=0.45
    )

    grafico03.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    return grafico03
