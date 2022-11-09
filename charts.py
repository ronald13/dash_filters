from dash import dash_table


def create_table(
    df, tableid="datatable",  page_size=5, link_column="Player"
):


    table = dash_table.DataTable(
        id=tableid,
        data=df.to_dict("records"),
        # columns=[{"name": i, "id": i} for i in university.columns],
        columns=[
            {"id": x, "name": x, "presentation": "markdown"}
            if x == link_column
            else {"id": x, "name": x}
            for x in df.columns
        ],
        page_size=page_size,
        page_current=0,
        style_cell={"border": "none", "font-family": "Open Sans"},
        style_data={
            "whiteSpace": "normal",
            "height": "auto",
            # 'font-family': 'Open Sans',
        },
        css=[
            {
                "selector": ".dash-spreadsheet tr th",
                "rule": "height: 15px;",
            },  # set height of header
            {
                "selector": ".dash-spreadsheet tr td",
                "rule": "height: 75px;",
            },  # set height of body rows
            # {
            #     "selector": "tr:first-child",
            #     "rule": "display: none",
            # },  # hide header

        ],
        fill_width=False,
        style_as_list_view=True,
        # style_cell={'padding': '15px'},
        style_header={
            "backgroundColor": "white",
            "fontWeight": "bold",
            "font-size": "12px",
            "borderBottom": "1px solid #e0e0e0",
            # 'fontFamily': 'Open Sans',
        },
        style_header_conditional=[
            {
                "if": {"column_id": "Player"},
                "color": "#0973c0",
            }
        ],
        style_cell_conditional=[
            {"textAlign": "left"},
            {"font-size": "14px"},
            {
                "if": {"column_id": "Player"},
                'min-width':'250px',
                'max-width': 'calc(80% - 300px)',
                "color": "#0973c0",
                "font-family": "Open Sans",
            },
            {
                "if": {"column_id": "Year"},
                "font-family": "Open Sans",
                "min-width": "90px",
                "max-width":"7%",
                "width":"100%",
                "padding": "0 10px 0 0",
            },
            {
                "if": {"column_id": "City"},
                "min-width": "140px",
                "max-width": "10%",
                "width": "100%",

                "padding": "0 10px 0 0",
            },
            {
                "if": {"column_id": "Country"},
                "min-width": "180px",
                "padding": "0 10px 0 0",
                "max-width": "10%",
                "width": "100%",

            },
            {
                "if": {"column_id": "Points"},
                "min-width": "300px",
                "width": "300px",
                "color": "#fff",
                # 'padding-left': '30px',
            },
        ],

    )
    return table

def set_layout(fig, l=0, r=0, t=0, b=0, heightgraph=180):
    fig.update_layout(
        font_family='Open Sans',
        template='plotly_white',
        paper_bgcolor="rgb(0,0,0,0)",
        legend=dict(orientation="h", yanchor="bottom",
                    y=1.0,
                    xanchor="left",
                    x=0),
        margin={'t': t, 'r': r, 'l': l, 'b': b},
        yaxis=dict(
             titlefont_size=5,
             tickfont_size=14,
             zeroline=True, linewidth=6, linecolor='grey',
             visible=False,
             ),
        height=heightgraph,
        width=300,
        xaxis=dict(
            titlefont_size=12,
            tickfont_size=14,
            color='grey',
            showticklabels=False,
            showgrid=False,
        ),
    )
    fig.update_traces(hoverlabel_bgcolor='#ffffff',  hovertemplate='<extra></extra>', textfont=dict(color='black'), texttemplate='%{x:.0f} ')