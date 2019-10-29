#scanpy packages
import numpy as np
import pandas as pd
import os
import re

#app dependencies
import json
from textwrap import dedent as d

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

#this is a new package for graphic features
import plotly.graph_objs as go

############################################# code here will assign clusters and upload the coordinates onto the graph
master = pd.read_csv('./combined.csv') # meta data
exp_matrix = pd.read_csv('./expression_matrix.csv') # expression matrix

all_data = pd.concat([master,exp_matrix], axis=1)

#sort the values based on the louvain column
master_sorted = master.sort_values(by=['louvain'])

#### Get louvain values as string

master['louvain'] = master['louvain'].apply(str)
master.dtypes

master_sorted['louvain'] = master_sorted['louvain'].apply(str)
master_sorted.dtypes

###############################################################

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

###############################################################

app.layout = html.Div([
        html.Div([
            html.H3('Louvain Cluster'),
            dcc.Graph(
            id='g1', figure={
                'data': [
                    go.Scatter(
                        x=master_sorted[master_sorted['louvain'] == i]['0'],
                        y=master_sorted[master_sorted['louvain'] == i]['1'],
                        text=master_sorted[master_sorted['louvain'] == i]['STAGE'],
                        mode='markers',
                        opacity=1,
                        marker={
                            'size': 5,
                        },
                        name=i
                    ) for i in master_sorted.louvain.unique()
                ],
                'layout': go.Layout(
                    xaxis={'title': 'UMAP1'},
                    yaxis={'title': 'UMAP2'},
                    #legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            })
        ]),
        html.Div([
            html.H3('Gene Expression'),
            dcc.Graph(id='g2'),
    
        html.Div([  ###### this add the selection option below the gene ############################## expression graph
            dcc.Input(id='my-id', value='enter a gene ID', type='text'),
          html.H3('Try these genes: VGLL4L, TWIST2, ID1, CLDNG, GSC, MIXL1'),
            ])])
        ]) 
        
  
@app.callback(
    Output(component_id='g2', component_property='figure'),
    [Input(component_id='my-id', component_property='value')]
)
def update_graph(gene):
    return {
        'data': [
            go.Scatter(
                x=all_data['0'],
                y=all_data['1'],
                text=['STAGE'],
                mode='markers',
                opacity=1,
                marker={
                    'size': 5,
                    'color': all_data[gene],
                    'colorscale': 'Viridis',
                    'showscale': True
                }
               
            ) 
        ],
        'layout': go.Layout(
            xaxis={'title': 'UMAP1'},
            yaxis={'title': 'UMAP2'},
            showlegend=False,
            hovermode='closest'
            )
        }
    
    
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})
     

 
if __name__ == '__main__':
    app.run_server(debug=True)