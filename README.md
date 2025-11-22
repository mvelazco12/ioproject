Modelo de Optimización de Asignación de Turnos – Streamlit + PuLP

Este proyecto implementa un modelo de programación lineal entera binaria para la asignación óptima de turnos de enfermeras, basado en la estructura presentada en Yilmaz (2012).
La aplicación está construida con Streamlit para la interfaz y PuLP (CBC) como solver de optimización.

 Características principales

Optimización de turnos para 50+ enfermeras.

Capacidad para programar 1 o 2 semanas (21 o 42 turnos).

Parámetros ajustables por el usuario.

Restricciones reales del problema:

Límite de horas semanales por enfermera.

Ventana de descanso: no se permiten 2 turnos consecutivos dentro de una ventana de 3.

Mínimos y máximos de personal por turno.

Matriz de resultados dinámica.

Heatmap visual.

Descarga en CSV.

Cálculo automático de:

turnos asignados,

horas trabajadas,

número total de variables binarias del modelo.

📦 Requisitos
pip install streamlit pandas pulp numpy

▶️ Cómo ejecutar la aplicación
streamlit run app.py


Donde app.py es el archivo que contiene el código mostrado.

🧠 Descripción del modelo matemático
Variables


si la enfermera i trabaja el turno j
en otro caso
	​


Variables:


TN×turns

Ejemplo: 50 enfermeras × 42 turnos = 2100 variables binarias.

Función Objetivo

Minimizamos:

𝑍
=
𝑊
𝐻
⋅
𝑇
𝑁
−
ℎ
∑
𝑖
,
𝑗
𝑥
𝑖
𝑗
Z=WH⋅TN−h
i,j
∑
	​

x
ij
	​


Equivalente a maximizar la cantidad de turnos asignados, sin violar restricciones.

Restricciones

Horas máximas por enfermera

ℎ
∑
𝑗
𝑥
𝑖
𝑗
≤
𝑊
𝐻
h
j
∑
	​

x
ij
	​

≤WH

Ventana de descanso (3 turnos)

𝑥
𝑖
,
𝑗
+
𝑥
𝑖
,
𝑗
+
1
+
𝑥
𝑖
,
𝑗
+
2
≤
1
x
i,j
	​

+x
i,j+1
	​

+x
i,j+2
	​

≤1

Mínimo y máximo de personal por turno

𝑁
𝑗
_
𝑚
𝑖
𝑛
[
𝑗
]
≤
∑
𝑖
𝑥
𝑖
𝑗
≤
𝑁
𝑗
_
𝑚
𝑎
𝑥
[
𝑗
]
Nj_min[j]≤
i
∑
	​

x
ij
	​

≤Nj_max[j]
🖥️ Interfaz

La aplicación cuenta con:

Panel lateral para parámetros.

Matriz de asignaciones.

Heatmap visual.

Descarga en CSV.

Métricas automáticas.

 Salida



Métricas del modelo:

Horas totales trabajadas.

Número de turnos asignados.

Número de variables binarias creadas.

Tecnologías usadas

Python

Streamlit

PuLP (CBC solver)

Pandas