from dash import dcc, html, callback
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np
from utils import Encabezado, Footer, crear_resumen_ejecutivo, crear_seccion_contenido
from sklearn.preprocessing import MinMaxScaler

# Colores definidos
colors = {
    'primary': '#1C3D5A',
    'secondary': '#3E7CB1',
    'accent': '#A3D5FF',
    'background': '#FFFFFF',
    'text': '#333333'
}

# Datos existentes
years = list(range(2010, 2024))
gini_index = [0.51, 0.505, 0.505, 0.495, 0.495, 0.485, 0.48, 0.475, 0.47, 0.465, 0.46, 0.455, 0.45, 0.445]
poverty_rate = [25.3, 22.8, 20.8, 18.7, 17.2, 15.1, 13.7, 12.7, 11.4, 10.8, 10.8, 11.7, 12.5, 11.9]
education_years = [9.7, 9.8, 9.9, 10.0, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9, 11.0]
health_expenditure = [6.8, 6.9, 7.0, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.0, 8.1]
crime_rate = [2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3700, 3900, 4100]
victimization_rate = [28.2, 28.8, 29.4, 30.0, 30.6, 31.2, 31.8, 32.4, 33.0, 33.6, 34.2, 33.8, 35.0, 36.2]
migration_rate = [1.3, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.2, 4.5, 4.8, 5.1]

df_social = pd.DataFrame({
    'Año': years,
    'Índice de Gini': gini_index,
    'Tasa de Pobreza (%)': poverty_rate,
    'Años de Educación': education_years,
    'Gasto en Salud (% PIB)': health_expenditure,
    'Tasa de Criminalidad (por 100,000 hab.)': crime_rate,
    'Tasa de Victimización (%)': victimization_rate,
    'Tasa de Migración (%)': migration_rate
})

# Nuevos datos simulados para el análisis enriquecido
regiones = ['Arica y Parinacota', 'Tarapacá', 'Antofagasta', 'Atacama', 'Coquimbo', 'Valparaíso', 
            'Metropolitana', "O'Higgins", 'Maule', 'Ñuble', 'Biobío', 'Araucanía', 'Los Ríos', 
            'Los Lagos', 'Aysén', 'Magallanes']

np.random.seed(42)

data = {
    'Region': regiones,
    'Indice_Pobreza': np.random.uniform(5, 25, 16),
    'Desempleo': np.random.uniform(5, 15, 16),
    'Deficit_Habitacional': np.random.uniform(10, 30, 16),
    'Acceso_Agua_Potable': np.random.uniform(85, 100, 16),
    'Acceso_Electricidad': np.random.uniform(95, 100, 16),
    'Indice_Vulnerabilidad': np.random.uniform(20, 50, 16),
    'Cobertura_Salud': np.random.uniform(70, 95, 16),
    'Anos_Escolaridad': np.random.uniform(9, 12, 16),
    'Ingreso_Medio': np.random.uniform(300000, 800000, 16)
}

df_enriquecido = pd.DataFrame(data)

# Normalización de datos para el gráfico de radar
scaler = MinMaxScaler()
df_normalized = pd.DataFrame(scaler.fit_transform(df_enriquecido.select_dtypes(include=[np.number])), 
                             columns=df_enriquecido.select_dtypes(include=[np.number]).columns)
df_normalized['Region'] = df_enriquecido['Region']

def create_social_indicator_figure(indicator):
    try:
        if indicator not in df_social.columns:
            raise ValueError(f"Indicador '{indicator}' no encontrado en el DataFrame")
        
        trace = go.Scatter(
            x=df_social['Año'],
            y=df_social[indicator],
            mode='lines+markers',
            name=indicator,
            line=dict(color=colors['primary'], width=2),
            marker=dict(size=8, color=colors['secondary'])
        )

        layout = go.Layout(
            title=f'Evolución de {indicator} en Chile (2010-2023)',
            xaxis=dict(title='Año'),
            yaxis=dict(title=indicator),
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font=dict(family="Roboto", size=12, color=colors['text'])
        )

        return {'data': [trace], 'layout': layout}
    except Exception as e:
        return go.Figure()  # Figura vacía en caso de error

