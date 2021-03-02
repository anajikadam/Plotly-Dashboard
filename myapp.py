# Import All Required ibrary
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Dash Enterprise'

colors = {
    'background': '#111111',
    'bodyColor':'#F2DFCE',
    'text': '#7FDBFF'
}
def get_page_heading_style():
    return {'backgroundColor': colors['background']}


def get_page_heading_title():
    return html.H1(children='Hello New Web Dashbord with Plotly',
                                        style={
                                        'textAlign': 'center',
                                        'color': colors['text']
                                    })

def get_page_heading_subtitle():
    return html.Div(children='Visualize of data generated from sources all over the world.',
                                         style={
                                             'textAlign':'center',
                                             'color':colors['text']
                                         })

def generate_page_header():
    main_header =  dbc.Row(
                            [
                                dbc.Col(get_page_heading_title(),md=12)
                            ],
                            align="center",
                            style=get_page_heading_style()
                        )
    subtitle_header = dbc.Row(
                            [
                                dbc.Col(get_page_heading_subtitle(),md=12)
                            ],
                            align="center",
                            style=get_page_heading_style()
                        )
    header = (main_header,subtitle_header)
    return header


def generate_card_content(card_header,card_value,overall_value):
    card_head_style = {'textAlign':'center','fontSize':'150%'}
    card_body_style = {'textAlign':'center','fontSize':'200%'}
    card_header = dbc.CardHeader(card_header,style=card_head_style)
    card_body = dbc.CardBody(
        [
            html.H5(f"{int(card_value):,}", className="card-title",style=card_body_style),
            html.P(
                "Worlwide: {:,}".format(overall_value),
                className="card-text",style={'textAlign':'center'}
            ),
        ]
    )
    card = [card_header,card_body]
    return card

def generate_cards(cntry='US'):
    conf_overall_total = 56
    dead_overall_total = 96
    recv_overall_total = 100

    conf_cntry_total = 41
    dead_cntry_total = 51
    recv_cntry_total = 58
    cards = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(dbc.Card(generate_card_content("Recovered",recv_cntry_total,recv_overall_total), color="success", inverse=True),md=dict(size=2,offset=3)),
                    dbc.Col(dbc.Card(generate_card_content("Confirmed",conf_cntry_total,conf_overall_total), color="warning", inverse=True),md=dict(size=2)),
                    dbc.Col(dbc.Card(generate_card_content("Dead",dead_cntry_total,dead_overall_total),color="dark", inverse=True),md=dict(size=2)),
                ],
                className="mb-4",
            ),
        ],id='card1'
    )
    return cards

def fig_world_trend():
    
    year=['2015', '2016', '2017','2018', '2019', '2020']
    fig = go.Figure(data=[
        go.Bar(name='Male', x=year, y=[20, 14, 23,25,21,23]),
        go.Bar(name='Female', x=year, y=[12, 18, 29,25,28,29])
    ])
    # Change the bar mode
    fig.update_layout(
    title={
        'text': "Plot Title",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
    fig.update_layout(barmode='group')
    return fig
def graph1():
    return dcc.Graph(id='graph1',figure=fig_world_trend())

def fig_world_trend1():
    fig = make_subplots(rows=1, cols=2)
    fig.add_trace(
        go.Scatter(x=[1, 2, 3], y=[4, 5, 6],name="Name of Trace 1" ),
        row=1, col=1
        
    )
    fig.add_trace(
        go.Scatter(x=[20, 30, 40], y=[50, 60, 70],name="Name of Trace 1" ),
        row=1, col=2
    )
    fig.update_layout(height=600, width=800, title_text="Side By Side Subplots")
    # fig.show()
    return fig

def graph2():
    return dcc.Graph(id='graph2',figure=fig_world_trend1())

def fig_world_trend2():
    fig = make_subplots(
        rows=2, cols=2,
        specs=[[{"type": "xy"}, {"type": "polar"}],
            [{"type": "domain"}, {"type": "scene"}]],
        )

    fig.add_trace(go.Bar(y=[2, 3, 1]),
                row=1, col=1)
    fig.add_trace(go.Barpolar(theta=[0, 45, 90], r=[2, 3, 1]),
                row=1, col=2)
    fig.add_trace(go.Pie(values=[2, 3, 1]),
                row=2, col=1)
    fig.add_trace(go.Scatter3d(x=[2, 3, 1], y=[0, 0, 0],
                            z=[0.5, 1, 2], mode="lines"),
                row=2, col=2)
    fig.update_layout(height=700, showlegend=False)
    # fig.show()
    return fig

def graph3():
    return dcc.Graph(id='graph3',figure=fig_world_trend2())

def generate_inp():
    app = html.Div([
        html.H6("Change the value in the text box to see callbacks in action!"),
        html.Div(["Input: ",
                dcc.Input(id='my-input', value='initial value', type='text')]),
        html.Br(),
        html.Div(id='my-output'),
    ])
    return app
def generate_layout():
    page_header = generate_page_header()
    layout = dbc.Container(
        [   
            page_header[0],
            page_header[1],
            html.Hr(),
            generate_cards(),
            html.Hr(),
            dbc.Row(
                [                
                    
                    dbc.Col(graph1(),md=dict(size=6,offset=3))
        
                ],
                align="center",

            ),
            html.Hr(),
            dbc.Row(
                [                
                    
                    dbc.Col(graph3(),md=dict(size=6,offset=3))
        
                ],
                align="center",

            ),
            html.Hr(),
            dbc.Row([   
                    dbc.Col(graph2(),md=dict(size=6,offset=3))
                ],
                align="center",
            ),
            generate_inp()
        ],fluid=True,style={'backgroundColor': colors['bodyColor']}
    )
    return layout



app.layout = generate_layout()
@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)

if __name__ == '__main__':
    # app.run_server('0.0.0.0',debug=True,port=8051)
    app.run_server('0.0.0.0',debug=True)

