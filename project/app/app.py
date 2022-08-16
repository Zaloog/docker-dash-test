import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from functions import plot_regression

import dash
from dash import dcc, html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Graph(id="regression_plot"),
                html.P(
                    "Standard Deviation", style={"color": "white", "marginLeft": "20px"}
                ),
                dcc.Slider(
                    id="std_slider",
                    min=0,
                    max=40,
                    step=0.5,
                    value=10,
                    marks={i: str(i) for i in range(0, 40, 5)},
                ),
            ]
        ),
    ]
)


@app.callback(
    Output(component_id="regression_plot", component_property="figure"),
    [Input(component_id="std_slider", component_property="value")],
)
def update_regression_plot(std):
    return plot_regression(std)


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
