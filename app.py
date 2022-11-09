import os
import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from charts import create_table, set_layout
import plotly.graph_objects as go
import dash_trich_components as dtc


app = Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
)
server = app.server

theme_toggle = dtc.ThemeToggle(
        bg_color_dark='#232323',
        # icon_color_dark='#EDC575',
        # bg_color_light='#07484E',
        icon_color_light='#C8DBDC',
        tooltip_text='Toggle light/dark theme'
    )
theme_switch = html.Div(theme_toggle, className='theme__switcher')
header = html.Div([
        html.H1('Filter set'),
        html.P('We create different types of filters that work together'),
], className='dash__header')

footer = html.Div([
    html.P('Created by:', style={}),

], className='dash__footer')



df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')

fig = go.Figure(data=go.Choropleth(
    locations = df['CODE'],
    z = df['GDP (BILLIONS)'],
    text = df['COUNTRY'],
    colorscale = 'Blues',

    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    # marker_line_width=0.5,
    # colorbar_tickprefix = '$',
    # colorbar_title = 'GDP<br>Billions US$',
))
_ = fig.update_traces(showscale=False)
fig.update_layout(
    title_text='2014 Global GDP',
    showlegend=False,
    dragmode=False,
    clickmode='event+select',
    geo=dict(

        showframe=False,
        showcoastlines=False,
        projection_type='patterson'
    ),

)


app.layout = html.Div([
                    header,
                    theme_switch,
                    html.Div([
                        html.Div([
                                    dcc.RangeSlider(id='year_slider',
                                                    min=2015,
                                                    max=2022,
                                                    value=[2017, 2022],
                                                    marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in
                                                           range(2015, 2023)},
                                                    ),
                                    dbc.RadioItems(
                                        id="month_selector",
                                        options=[{'label': 'Jan', 'value': 'Jan'},
                                                 {'label': 'Feb', 'value': 'Feb'},
                                                 {'label': 'Mar', 'value': 'Mar'},
                                                 {'label': 'Apr', 'value': 'Apr'},
                                                 {'label': 'May', 'value': 'May'},
                                                 {'label': 'Jun', 'value': 'Jun'},
                                                 {'label': 'Jul', 'value': 'Jul'},
                                                 {'label': 'Aug', 'value': 'Aug'},
                                                 {'label': 'Sep', 'value': 'Sep'},
                                                 {'label': 'Oct', 'value': 'Oct'},
                                                 {'label': 'Nov', 'value': 'Nov'},
                                                 {'label': 'Dec', 'value': 'Dec'},
                                                 {'label': 'All', 'value': 'All'},
                                                 ],
                                        labelClassName="date-group-labels",
                                        labelCheckedClassName="date-group-labels-checked",
                                        inline=True,
                                        value='All',
                                        style={'margin': '0 20px 20px 0'}
                                    ),

                            ], className="dash_filter"),
                            dcc.Graph(figure=fig, config={'displayModeBar': False})
                    ], className='dash__graph_block'),
                    footer

                ], className='dash__wrapper', style={})


# don't run when imported, only when standalone
if __name__ == '__main__':
    port = os.getenv("DASH_PORT", 8053)
    app.run_server(debug=True,  port=port)
