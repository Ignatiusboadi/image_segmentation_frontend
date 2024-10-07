import dash
from dash import dcc, html, Input, Output, State, callback, dcc, ctx
import dash_bootstrap_components as dbc
import os
import zipfile
import io
import base64

from dash.exceptions import PreventUpdate
from flask import send_file

upload_message = 'Multiple file uploads are allowed. Please place all scans in a folder, select all files, and upload them together.'

app = dash.Dash(__name__, title='IMAGE SEGMENTATION', external_stylesheets=[dbc.themes.SIMPLEX],
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}], update_title=None,
                suppress_callback_exceptions=True, assets_folder='assets', assets_url_path='/assets/')

layout = html.Div(style={'padding-top': '30px', 'background-image': 'url("/assets/brain_imag_bg.webp"',
                         'height': '100vh'}, children=[
    dbc.Row(children=[
        dbc.Col(children=[
            html.H2("Brain Image Tumor Segmentation", className="text-center mb-4",
                    style={'textAlign': 'center', 'font-weight': 'bold', 'color': '#3B1C0A', 'padding-top': '10px',
                           'font-size': '200%'}),
        ], width=11),
        dbc.Col(dbc.Button(id='logout', children='Logout', n_clicks=None))], justify='center'),
    dbc.Container(style={'padding-top': '100px'}, children=[
        dbc.Row(children=[
            dbc.Col(children=[
                dbc.Card([
                    dbc.CardBody(style={'background-color': 'GhostWhite'}, children=[
                        dbc.Label("Upload Folder", html_for="upload-files"),
                        dbc.Card([
                            dbc.CardBody(style={'textAlign': 'center', }, children=[
                                dcc.Upload(id='upload-files',
                                           children=html.Div([
                                               'Drag and Drop or ', html.A('Select Files')]),
                                           multiple=True,
                                           style={'width': '100%', 'height': '60px',
                                                  'lineHeight': '60px', 'borderWidth': '1px',
                                                  'borderStyle': 'dashed', 'borderRadius': '5px',
                                                  'textAlign': 'center',
                                                  'font-family': 'Lucida Console'}), ])]),
                        html.Br(),
                        html.Em(upload_message, style={'color': 'green'}),
                        html.Br(),
                        dbc.Row(children=[dbc.Col(children=[
                            dbc.Button("Segment Scans", id='segment', color="danger",
                                       className='text-center', outline=True,
                                       size='md', style={'padding-left': '45px',
                                                         'padding-right': '45px'}), ],
                            width={'offset': 4},
                            style={'padding-left': '25px', 'padding-right': '25px'})],
                            justify="center"),
                    ], ),
                ], ),

            ], width={'size': 6, 'offset': 3})], style={'padding-bottom': '50px'}),
        dbc.Row(style={'padding-top': '30px'}, children=[
            dbc.Col(children=[
                dbc.Card([
                    dbc.CardBody(style={'background-color': 'GhostWhite'}, children=[
                        dbc.Label("", html_for="upload-files"),
                        dbc.Card([
                            dbc.CardBody(style={'textAlign': 'center', }, children=[
                                dbc.Button("Download segmented scans", id='segment', color="success",
                                           outline=True, className="mt-1", size='md',
                                           style={'padding-left': '45px', 'padding-right': '45px'}), ])]),
                    ], ), ], ),

            ], width={'size': 6, 'offset': 3})]),
    ], fluid=True)])


@callback(Output('url', 'pathname'),
          Output('token', 'data'),
          Output('logout', 'n_clicks'),
          Input('logout', 'n_clicks'))
def log_out(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    if n_clicks:
        return '/', None, None


if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
