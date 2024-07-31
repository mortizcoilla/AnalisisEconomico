from dash import html, dcc
import pandas as pd

def Encabezado(app):
    return html.Header([
        html.Div([
            html.Div([
                html.H1("Análisis Económico de Chile", className="main-title"),
                html.H2(id="subtitle", className="subtitle"),
            ], className="header-title-container"),
            html.Button("☰", className="menu-toggle", id="menu-toggle"),
        ], className="header-content"),
        html.Nav([
            dcc.Link("Resumen", href="/informe-economico-chile/resumen", className="nav-link"),
            dcc.Link("Macroeconomía", href="/informe-economico-chile/macroeconomia", className="nav-link"),
            dcc.Link("Sectorial", href="/informe-economico-chile/sectorial", className="nav-link"),
            dcc.Link("Comercio", href="/informe-economico-chile/comercio", className="nav-link"),
            dcc.Link("Sociedad", href="/informe-economico-chile/sociedad", className="nav-link"),
            dcc.Link("Políticas Públicas", href="/informe-economico-chile/politicas", className="nav-link"),
        ], className="nav-menu", id="nav-menu")
    ], className="header")

def obtener_menu():
    return html.Nav([
        dcc.Link("Resumen", href="/informe-economico-chile/resumen", className="nav-link"),
        dcc.Link("Macroeconomía", href="/informe-economico-chile/macroeconomia", className="nav-link"),
        dcc.Link("Sectorial", href="/informe-economico-chile/sectorial", className="nav-link"),
        dcc.Link("Comercio", href="/informe-economico-chile/comercio", className="nav-link"),
        dcc.Link("Sociedad", href="/informe-economico-chile/sociedad", className="nav-link"),
        dcc.Link("Políticas Públicas", href="/informe-economico-chile/politicas", className="nav-link"),
    ], className="nav-menu")

def crear_tabla_dash(df):
    """ Retorna una definición de tabla HTML de Dash para un DataFrame de Pandas """
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
            ]) for i in range(len(df))
        ])
    ], className="data-table")

def Footer(app):
    return html.Footer([
        html.Div([
            html.A(html.Img(src=app.get_asset_url("icons/whatsapp.png"), className="social-icon"), href="https://wa.me/56933293943?text=Hola%20Miguel", target="_blank"),
            html.A(html.Img(src=app.get_asset_url("icons/email.png"), className="social-icon"), href="mailto:mortizcoilla@gmail.com?subject=Contacto%20desde%20la%20página%20web&body=Hola%20Miguel,", target="_blank"),
            html.A(html.Img(src=app.get_asset_url("icons/github.png"), className="social-icon"), href="https://github.com/mortizcoilla", target="_blank"),
            html.A(html.Img(src=app.get_asset_url("icons/linkedin.png"), className="social-icon"), href="https://www.linkedin.com/in/mortizcoilla", target="_blank"),
            html.A(html.Img(src=app.get_asset_url("icons/microsoft.png"), className="social-icon"), href="https://learn.microsoft.com/es-mx/users/mortizcoilla", target="_blank"),
            html.A(html.Img(src=app.get_asset_url("icons/coursera.png"), className="social-icon"), href="https://www.coursera.org/learner/mortizcoilla", target="_blank"),
        ], className="social-links"),
    ], className="footer")

def crear_seccion_contenido(titulo, contenido, clase_adicional=""):
    return html.Div([
        html.H2(titulo, className="section-title"),
        html.Div(contenido, className="section-content")
    ], className=f"content-section {clase_adicional}".strip())

def crear_resumen_ejecutivo(texto, contenido_adicional=None):
    contenido = [
        html.P(texto, className="executive-summary-text")
    ]
    if contenido_adicional:
        contenido.extend(contenido_adicional)
    return html.Div(contenido, className="executive-summary-box")

def crear_contenedor_grafico(titulo, grafico, analisis):
    return html.Div([
        html.H3(titulo, className="graph-title"),
        html.P(analisis, className="analysis-text"),
        dcc.Graph(figure=grafico)
    ], className="graph-container")