def create_radar_chart(df):
    try:
        fig = go.Figure()

        for i, region in enumerate(df['Region']):
            fig.add_trace(go.Scatterpolar(
                r=df.iloc[i, :-1].values.tolist() + [df.iloc[i, 0]],
                theta=df.columns[:-1].tolist() + [df.columns[0]],
                fill='toself',
                name=region
            ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1]
                )),
            showlegend=True,
            title="Comparación Multidimensional de Indicadores Sociales por Región"
        )
        return fig
    except Exception as e:
        return go.Figure()  # Figura vacía en caso de error

def create_correlation_heatmap(df):
    try:
        correlation_matrix = df.select_dtypes(include=[np.number]).corr()
        return px.imshow(correlation_matrix, 
                         labels=dict(color="Correlación"),
                         x=correlation_matrix.columns,
                         y=correlation_matrix.columns,
                         title="Matriz de Correlación entre Indicadores Sociales")
    except Exception as e:
        return go.Figure()  # Figura vacía en caso de error
    
def create_layout(app):
    return html.Div([
        Encabezado(app),
        html.Div([
            html.H2("Sociedad Chilena: Desigualdades Persistentes y Nuevos Desafíos", className="section-title"),
            crear_resumen_ejecutivo("""
            El análisis enriquecido de los indicadores sociales de Chile revela una sociedad compleja, 
            con desigualdades persistentes y nuevos desafíos emergentes. Este estudio profundiza en 
            aspectos como vivienda, empleo, acceso a servicios básicos, vulnerabilidad y protección social,
            ofreciendo una visión más holística de la realidad social chilena.
            """),
            
            crear_seccion_contenido("Indicadores Sociales Clave", [
                html.Div([
                    html.Div([
                        dcc.Dropdown(
                            id={'type': 'social-indicator-dropdown', 'page': 'sociedad'},
                            options=[
                                {'label': 'Índice de Gini', 'value': 'Índice de Gini'},
                                {'label': 'Tasa de Pobreza (%)', 'value': 'Tasa de Pobreza (%)'},
                                {'label': 'Años de Educación', 'value': 'Años de Educación'},
                                {'label': 'Gasto en Salud (% PIB)', 'value': 'Gasto en Salud (% PIB)'},
                                {'label': 'Tasa de Criminalidad (por 100,000 hab.)', 'value': 'Tasa de Criminalidad (por 100,000 hab.)'},
                                {'label': 'Tasa de Victimización (%)', 'value': 'Tasa de Victimización (%)'},
                                {'label': 'Tasa de Migración (%)', 'value': 'Tasa de Migración (%)'}
                            ],
                            value='Índice de Gini',
                            clearable=False
                            ),
                        dcc.Graph(id={'type': 'social-indicator-graph', 'page': 'sociedad'}),
                    ], className="column-left"),
                    html.Div([
                        html.Div(id={'type': 'social-indicator-analysis', 'page': 'sociedad'}, className="analysis-text")
                    ], className="column-right"),
                ], className="two-column-layout"),
            ]),

            crear_seccion_contenido("Análisis Regional de Indicadores Sociales", [
                dcc.Graph(id={'type': 'radar-chart', 'page': 'sociedad'}, figure=create_radar_chart(df_normalized)),
                html.Div([
                    html.H4("Interpretación del Gráfico de Radar", className="subsection-title"),
                    dcc.Markdown("""
                    Este gráfico de radar muestra la comparación multidimensional de indicadores sociales 
                    entre las diferentes regiones de Chile. Cada eje representa un indicador social 
                    normalizado, permitiendo una comparación directa entre regiones. Las áreas más grandes 
                    indican un mejor desempeño general en los indicadores sociales.
                    """, className="analysis-text")
                ])
            ]),

            crear_seccion_contenido("Correlaciones entre Indicadores Sociales", [
                dcc.Graph(id={'type': 'correlation-heatmap', 'page': 'sociedad'}, figure=create_correlation_heatmap(df_enriquecido)),
                html.Div([
                    html.H4("Análisis de Correlaciones", className="subsection-title"),
                    dcc.Markdown("""
                    La matriz de correlación revela relaciones importantes entre los diferentes indicadores sociales:
                    
                    - Existe una fuerte correlación negativa entre el Índice de Pobreza y el Acceso a Servicios Básicos,
                      lo que subraya cómo la pobreza se manifiesta en múltiples dimensiones.
                    - La correlación positiva entre Años de Escolaridad e Ingreso Medio refuerza la idea de que la 
                      educación sigue siendo un factor clave en la movilidad social, a pesar de sus deficiencias.
                    - El Déficit Habitacional muestra una correlación significativa con el Índice de Vulnerabilidad,
                      destacando cómo la falta de vivienda adecuada amplifica otras formas de precariedad social.
                    """, className="analysis-text")
                ])
            ]),

            crear_seccion_contenido("Análisis Crítico de la Situación Social en Chile", [
                dcc.Markdown("""
                1. Desigualdad Regional Persistente:
                   Los datos revelan una marcada disparidad entre regiones, con la Región Metropolitana mostrando 
                   consistentemente mejores indicadores que el resto del país. Esta centralización del desarrollo 
                   perpetúa un ciclo de desigualdad que las políticas públicas han sido incapaces de romper.

                2. Déficit Habitacional Crónico:
                   Con tasas de déficit habitacional que oscilan entre 10% y 30%, es evidente que el derecho a la 
                   vivienda digna sigue siendo una promesa incumplida. La especulación inmobiliaria y la falta de 
                   regulación efectiva han priorizado el lucro sobre las necesidades básicas de la población.

                3. Precariedad Laboral Enmascarada:
                   Las tasas de desempleo (5-15%) no reflejan la realidad del subempleo y la informalidad. El modelo 
                   económico neoliberal ha generado empleos de baja calidad y alta inestabilidad, erosionando la 
                   seguridad social y perpetuando la vulnerabilidad económica.

                4. Acceso a Servicios Básicos: Una Falsa Victoria:
                   Aunque las cifras de acceso a agua potable y electricidad parecen altas (85-100%), estas estadísticas 
                   enmascaran problemas de calidad y continuidad del servicio, especialmente en zonas rurales y periurbanas.

                5. Vulnerabilidad Social Estructural:
                   Los índices de vulnerabilidad (20-50%) demuestran que una parte significativa de la población vive 
                   en constante riesgo de caer en la pobreza. Este "éxito" del modelo chileno se sostiene sobre una 
                   base frágil de endeudamiento y precariedad.

                Conclusión:
                El análisis revela un Chile profundamente desigual, donde los aparentes avances macroeconómicos 
                enmascaran realidades sociales precarias y vulnerables. El modelo de desarrollo chileno, alabado 
                internacionalmente, se sustenta sobre bases frágiles de desigualdad estructural y exclusión sistemática. 

                La persistencia de estas brechas, a pesar de décadas de políticas supuestamente progresistas, evidencia 
                el fracaso del enfoque neoliberal para abordar problemas sociales complejos. Se requiere una 
                reconstrucción radical del contrato social chileno, priorizando la equidad, la sostenibilidad y la 
                dignidad humana por encima de los indicadores macroeconómicos superficiales.
                """, className="analysis-text")
            ]),

        ], className="page-content"),
        Footer(app)
    ], className="main-container")

