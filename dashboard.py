import streamlit as st
from Conexion import cargar_datos
from Indicadores import *     # * indica todos las variables uqe estan dentro de la funcion indicadores 
from graficos import *
from auth import login

@st.cache_data
def obtener_datos():
    return cargar_datos()

df = obtener_datos()    #UTILIZANDO LA FUNCION  QUE NOS DEVUELVE EL DATA FRAME

# CONFIGURACIÓN DE DASHBOARD CON STREAMLIT:


st.set_page_config(page_title = "Wigo Motors", 
                   layout="wide")      
if "login" not in st.session_state:
    st.session_state["login"] = False

if not st.session_state["login"]:
    login()
    st.stop()

st.title("WIGO MOTORS S.A.C. 🚗 ")                      
st.subheader("📊 Dashboard comercial") 

st.sidebar.success(f"Bienvenido: {st.session_state['usuario']}")

if st.sidebar.button("Cerrar sesión"):

    st.session_state.clear()
    st.rerun()

st.sidebar.header("Buscador")
tipo_busqueda = st.sidebar.selectbox("Seleccione tipo de búsqueda", ["Marca", "Asesor comercial", "Sede"])  


df_filtrado = df.copy()     # Haciendo una copia del DataFrame 



# FILTRO POR MARCA:


if tipo_busqueda == "🚗 Marca":
    valor = st.sidebar.selectbox("Seleccionar marca", sorted(df["marca"].unique())) # Mostrar las marcas disponibles y sin repetir
    df_filtrado = df[df["marca"] == valor]                                   # Filtrar búsqueda por marca  
    
elif tipo_busqueda == "👨‍💼 Asesor comercial":
    valor = st.sidebar.selectbox("Seleccionar asesor", sorted(df["asesor_comercial"].unique())) # Mostrar las marcas disponibles y sin repetir
    df_filtrado = df[df["asesor_comercial"] == valor]                                   # Filtrar búsqueda por marca  
    
elif tipo_busqueda == "🏢 Sede":
    valor = st.sidebar.selectbox("Seleccionar sede", sorted(df["tienda"].unique())) # Mostrar las marcas disponibles y sin repetir
    df_filtrado = df[df["tienda"] == valor]                                   # Filtrar búsqueda por marca  

# =====================================
# FILTRO POR RANGO DE PRECIOS
# =====================================

precio_min = int(df["precio_venta"].min())
precio_max = int(df["precio_venta"].max())

rango_precio = st.sidebar.slider(
    "💰 Rango de precio (S/)",
    min_value=precio_min,
    max_value=precio_max,
    value=(precio_min, precio_max),
    step=1000
)

df_filtrado = df_filtrado[
    (df_filtrado["precio_venta"] >= rango_precio[0]) &
    (df_filtrado["precio_venta"] <= rango_precio[1])
]


# MOSTRAR RESULTADOS:


st.success(f"Registros encontrados: {len(df_filtrado)}")        # Mostrar la cantidad de filas encontradas (color verde)
st.dataframe(
    df_filtrado,
    use_container_width=True,
    hide_index=True
)


# INDICADORES GENERALES:

st.subheader("Indicadores:")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Precio Total", f"S/{precio_total(df_filtrado):,.2f}")
c2.metric("Unidades vendidas", f"{unidades_vendidas(df_filtrado)}")
c3.metric("Precio promedio", f"S/{precio_promedio(df_filtrado):,.2f}")
c4.metric("Operaciones", operaciones(df_filtrado))

c5, c6, c7, c8 = st.columns(4)

c5.metric("Precio más alto", f"S/{precio_maximo(df_filtrado):,.2f}")
c6.metric("Precio más bajo", f"S/{precio_minimo(df_filtrado):,.2f}")

st.plotly_chart(
    grafico_ventas(df_filtrado),
    use_container_width=True,
    key="grafico_ventas"
)

st.plotly_chart(
    grafico_promedio(df_filtrado),
    use_container_width=True,
    key="grafico_promedio"
)

st.plotly_chart(
    grafico_participacion(df_filtrado),
    use_container_width=True
)



