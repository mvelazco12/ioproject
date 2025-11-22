import streamlit as st
import pandas as pd
from pulp import *
import numpy as np

st.set_page_config(page_title="Asignación de turnos", layout="wide")

st.title(" Modelo de optimización de asignación de turnos")


st.sidebar.header("⚙️ Parámetros del modelo")


TN = st.sidebar.number_input("Número de enfermeras (TN)", 10, 200, 50)
weeks = st.sidebar.selectbox("Semanas a programar", [1, 2], index=1)
WH = st.sidebar.number_input("Máx horas semanales", 20, 60, 40)
shift_hours = st.sidebar.number_input("Horas por turno", 4, 12, 8)

turns = 21 * weeks

Nj_min = [3,2,1, 3,3,1, 4,2,1, 4,2,1, 3,2,1, 1,1,1, 1,1,1] * weeks
Nj_max = [5,3,2, 4,4,2, 5,3,2, 5,3,2, 4,4,2, 2,1,1, 1,1,1] * weeks

if st.sidebar.button(" Optimización"):
    st.success("Ejecutando solver… por favor espere.")
    

    prob = LpProblem("Nurse_Scheduling", LpMinimize)

    # Variables
    x = LpVariable.dicts("x", (range(TN), range(turns)), 0, 1, LpBinary)

    # Objetivo
    prob += WH*TN - shift_hours * lpSum(x[i][j] for i in range(TN) for j in range(turns))

    # Max horas por enfermera
    for i in range(TN):
        prob += shift_hours * lpSum(x[i][j] for j in range(turns)) <= WH

    # Restricción descanso (ventanas de 3)
    for i in range(TN):
        for j in range(turns - 2):
            prob += x[i][j] + x[i][j+1] + x[i][j+2] <= 1

    # Min / Max por turno
    for j in range(turns):
        prob += lpSum(x[i][j] for i in range(TN)) >= Nj_min[j]
        prob += lpSum(x[i][j] for i in range(TN)) <= Nj_max[j]

    # Resolver
    prob.solve(PULP_CBC_CMD(msg=False))
    
    status = LpStatus[prob.status]
    st.write(f"### ✔ Estado del modelo: **{status}**")

    #resutlaos
    table = pd.DataFrame(0, index=[f"N{i+1}" for i in range(TN)],
                             columns=[f"T{j+1}" for j in range(turns)])

    for i in range(TN):
        for j in range(turns):
            table.iloc[i, j] = int(x[i][j].value())

    st.subheader(" Matriz de asignaciones")
    st.dataframe(table, height=500)

    st.subheader("Visualización tipo Heatmap")
    st.write("Oscuro = trabaja · Claro = libre")

    styled = table.style.background_gradient(cmap="Blues")
    st.dataframe(styled, height=600)

    # DESCARGA CSV
    csv = table.to_csv().encode("utf-8")
    st.download_button("Descargar asignaciones en CSV",
                       csv, "asignaciones.csv", "text/csv")


    # Métricas
    total_shifts = table.sum().sum()
    total_hours = total_shifts * shift_hours

    st.metric("Turnos Asignados", total_shifts)
    st.metric("Total de Horas Trabajadas", total_hours)
    st.metric("Variables Binarias", TN * turns)
