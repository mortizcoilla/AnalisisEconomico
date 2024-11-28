# Informe Económico de Chile

## Descripción del Proyecto

Este proyecto es una aplicación web interactiva desarrollada con Dash, una biblioteca de Python para crear aplicaciones web analíticas. La aplicación proporciona un análisis detallado de varios aspectos de la economía chilena, incluyendo macroeconomía, comercio, políticas públicas, métricas sociales y análisis sectorial. La aplicación está diseñada para ayudar a los usuarios a comprender mejor la situación económica y social de Chile a través de datos, gráficos y análisis detallados.

## Alcances

- **Macroeconomía**: Análisis de indicadores macroeconómicos clave como el PIB, la desigualdad, la productividad, la inflación y el desempleo.
- **Comercio**: Análisis del comercio internacional de Chile, incluyendo exportaciones, importaciones y balanza comercial.
- **Políticas Públicas**: Análisis de indicadores clave de políticas públicas como el gasto público, la inversión pública, la deuda pública y la presión fiscal.
- **Métricas Sociales**: Análisis de indicadores sociales clave como el índice de Gini, la tasa de pobreza, la educación, el gasto en salud, la criminalidad y la migración.
- **Análisis Sectorial**: Análisis de la contribución de diferentes sectores al PIB de Chile, incluyendo minería, agricultura, manufactura, servicios y construcción.

## Herramientas y Tecnologías

- **Dash**: Biblioteca de Python para crear aplicaciones web analíticas.
- **Plotly**: Biblioteca para crear gráficos interactivos.
- **Pandas**: Biblioteca para manipulación y análisis de datos.
- **Scikit-learn**: Biblioteca para aprendizaje automático y análisis de datos.
- **HTML/CSS**: Para el diseño y estilo de la interfaz de usuario.

## Estructura del Proyecto

### 1. Archivo Principal (`app.py`)
- **Inicialización de la App**: Configura la aplicación Dash con opciones como el título y la carpeta de assets.
- **Layout Principal**: Define el layout principal que incluye una barra lateral y el contenido principal.
- **Callbacks de Navegación**: Maneja la navegación entre diferentes páginas basadas en la URL.
- **Ejecución de la App**: Ejecuta la aplicación en modo de depuración.

### 2. Página de Macroeconomía (`macroeconomia.py`)
- **Datos para Gráficos**: Define los datos para los gráficos, como el PIB, la desigualdad, la productividad, la inflación y el desempleo.
- **Análisis de Indicadores**: Proporciona un diccionario con análisis detallados para cada indicador.
- **Layout de la Página**: Define el layout de la página, incluyendo un resumen ejecutivo, un menú desplegable para seleccionar indicadores, gráficos y análisis.
- **Funciones Auxiliares**: Funciones para crear gráficos y manejar callbacks.
- **Callbacks**: Actualiza el gráfico y el análisis basado en el indicador seleccionado.

### 3. Página de Comercio (`comercio.py`)
- **Datos para Gráficos**: Define los datos para los gráficos, como exportaciones, importaciones y balanza comercial.
- **Análisis de Indicadores**: Proporciona un diccionario con análisis detallados para cada indicador.
- **Layout de la Página**: Define el layout de la página, incluyendo un resumen ejecutivo, un menú desplegable para seleccionar indicadores, gráficos y análisis.
- **Funciones Auxiliares**: Funciones para crear gráficos y manejar callbacks.
- **Callbacks**: Actualiza el gráfico y el análisis basado en el indicador seleccionado.

### 4. Página de Políticas Públicas (`politicas.py`)
- **Datos para Gráficos**: Define los datos para los gráficos, como el gasto público, la inversión pública, la deuda pública y la presión fiscal.
- **Análisis de Indicadores**: Proporciona un diccionario con análisis detallados para cada indicador.
- **Layout de la Página**: Define el layout de la página, incluyendo un resumen ejecutivo, un menú desplegable para seleccionar indicadores, gráficos y análisis.
- **Funciones Auxiliares**: Funciones para crear gráficos y manejar callbacks.
- **Callbacks**: Actualiza el gráfico y el análisis basado en el indicador seleccionado.

### 5. Página de Métricas Sociales (`sociedad.py`)
- **Datos para Gráficos**: Define los datos para los gráficos, como el índice de Gini, la tasa de pobreza, la educación, el gasto en salud, la criminalidad y la migración.
- **Análisis de Indicadores**: Proporciona un diccionario con análisis detallados para cada indicador.
- **Layout de la Página**: Define el layout de la página, incluyendo un resumen ejecutivo, un menú desplegable para seleccionar indicadores, gráficos y análisis.
- **Funciones Auxiliares**: Funciones para crear gráficos y manejar callbacks.
- **Callbacks**: Actualiza el gráfico y el análisis basado en el indicador seleccionado.

### 6. Página de Análisis Sectorial (`sectorial.py`)
- **Datos para Gráficos**: Define los datos para los gráficos, como la contribución de la minería, la agricultura, la manufactura, los servicios y la construcción al PIB.
- **Análisis de Indicadores**: Proporciona un diccionario con análisis detallados para cada sector.
- **Layout de la Página**: Define el layout de la página, incluyendo un resumen ejecutivo, un menú desplegable para seleccionar sectores, gráficos y análisis.
- **Funciones Auxiliares**: Funciones para crear gráficos y manejar callbacks.
- **Callbacks**: Actualiza el gráfico y el análisis basado en el sector seleccionado.

### 7. Utilidades (`utils.py`)
- **Crear Resumen Ejecutivo**: Función para crear un resumen ejecutivo.
- **Crear Sección de Contenido**: Función para crear una sección de contenido.

## Instalación

Para ejecutar la aplicación, sigue estos pasos:

1. Clona el repositorio:
   ```bash
   git clone <URL del repositorio>
   cd <nombre del directorio>

2. Instala las dependencias:
 
    pip install -r requirements.txt

3. Ejecuta la aplicación:


    python app.py
    Abre tu navegador y ve a http://127.0.0.1:8050/ para ver la aplicación en funcionamiento.

Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún problema o tienes una sugerencia, por favor abre un issue o envía un pull request.
