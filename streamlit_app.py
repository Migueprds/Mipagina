import streamlit as st

st.title("⚽ Noticias de Fútbol")

st.sidebar.header("Menú")
page = st.sidebar.selectbox("Selecciona una opción", ["Inicio", "Resultados", "Equipos"])

if page == "Inicio":
    st.header("Últimas Noticias")
    st.write("Aquí encontrarás las últimas noticias del mundo del fútbol.")
    
elif page == "Resultados":
    st.header("Resultados en Vivo")
    st.write("Consulta los marcadores más recientes de las principales ligas del mundo.")
    
elif page == "Equipos":
    st.header("Información de Equipos")
    equipo = st.selectbox("Selecciona un equipo", ["Real Madrid", "Barcelona", "Manchester City", "Bayern Múnich"])
    st.write(f"Mostrando información sobre {equipo}.")
