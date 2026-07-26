import streamlit as st

USUARIO = "Infouni"
PASSWORD = "12345"

def login():

    st.title("🔐 WIGO MOTORS S.A.C.")
    st.subheader("Inicio de sesión")

    usuario = st.text_input(" 👤 Usuario")
    password = st.text_input("🔑 Contraseña", type="password")

    if st.button("Ingresar"):

        if usuario == USUARIO and password == PASSWORD:

            st.session_state["login"] = True
            st.session_state["usuario"] = usuario
            st.rerun()

        else:
            st.error("Usuario o contraseña incorrectos")
