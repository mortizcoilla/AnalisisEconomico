from dash import html, dcc, callback
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
from utils import Encabezado, crear_resumen_ejecutivo, crear_seccion_contenido

# Datos para los gráficos (asegúrate de que esta parte esté correcta y completa)
df_summary = pd.DataFrame({
    'Año': range(2010, 2024),
    'Índice de Libertad Económica': [78, 77, 76, 75, 73, 72, 70, 68, 66, 64, 62, 60, 58, 56],
    'Crecimiento del PIB (%)': [5.8, 6.1, 5.3, 4.0, 1.8, 2.3, 1.7, 1.2, 3.9, 1.1, -5.8, 11.7, 2.4, 0.2],
    'Poder Adquisitivo (Índice)': [100, 102, 104, 105, 106, 107, 108, 109, 110, 111, 105, 102, 95, 90],
    'Tasa de Criminalidad (por 100,000 hab.)': [2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3700, 3900, 4100],
    'Satisfacción con el Sistema de Salud (%)': [70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44],
    'Calidad de la Educación (Índice)': [75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62]
})

# Colores personalizados
colors = {
    'primary': '#1C3D5A',
    'secondary': '#3E7CB1',
    'text_primary': '#4A4A4A',
    'text_secondary': '#818181',
    'background': '#FFFFFF',
    'background_alt': '#F5F8FA',
    'accent': '#A3D5FF',
    'border': '#E0E0E0'
}

def crear_grafico(id, tipo, datos):
    try:
        if tipo == 'libertad-pib':
            figure = go.Figure(data=[
                go.Scatter(x=datos['Año'], y=datos['Índice de Libertad Económica'], name='Libertad Económica', yaxis='y', line=dict(color=colors['primary']), mode='lines+markers', marker=dict(size=8, color=colors['primary'])),
                go.Scatter(x=datos['Año'], y=datos['Crecimiento del PIB (%)'], name='Crecimiento PIB', yaxis='y2', line=dict(color=colors['secondary']), mode='lines+markers', marker=dict(size=8, color=colors['secondary']))
            ])
            figure.update_layout(
                title='Libertad Económica vs. Crecimiento del PIB',
                yaxis=dict(title='Índice de Libertad Económica', titlefont=dict(color=colors['primary'])),
                yaxis2=dict(title='Crecimiento del PIB (%)', overlaying='y', side='right', titlefont=dict(color=colors['secondary']))
            )
        elif tipo == 'calidad-vida':
            figure = go.Figure(data=[
                go.Scatter(x=datos['Año'], y=datos['Poder Adquisitivo (Índice)'], name='Poder Adquisitivo', line=dict(color=colors['primary']), mode='lines+markers', marker=dict(size=8, color=colors['primary'])),
                go.Scatter(x=datos['Año'], y=datos['Satisfacción con el Sistema de Salud (%)'], name='Satisfacción con el Sistema de Salud', line=dict(color=colors['secondary']), mode='lines+markers', marker=dict(size=8, color=colors['secondary'])),
                go.Scatter(x=datos['Año'], y=datos['Calidad de la Educación (Índice)'], name='Calidad de la Educación', line=dict(color=colors['accent']), mode='lines+markers', marker=dict(size=8, color=colors['accent']))
            ])
            figure.update_layout(
                title='Evolución de Indicadores de Calidad de Vida'
            )
        elif tipo == 'criminalidad':
            figure = go.Figure(data=[
                go.Scatter(x=datos['Año'], y=datos['Tasa de Criminalidad (por 100,000 hab.)'], name='Tasa de Criminalidad', line=dict(color=colors['primary']), mode='lines+markers', marker=dict(size=8, color=colors['primary']))
            ])
            figure.update_layout(
                title='Evolución de la Tasa de Criminalidad en Chile'
            )
        else:
            raise ValueError(f"Tipo de gráfico no reconocido: {tipo}")
        
        # Configuración común para todos los gráficos
        figure.update_layout(
            font_family="Roboto",
            legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5),
            plot_bgcolor='white',
            paper_bgcolor='white',
            xaxis=dict(gridcolor='lightgrey'),
            yaxis=dict(gridcolor='lightgrey')
        )
        
        return dcc.Graph(id={'type': 'graph', 'index': id}, figure=figure)
    except Exception as e:
        return html.Div(f"Error al crear el gráfico: {str(e)}")

