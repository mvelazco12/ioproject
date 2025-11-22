Modelo de Optimización de Asignación de Turnos 

Este proyecto implementa un modelo de programación lineal entera binaria para la asignación óptima de turnos de enfermeras.
La aplicación está construida con Streamlit para la interfaz y PuLP  como solver de optimización.

 - Características principales

Optimización de turnos para 50+ enfermeras.

Capacidad para programar 1 o 2 semanas (21 o 42 turnos).

Parámetros ajustables por el usuario.

Restricciones reales del problema:

Límite de horas semanales por enfermera.

Ventana de descanso: no se permiten 2 turnos consecutivos dentro de una ventana de 3.

Mínimos y máximos de personal por turno.

Matriz de resultados dinámica.

Heatmap visual.

- Cálculo automático de:

turnos asignados,

horas trabajadas,

número total de variables binarias del modelo.

- Requisitos
pip install streamlit pandas pulp numpy

- Cómo ejecutar la aplicación
streamlit run otroproject.py



La aplicación cuenta con:

Panel lateral para parámetros.

Matriz de asignaciones.

Heatmap visual.

Métricas automáticas.

 Salida



- Métricas del modelo:

Horas totales trabajadas.

Número de turnos asignados.

Número de variables binarias creadas.

- Tecnologías usadas: 

Python

Streamlit

PuLP (CBC solver)

Pandas
