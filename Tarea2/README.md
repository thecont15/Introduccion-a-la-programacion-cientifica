# Tarea 2 — Análisis y predicción del peso al nacer

**Jesid Alexander López Álvarez · Introducción a la programación científica · 2026-2**

- [Cuaderno en Google Colab](https://colab.research.google.com/drive/1D-07HWEjbTfljqgGYukFc82ysKeUebFZ).
- [Notebook ejecutado](../notebooks/tarea2_jesid_peso_nacer.ipynb).
- [Tablas y figuras](../notebooks/salidas_tarea2/).
- [Resumen de resultados](../notebooks/salidas_tarea2/resumen_resultados.json).

## Problema y datos

¿Cuánto mejora un árbol de decisión la estimación del peso al nacer, en gramos,
frente a predecir siempre un valor fijo, dentro de los casos de bajo peso
notificados en Medellín?

El CSV SIVIGILA de 2011–2021 contiene **10.187 filas y 19 columnas**.
La variable objetivo es `peso_nacer`; el ejercicio es de regresión.

Fuente: [MEData, Alcaldía de Medellín](https://medata.app.medellin.gov.co/).
Se utiliza la copia del CSV ya disponible en el repositorio. El notebook
descarga una revisión fija desde GitHub y comprueba su SHA-256 para mantener
la misma entrada en cada ejecución.

## Preparación y análisis

1. Lectura como texto con separador y codificación explícitos.
2. Parseo de números, fechas y categorías; separación de vacíos, centinelas y
   fallos de conversión.
3. Auditoría de faltantes, duplicados, rangos y atípicos.
4. Decisión documentada para cada una de las 19 columnas.
5. Cinco figuras descriptivas con pregunta, lectura y límite de interpretación.
6. Comparación del árbol con referencias de media y mediana.

El peso objetivo no se imputa. No se eliminan registros automáticamente por
ser atípicos. Los códigos educativos se conservan como categorías sin
asignarles una equivalencia que no está confirmada para todo el extracto.

## Modelo

- X: `sem_gest`, `comuna`, `tipo_ss_` y `niv_edu_ma`.
- Entrenamiento: **8.148 registros**; prueba: **2.037 registros**.
- Se excluyen dos filas por ausencia de y; se mantienen las ausencias de X
  para tratarlas dentro de la preparación del modelo.
- Semilla: **42**. Profundidad elegida: **2**, mediante validación cruzada
  de cinco particiones en entrenamiento; mínimo de 20 registros por hoja.
- La imputación y el one-hot se ajustan dentro de un Pipeline, sin usar la
  prueba para aprender la preparación ni escoger la profundidad.

| Método | MAE en prueba |
| --- | ---: |
| Media del entrenamiento | 122,90 g |
| Mediana del entrenamiento | 115,23 g |
| Árbol de decisión | 118,17 g |

El árbol mejora el MAE frente a la media en **3,85 %**, pero su error es mayor
que el de la mediana. Su R² en prueba es **0,0424**. Este resultado no demuestra
que un modelo más complejo sea superior a todas las referencias sencillas.

## Límites

El extracto incluye casos de bajo peso; no permite calcular la probabilidad de
bajo peso en todos los nacimientos. Los conteos por comuna no son tasas.
La partición aleatoria no acredita rendimiento en años futuros ni uso clínico.
La semántica y disponibilidad temporal de algunos campos requieren verificación.

## Reproducibilidad y estado

El notebook incluye las salidas de sus **18 celdas de código ejecutadas en orden,
sin errores**, y siete figuras embebidas. No depende de rutas de Windows,
montar Drive ni ejecutar otro cuaderno.

En Colab se ejecuta con **Entorno de ejecución → Ejecutar todas**. Las tablas,
las figuras y las métricas se generan en `salidas_tarea2/` dentro de la sesión.
Las versiones usadas quedan impresas al comienzo del cuaderno.

El archivo se compartió con el docente como lector. Queda confirmar la ejecución
en una sesión real de Colab y el acceso general **Cualquiera que tenga el enlace
→ Lector**.
