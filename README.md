# Introducción a la programación científica

**Jesid Alexander López Álvarez · 2026-2**

Repositorio de entregas de algoritmos y análisis de datos en Python.

## Tarea 1 — Algoritmos greedy

- [Entrega de Jesid](Tarea1/Jesid/README.md).
- Soluciones de Lemonade Change y Assign Cookies, con pruebas exhaustivas.
- Estado: verificación local disponible; capturas Accepted de LeetCode pendientes.

## Tarea 2 — Peso al nacer

- [README de la Tarea 2 de Jesid](Tarea2/README.md).
- [Google Colab](https://colab.research.google.com/drive/1D-07HWEjbTfljqgGYukFc82ysKeUebFZ).
- [Cuaderno ejecutado](notebooks/tarea2_jesid_peso_nacer.ipynb).
- [Resultados y figuras](notebooks/salidas_tarea2/).

El árbol obtiene MAE **118,17 g**, frente a **122,90 g** de la media y
**115,23 g** de la mediana. El README de la tarea documenta el alcance,
la ejecución y las comprobaciones de acceso pendientes.

## Quinto parcial — Reparación, gráficos y modelo

- [Presentación de Jesid](quinto_parcial/index_jesid.html).
- [Datos verificados de la presentación](quinto_parcial/datos_verificados.json).
- Video: pendiente de grabación y publicación del enlace.

La presentación contiene **31 diapositivas**, cinco figuras incrustadas, seis
fragmentos de Python explicados y un esquema del algoritmo. Funciona sin
internet, con flechas, selector de diapositiva y contador.

Esta versión presenta los resultados guardados en
[sivigila_bpn.ipynb](notebooks/sivigila_bpn.ipynb) y
[prediccion_peso_nacer_arbol.ipynb](notebooks/prediccion_peso_nacer_arbol.ipynb):
baseline **123,7 g**, árbol **120,2 g**, R² **0,035**, mejora reportada **2,8 %**.
El cuaderno nuevo de Tarea 2 usa otra selección de variables y preparación;
sus cifras se documentan por separado y no se intercambian con las de esta
presentación.

## Datos del proyecto

El análisis utiliza el extracto SIVIGILA de bajo peso al nacer en Medellín,
2011–2021: **10.187 registros y 19 columnas** en
[data/sivigila_bpn.csv](data/sivigila_bpn.csv).

Fuente: [MEData, Alcaldía de Medellín](https://medata.app.medellin.gov.co/).
El extracto contiene casos notificados; no representa todos los nacimientos
ni permite calcular riesgo poblacional sin denominadores adicionales.

Los archivos históricos de datos, notebooks y entregas se conservan.
