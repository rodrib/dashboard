import random
import duckdb
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


st.set_page_config(page_title="Ventas Dashboard", page_icon=":bar_chart:", layout="wide")

st.title("Ventas Dashboard")
st.markdown("_Prototype v0.4.1_")


# Leer el archivo CSV
nombre_archivo = 'pages\data-dummies - yerba.csv'
df = pd.read_csv(nombre_archivo)

all_months = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dic"]

with st.expander("Data Preview"):
    st.dataframe(
        df,
        column_config={"Año": st.column_config.NumberColumn(format="%d")},
    )


#######################################
# VISUALIZATION METHODS
#######################################
