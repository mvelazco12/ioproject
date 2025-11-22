Este manual explica cómo usar la aplicación para generar automáticamente horarios de enfermería mediante modelos matemáticos de optimización.

1️⃣ Inicio

Al abrir la aplicación, verás:

Título del modelo

Panel lateral con parámetros

Botón de Optimización

Área para resultados

2️⃣ Configurar los parámetros

En el panel izquierdo ajusta:

✔ Número de enfermeras (TN)

Valores entre 10 y 200.

✔ Semanas a programar

1 semana → 21 turnos

2 semanas → 42 turnos

✔ Máx horas semanales (WH)

Límite de horas que cada enfermera puede trabajar.

✔ Horas por turno

Duración de cada turno (normalmente 8 h).

3️⃣ Ejecutar el modelo

Haz clic en:

👉 “Optimización”

La aplicación mostrará:

Un mensaje verde de que el solver está trabajando.

El estado final del modelo, normalmente Optimal.

4️⃣ Interpretación de resultados

Pueden aparecer tres secciones:

🟦 1. Matriz de asignaciones

Filas → enfermeras (N1, N2, N3…)

Columnas → turnos (T1, T2, T3…)

Valores:

1 = turno asignado

0 = turno libre

🔥 2. Visualización tipo Heatmap

Azul fuerte → la enfermera trabaja

Azul claro → descanso

Permite identificar:

Distribución del trabajo

Patrones de descanso

Balance en los turnos

📊 3. Métricas

La aplicación muestra:

✔ Turnos asignados

Cantidad total de "1" en la matriz.

✔ Total de horas trabajadas

Se calcula como:

turnos asignados
×
horas por turno
turnos asignados×horas por turno
✔ Variables binarias

Número total de decisiones que el modelo debe tomar:

𝑇
𝑁
×
𝑡
𝑢
𝑟
𝑛
𝑠
TN×turns

Ejemplo:
50 enfermeras × 42 turnos = 2100 variables binarias.