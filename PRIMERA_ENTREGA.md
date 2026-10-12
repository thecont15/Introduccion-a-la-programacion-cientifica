# Primera Entrega — Análisis de Datos con Python

## Objetivo de la actividad

En un Jupyter Notebook (`.ipynb`), el grupo debe:

1. Leer y explorar el/los dataset(s).
2. Analizar y limpiar los datos.
3. Encontrar patrones, tendencias o recurrencias interesantes.
4. Crear gráficos que permitan visualizar los resultados.
5. Presentar brevemente los principales hallazgos y conclusiones.

El notebook se publica en el repositorio de GitHub del grupo. Cada integrante hace **commits individuales**
y, al terminar, se hace **merge hacia `main`**. La versión que se evalúa es la que quede en `main`.

**Fecha máxima de entrega: sábado 29 de agosto de 2026, 11:59 p. m.**

## Estado actual del proyecto

- [notebooks/main.ipynb](notebooks/main.ipynb) ya cubre, para `data/WB_CLEAR_AQUASTAT_4554.csv`
  (eficiencia de uso de agua, 1407 filas × 37 columnas):
  - Lectura del dataset (secciones 2 y 2.2).
  - Parseo de números y de texto/categorías (sección 3).
  - Depuración: auditoría mínima, duplicados, valores atípicos por IQR (sección 4).
  - Criterio de cuándo eliminar datos (sección 5.2).
  - Imputación por media/mediana/moda, distribución empírica, ruido e imputación agrupada (sección 6).
- **Pendiente** (puntos 3, 4 y 5 de la actividad, sin empezar todavía):
  - Explorar y limpiar el segundo dataset ya presente en el repo:
    [data/WB_WDI_SH_FPL_SATM_ZS.csv](data/WB_WDI_SH_FPL_SATM_ZS.csv) (sin URL de origen documentada aún).
  - Búsqueda de patrones/tendencias (incluyendo cruces entre ambos datasets si aplica).
  - Gráficos/visualizaciones (no hay ninguno todavía).
  - Sección final de hallazgos y conclusiones.

## Paso a paso a realizar

1. **Documentar la fuente del segundo dataset**
   - Ubicar la URL de origen de `WB_WDI_SH_FPL_SATM_ZS.csv` y agregarla junto a la ya existente
     (mismo criterio que [URL_DATASET.txt](URL_DATASET.txt)).

2. **Leer y explorar el segundo dataset**
   - Nueva sección numerada en el notebook (continuando la numeración existente).
   - `pd.read_csv` con parámetros explícitos, igual que se hizo con el primer dataset.
   - Mostrar `shape`, `info()` y `head()` como evidencia.

3. **Parsear y depurar el segundo dataset**
   - Mismo patrón ya aplicado al primero: parseo de números y texto/categorías, auditoría mínima,
     duplicados, valores atípicos, decisión de eliminar vs. imputar.

4. **Buscar patrones y tendencias**
   - Estadísticas descriptivas relevantes.
   - Si los datasets comparten llave (país/año), evaluar cruces entre ambos.
   - Anotar en markdown cualquier hallazgo antes de graficarlo.

5. **Crear visualizaciones**
   - Al menos: una tendencia temporal (línea), una comparación entre categorías/países (barras)
     y una distribución de valores (histograma o boxplot).
   - Cada gráfico con título y ejes etiquetados; cada uno debe ir precedido de una celda markdown
     que explique qué se está mostrando y por qué.

6. **Redactar hallazgos y conclusiones**
   - Sección markdown final del notebook resumiendo los 2-3 insights más relevantes encontrados,
     apoyados en los gráficos anteriores.

7. **Entrega**
   - Verificar que el notebook completo corre de principio a fin sin errores (Restart & Run All).
   - Abrir Pull Request de la rama de trabajo hacia `main`.
   - Confirmar que `main` queda con la versión final antes de la fecha límite.

## Estándares de flujo de trabajo (Git)

- **Nunca** se escribe ni se hace push directo sobre `main`.
- Todo trabajo se desarrolla en una rama nueva creada a partir de `main`.
- Nombre de rama: `feat-<3 o 4 palabras que resuman el trabajo>`, en minúsculas y separadas por
  guiones (ej. `feat-descargar-dataset-agua`).
- Mensajes de commit con el estilo ya usado en el historial: `feat:<descripción breve>`
  (ej. `feat:agregar resta`, `feat:segundo comentario`).
- Commits pequeños e individuales: cada integrante hace sus propios commits, sin mezclar avances
  de varias personas en uno solo.
- Antes de abrir el Pull Request, sincronizar con `main` (`git fetch` / `git merge main` o `rebase`)
  para evitar conflictos de última hora.
- El Pull Request debe quedar revisado (approve) por al menos un integrante antes de mergear.
- Solo se mergea a `main` cuando el notebook corre completo sin errores.

## Estándares de programación (según lo ya aplicado en el notebook)

- Flujo por dataset: **Lectura → Parseo → Depuración → Imputación/Eliminación**, cada etapa en su
  propia sección numerada del notebook (igual que las secciones 2 a 6 ya existentes).
- Cada sección inicia con una celda markdown con el número y nombre del paso.
- Nombres de variables descriptivos en español y en `snake_case` (`df_world_bank`, `columnas_texto`, etc.).
- Rutas de archivos relativas desde `notebooks/` hacia `../data/`.
- `pd.read_csv` siempre con parámetros explícitos (`sep`, `encoding`, `decimal`, `na_values`), nunca
  con los valores por defecto.
- Comentarios breves que expliquen el **por qué** de una decisión de limpieza (por qué se imputa o
  se elimina), no qué hace la línea de código.
- Cada celda de código muestra evidencia del resultado (`shape`, `head()`, conteos) para que el paso
  quede verificable con solo leer el notebook.
- Si ambos datasets comparten lógica de limpieza, extraerla a una función reutilizable en vez de
  copiar y pegar el mismo bloque dos veces.
- No se hace commit con celdas sin ejecutar o con errores.
