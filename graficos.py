# GRÁFICOS DE BARRAS EN STREAMLIT:
# --------------------------------

import plotly.express as px


# GRÁFICO 1


def grafico_ventas(df):
    ventas = df.groupby("marca")["cantidad"].sum().reset_index()


    grafico01 = px.bar(
        ventas,
        x = "marca",
        y = "cantidad",
        title = "Ventas por Marca"
    )
    
    return grafico01




# GRÁFICO 2
def grafico_promedio(df):
    promedio = df.groupby("marca")["precio_venta"].mean().reset_index()


    grafico02 = px.bar(
        promedio,
        x = "marca",
        y = "precio_venta",       
        title = "Precio promedio por marca"
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
        title="Participación por Marca",
        hole=0.45
    )

    grafico03.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    grafico03.update_layout(
        title_x=0.5,
        legend_title="Marca"
    )

    return grafico03