def create_layout(app):
    return html.Div([
        Encabezado(app),
        html.Div([
            html.Div([
                crear_resumen_ejecutivo("""
                El presente informe analiza en profundidad la macroeconomía, los sectores productivos, el comercio internacional, 
                los indicadores sociales y las políticas públicas de Chile. El análisis revela una situación crítica en la economía 
                y sociedad chilena, sugiriendo la necesidad urgente de reformas estructurales tales como:
                """, [
                    html.Ul([
                        html.Li("Implementar políticas que fomenten la libertad económica y estimulen el crecimiento del PIB."),
                        html.Li("Mejorar la calidad y accesibilidad de los sistemas de salud y educación."),
                        html.Li("Reforzar las políticas de seguridad pública para reducir la tasa de criminalidad."),
                        html.Li("Desarrollar estrategias para aumentar el poder adquisitivo de los ciudadanos."),
                    ])
                ])
            ], className="executive-summary-container content-section"),
            
            crear_seccion_contenido("Libertad Económica y Crecimiento del PIB", [
                html.P("""
                La relación entre la libertad económica y el crecimiento del PIB en Chile muestra una tendencia preocupante. 
                La disminución de la libertad económica parece estar teniendo un impacto negativo en el crecimiento económico del país.
                """, className="analysis-text"),
                crear_grafico('grafico-libertad-pib', 'libertad-pib', df_summary)
            ]),
            
            crear_seccion_contenido("Indicadores de Calidad de Vida", [
                html.P("""
                Los indicadores de calidad de vida en Chile muestran una tendencia preocupante. Se observa un deterioro 
                generalizado en la calidad de vida de los chilenos, a pesar del supuesto progreso económico.
                """, className="analysis-text"),
                crear_grafico('grafico-calidad-vida', 'calidad-vida', df_summary)
            ]),
            
            crear_seccion_contenido("Criminalidad y Seguridad", [
                html.P("""
                La tasa de criminalidad en Chile ha aumentado de manera alarmante. Este aumento significativo en la 
                criminalidad sugiere un deterioro en la seguridad pública y plantea serias preguntas sobre la efectividad 
                de las políticas de seguridad actuales.
                """, className="analysis-text"),
                crear_grafico('grafico-criminalidad', 'criminalidad', df_summary)
            ]),
        ], className="page-content"),
        html.Footer([
            html.Div([
                html.A(html.Img(src=app.get_asset_url("icons/whatsapp.png"), className="social-icon"), href="https://wa.me/56933293943?text=Hola%20Miguel", target="_blank"),
                html.A(html.Img(src=app.get_asset_url("icons/email.png"), className="social-icon"), href="mailto:mortizcoilla@gmail.com?subject=Contacto%20desde%20la%20página%20web&body=Hola%20Miguel,", target="_blank"),
                html.A(html.Img(src=app.get_asset_url("icons/github.png"), className="social-icon"), href="https://github.com/mortizcoilla", target="_blank"),
                html.A(html.Img(src=app.get_asset_url("icons/linkedin.png"), className="social-icon"), href="https://www.linkedin.com/in/mortizcoilla", target="_blank"),
                html.A(html.Img(src=app.get_asset_url("icons/microsoft.png"), className="social-icon"), href="https://learn.microsoft.com/es-mx/users/mortizcoilla", target="_blank"),
                html.A(html.Img(src=app.get_asset_url("icons/coursera.png"), className="social-icon"), href="https://www.coursera.org/learner/mortizcoilla", target="_blank"),
            ], className="social-links"),
        ], className="footer")
    ], className="main-container")

# No es necesario un callback específico para esta página,
# ya que no hay interacciones dinámicas en el resumen.

# Si necesitas agregar interactividad en el futuro, puedes hacerlo así:
# @callback(
#     Output({'type': 'graph', 'index': ALL}, 'figure'),
#     Input('some-input', 'value')
# )
# def update_graphs(value):
#     # Lógica para actualizar los gráficos
#     pass