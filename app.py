from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
from pages import resumen, macroeconomia, sectorial, comercio, sociedad, politicas
from utils import Encabezado, Footer

app = Dash(__name__, 
           meta_tags=[{"name": "viewport", "content": "width=device-width"}],
           suppress_callback_exceptions=True,
           assets_folder='assets')
app.title = "Informe Económico de Chile"
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    Encabezado(app),
    html.Div(id='page-content'),
    Footer(app)
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
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

@app.callback(Output('subtitle', 'children'),
              [Input('url', 'pathname')])
def update_subtitle(pathname):
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

@app.callback(
    Output("nav-menu", "className"),
    [Input("menu-toggle", "n_clicks")],
    [State("nav-menu", "className")]
)
def toggle_menu(n_clicks, current_class):
    if n_clicks:
        if current_class == "nav-menu":
            return "nav-menu active"
        else:
            return "nav-menu"
    return current_class

# Inicializa los callbacks de todas las páginas aquí
for page in [macroeconomia, sectorial, comercio, sociedad, politicas]:
    if hasattr(page, 'init_callbacks'):
        page.init_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)