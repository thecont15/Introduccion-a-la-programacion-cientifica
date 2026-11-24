# Introduccion-a-la-programacion-cientifica

1. Evaluación 1: datos generales
Campo	Detalle
Periodo	2026-2
Objetivo	Definir el problema, conformar el equipo e iniciar el desarrollo
Peso	20 %
Fecha de entrega	26 de agosto de 2026
Norma	Capítulo XII del Reglamento Estudiantil

Entregables: repositorio en GitHub, Git Flow, README, definición del problema, objetivos y alcance, dataset seleccionado, estructura del proyecto, lectura inicial de datos y primer prototipo funcional.

2. Flujo de trabajo con datos

Leer → Parsear → Depurar → Imputar/eliminar

Etapa	Pregunta	Ejemplo
Lectura	¿Cómo entra el archivo a memoria?	read_csv, encoding, separador
Parseo	¿Qué significa cada valor?	"26/08/2026" → datetime
Depuración	¿El valor es válido en el dominio?	edad = -3, temperatura = 999
Imputación/eliminación	¿Qué hacer con lo que falta?	media, muestreo, borrar fila

Regla de oro: no se imputa ni se borra nada que no se haya parseado y auditado antes.

3. Lectura (pandas)
Inspeccionar primero: pd.read_csv(..., nrows=5). Revisar separador, encoding, decimal, filas de título y cómo se marcan los faltantes.
Lectura controlada: definir sep, encoding, decimal y na_values explícitos.
Errores típicos:
UnicodeDecodeError: probar utf-8, latin-1 o cp1252.
Una sola columna gigante: el separador no es coma.
Números como texto: usar decimal="," y thousands=".".
Fechas como object: parsearlas.
Debe quedar constancia de: ruta, encoding, separador, filas y columnas, y % de faltantes por variable.
4. Parseo
Números: pd.to_numeric(errors="coerce"), y contar cuántos valores se perdieron.
Fechas: pd.to_datetime(..., dayfirst=True). En Colombia el día va primero.
Texto: strip, lower y unificar categorías (M, m, Masculino → masculino).
Booleanos: unificar Sí/No, 1/0 con un diccionario.
Criterio: parsear no es "arreglar" el dato. Lo que no cumple el tipo pasa a faltante.
5. Depuración
Auditoría mínima (obligatoria): dtype, n.º y % de faltantes, valores únicos y duplicados.
Duplicados:
Fila idéntica: se puede eliminar tras verificarla.
Misma clave con valores distintos: se documenta y se decide con una regla.
Tipos de valores raros:
Imposibles (edad = -5): se vuelven NaN.
Atípicos verosímiles: no se borran.
Centinelas (999, -99): se recodifican a NaN al leer.
La regla IQR detecta candidatos, no los elimina.
Consistencia entre variables: por ejemplo, la fecha de muerte no puede ser anterior a la de nacimiento. Se marca la fila, no se promedia.
6. Datos faltantes
Mecanismos:
MCAR: falta al azar.
MAR: falta según otras variables.
MNAR: falta por el propio valor.
Sí se elimina:
Filas vacías.
Duplicados exactos.
Columnas constantes o con ~100 % de faltantes.
Registros de prueba.
Imposibles irrecuperables.
Variables fuera de alcance.
Si una columna supera ~30–40 % de faltantes, mejor no usarla.
No se elimina:
Atípicos reales.
Una fila por faltar en una sola columna.
Muestras pequeñas.
Ausencia informativa (MNAR).
Errores de unidad, que se corrigen.
Datos cuyo origen no se entiende.
7. Imputación
Método	Preserva el centro	Preserva forma/varianza	Uso razonable
Media	Sí	No (pico y menos varianza)	Exploración, 1–5 % de faltantes
Mediana	Sí (robusto)	No	Datos asimétricos
Moda	Clase más frecuente	Infla esa clase	Categóricas
Muestreo empírico (hot-deck)	Aprox.	Sí	Cuando no se debe deformar el histograma
Predicción + ruido / MICE	Sí	Mejor	Si hay variables auxiliares
Imputación agrupada: dentro de un grupo (ciudad, sexo), usando groupby().transform().
Fijar semilla (default_rng(42)) para que sea reproducible.
Lo que no se debe hacer:
Imputar antes de parsear o recodificar centinelas.
Imputar la variable respuesta.
Presentar datos imputados como mediciones.
Encadenar media, borrado de atípicos y nueva media.
8. Orden recomendado del prototipo
Leer con encoding, separador y na_values explícitos.
Parsear tipos.
Contar los NaN nacidos en el parseo frente a los originales.
Depurar duplicados, centinelas e imposibles.
Decidir por variable: dejar, imputar o eliminar.
Si se imputa, comparar histograma y desviación estándar antes y después.
Dejar código y decisiones en el repositorio.
9. Estructura sugerida del proyecto
├── README.md
├── data/
│   ├── raw/          # original, no se edita
│   └── processed/    # salidas de parseo y depuración
├── notebooks/
├── src/
└── requirements.txt

Git Flow: main estable, develop y ramas feature/.... Si no se pueden subir los datos, el README indica la fuente y el script de descarga.

10. Criterios del prototipo

Debe mostrar que el equipo:

Eligió el dataset y definió problema, objetivos y alcance.
Lee el archivo de forma reproducible.
Parsea tipos.
Depura con reglas de dominio.
Justifica lo que elimina y lo que no.
Distingue la media de una imputación que no destruye la distribución.
Entrega un primer resultado generado por código.
11. Definición del problema (lo que escribiste)
Problema: talla de recién nacidos en Medellín. Se analiza la tasa de prematuros según la edad y la diversificación de la edad en los barrios.
Objetivos: mapas de calor por barrio, y usar los valores atípicos para ver diferencias entre edades y concluir cuál es la situación actual de las edades al dar a luz.
Alcance: edad vs barrio y comuna, talla vs sexo, edad vs registros.
Dataset: peso_nacer, medata con SIVIGILA, licencia, "19 filas y 1048576 columnas". Variables de interés: 15.
Limitaciones del dato: pendiente.
Puntos para revisar en tu definición
Filas y columnas: "19 filas y 1048576 columnas" parece invertido. 1.048.576 es el límite de filas de Excel, así que probablemente son esas filas y 19 columnas. Si es así, no pueden ser 15 variables de interés de 19 columnas sin justificarlo. Verifícalo con df.shape.
Talla y peso: el dataset se llama peso_nacer, pero el problema habla de talla. Aclara si usarás peso, talla o ambas.
Atípicos: el documento dice que no se borran solo por estar lejos. Si los usas como objetivo, explica cómo los distinguirás de los errores.
Limitaciones: falta completarlas. Algunas ideas: faltantes, barrios sin nombre o mal escritos, sesgo por subregistro y centinelas.

## Quinto parcial

#Sebastian Benavides

- Video: https://correoitmedu-my.sharepoint.com/:v:/r/personal/sebastianbenavides318826_correo_itm_edu_co/Documents/quinto_parcial.mp4?d=w59ab8e7f9d034a3c8eef5e35a4372530&csf=1&web=1&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D&e=Uk9WeV
- Diapositivas: `quinto_parcial/index.html`