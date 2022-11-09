import os
import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from charts import create_table, set_layout
import plotly.graph_objects as go
import dash_trich_components as dtc

from styling import PAGE_SIZE


# select the Bootstrap stylesheet2 and figure template2 for the theme toggle here:
template_theme1 = "lumen"
template_theme2 = "darkly"
url_theme1 = dbc.themes.LUMEN
url_theme2 = dbc.themes.DARKLY



# read data
university = pd.read_csv('data/data.csv')

app = Dash(
    __name__, external_stylesheets=[url_theme1, dbc.themes.BOOTSTRAP],
)
server = app.server


@app.callback(
    Output('barchart', 'figure'),

    [Input('table', "data"),
     Input('table', "page_current"),
     Input('table', "page_size"),
    ],
    # [State("university-table", "columns")],
)
def update_table(data, page_current, page_size):
    df = pd.DataFrame(data)
    # sort df with pages
    df = df.iloc[page_current * page_size:(page_current + 1) * page_size]
    row_barchart = go.Figure()
    row_barchart.add_trace(
        go.Bar(
            x=df["Points"][::-1],
            y=df.index,
            orientation="h",
            text=df["Points"][::-1],
            marker_color='#cfdad9',
            textfont=dict(color='black')
        )
    )
    set_layout(row_barchart, heightgraph=len(df) * 42)

    return row_barchart

theme_toggle = dtc.ThemeToggle(
        bg_color_dark='#232323',
        # icon_color_dark='#EDC575',
        # bg_color_light='#07484E',
        icon_color_light='#C8DBDC',
        tooltip_text='Toggle light/dark theme'
    )
theme_switch = html.Div(theme_toggle, className='theme__switcher')
header = html.Div([
        html.H1('Table + Bar'),
        html.P('There is no way to add a bar chart to the table in dash. You can work with Displaying Data Bars, but it looks rather clumsy'),
], className='dash__header')

footer = html.Div([
    html.P('Created by:', style={}),

], className='dash__footer')

app.layout = html.Div([
                    header,
                    theme_switch,
                    html.Div([
                        html.Div([
                            html.Div('Table - Points information ', className="table_name"),
                            html.Div([
                                    create_table(university, tableid='table', page_size=PAGE_SIZE, link_column='Player'),
                                    html.Div(
                                        [
                                            dcc.Graph(id='barchart', config={'displayModeBar': False})], style={'position': 'absolute', 'right': 0, 'top':'42px'}
                                    ),
                                ], style={'display': 'flex', 'position': 'relative', 'width': '100%'})
                        ]),
                    ], className='dash__graph_block'),
                    footer

                ], className='dash__wrapper', style={})


# don't run when imported, only when standalone
if __name__ == '__main__':
    port = os.getenv("DASH_PORT", 8053)
    app.run_server(debug=True,  port=port)