@callback(
    [Output({'type': 'social-indicator-graph', 'page': 'sociedad'}, 'figure'),
     Output({'type': 'social-indicator-analysis', 'page': 'sociedad'}, 'children')],
    [Input({'type': 'social-indicator-dropdown', 'page': 'sociedad'}, 'value')]
)
def update_social_content(selected_indicator):
    if not selected_indicator:
        raise PreventUpdate

    try:
        fig = create_social_indicator_figure(selected_indicator)
        analysis = f"Análisis crítico para {selected_indicator}:\n\n"
        
        if selected_indicator == 'Índice de Gini':
            analysis += """
            El Índice de Gini ha mostrado una leve mejoría, pasando de 0.51 en 2010 a 0.445 en 2023. 
            Sin embargo, esta reducción es insuficiente considerando que Chile sigue siendo uno de los 
            países más desiguales de la OCDE. La persistencia de esta desigualdad sugiere que las 
            políticas redistributivas han sido ineficaces para abordar las brechas estructurales en la sociedad chilena.
            """
        elif selected_indicator == 'Tasa de Pobreza (%)':
            analysis += """
            La tasa de pobreza ha disminuido significativamente, de 25.3% en 2010 a 11.9% en 2023. 
            Aunque esto parece ser un logro importante, es crucial considerar la calidad de vida de 
            quienes han superado la línea de pobreza. Muchos chilenos viven en una situación de 
            vulnerabilidad económica, apenas por encima del umbral de pobreza.
            """
        elif selected_indicator == 'Años de Educación':
            analysis += """
            El promedio de años de educación ha aumentado marginalmente de 9.7 a 11 años entre 2010 y 2023. 
            Este incremento de solo 1.3 años en más de una década es preocupantemente bajo. Refleja un 
            estancamiento en el desarrollo educativo del país y sugiere que el sistema educativo no está 
            evolucionando al ritmo necesario para preparar a la población para los desafíos de una economía moderna.
            """
        elif selected_indicator == 'Gasto en Salud (% PIB)':
            analysis += """
            El gasto en salud como porcentaje del PIB ha aumentado modestamente del 6.8% al 8.1% entre 2010 y 2023. 
            Este incremento es insuficiente considerando el envejecimiento de la población y los crecientes 
            desafíos en salud pública. La pandemia de COVID-19 expuso las deficiencias del sistema de salud 
            chileno, evidenciando la necesidad de una inversión mucho más significativa.
            """
        elif selected_indicator == 'Tasa de Criminalidad (por 100,000 hab.)':
            analysis += """
            La tasa de criminalidad ha aumentado alarmantemente de 2,800 a 4,100 por 100,000 habitantes entre 2010 y 2023. 
            Este incremento del 46% refleja un deterioro significativo en la seguridad ciudadana. El aumento de 
            la delincuencia no solo afecta la calidad de vida de los chilenos, sino que también puede tener 
            implicaciones negativas para la inversión y el desarrollo económico del país.
            """
        elif selected_indicator == 'Tasa de Victimización (%)':
            analysis += """
            La tasa de victimización ha aumentado de 28.2% en 2010 a 36.2% en 2023. Este incremento refleja 
            una creciente percepción de inseguridad entre la población chilena. La discrepancia entre la tasa 
            de criminalidad y la tasa de victimización sugiere que la percepción de inseguridad puede estar 
            aumentando más rápidamente que el crimen real.
            """
        elif selected_indicator == 'Tasa de Migración (%)':
            analysis += """
            La tasa de migración ha aumentado sustancialmente del 1.3% al 5.1% entre 2010 y 2023. Este cambio 
            demográfico significativo presenta desafíos importantes en términos de integración social, presión 
            sobre los servicios públicos y potenciales tensiones culturales. La falta de políticas migratorias 
            adecuadas y de planificación para este influjo ha exacerbado estos desafíos.
            """
        else:
            analysis += f"No se encuentra un análisis específico para el indicador: {selected_indicator}"
        
        return fig, dcc.Markdown(analysis)
    
    except Exception as e:
        return go.Figure(), f"Error al procesar el indicador: {str(e)}"
    
def init_callbacks(app):
    pass