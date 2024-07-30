from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from pages import resumen, macroeconomia, sectorial, comercio, sociedad, politicas
from utils import Encabezado, Footer

app = Dash(__name__, 
           suppress_callback_exceptions=True,
           meta_tags=[{"name": "viewport", "content": "width=device-width"}],
           assets_folder='assets')
app.title = "Informe Económico de Chile"
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    Encabezado(app),
    html.Div(id='page-content'),
    Footer(app)
])

@callback(Output('page-content', 'children'),
          Input('url', 'pathname'))
def display_page(pathname):
    try:
        if pathname == "/informe-economico-chile/macroeconomia":
            return macroeconomia.create_layout(app)
        elif pathname == "/informe-economico-chile/sectorial":
            return sectorial.create_layout(app)
        elif pathname == "/informe-economico-chile/comercio":
            return comercio.create_layout(app)
        elif pathname == "/informe-economico-chile/sociedad":
            return sociedad.create_layout(app)
        elif pathname == "/informe-economico-chile/politicas":
            return politicas.create_layout(app)
        else:
            return resumen.create_layout(app)
    except Exception as e:
        return html.Div([
            html.H1("Error"),
            html.P(f"Se produjo un error al cargar la página: {str(e)}")
        ])

@callback(Output('subtitle', 'children'),
          Input('url', 'pathname'))
def update_subtitle(pathname):
    try:
        if pathname == "/informe-economico-chile/resumen" or pathname == "/":
            return "Por Miguel Ortiz C."
        elif pathname == "/informe-economico-chile/macroeconomia":
            return "Macroeconomía de Chile: Más allá de las cifras"
        elif pathname == "/informe-economico-chile/sectorial":
            return "Análisis Sectorial: Desafíos y Oportunidades"
        elif pathname == "/informe-economico-chile/comercio":
            return "Comercio Internacional: Tendencias y Perspectivas"
        elif pathname == "/informe-economico-chile/sociedad":
            return "Indicadores Sociales: El Rostro Humano de la Economía"
        elif pathname == "/informe-economico-chile/politicas":
            return "Políticas Públicas: Moldeando el Futuro Económico"
        else:
            return "Por Miguel Ortiz C."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run_server(debug=True)