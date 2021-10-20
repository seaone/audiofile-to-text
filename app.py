import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from dash.html.P import P
from dash.html.Select import Select
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

form = dbc.Form(
  id='form',
  children = [
    dbc.Row([
      dbc.Col(
        children = [
          dbc.Input(id='file', type='file')
        ]
      ),

      dbc.Col(
        width='auto',
        children = [
          dbc.Select(
            id="dropdown",
            placeholder='Language',
            options = [
              {"label": "",},
              {"label": "Russian", "value": 'ru'},
              {"label": "English", "value": 'en'},
            ]
          )
        ]
      ),

      dbc.Col(
        width='auto',
        children = [
          dbc.Button(
            id='submit',
            children = ['Process']
          )
        ]
      ),
    ]),
  ]
)

app.layout = dbc.Container(
  style={'padding-top': '64px', 'padding-bottom': '64px'},
  children = [
    dbc.Row(
      style = {'margin-bottom': '48px'},
      children = [
        dbc.Col(
          children = [
            html.H1(style = {'margin-bottom': '24px'}, children = ['Audiofile to text']),
            form
          ]
        )
      ]
    ),

    dbc.Row(
      children = [
        html.Div(
          children = [
            html.H2(
              children=[
                'Result:'
              ]
            ),
            html.P(
              children = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in vulputate nisl. Cras ornare pulvinar dolor non cursus. Fusce scelerisque orci eros, non egestas libero euismod et. Donec molestie quam sed est cursus tincidunt. Nullam laoreet sollicitudin tellus, ac ultricies ante dignissim eu. Praesent auctor viverra porttitor. Curabitur elementum tincidunt enim nec laoreet. Proin pretium nibh nec massa fermentum tempor. Sed commodo metus sit amet faucibus mattis. Quisque vitae fringilla nibh. Pellentesque eleifend augue ac magna pharetra mattis. Nulla nibh tellus, euismod dapibus convallis at, porttitor ac turpis. Duis bibendum mollis placerat. Suspendisse potenti. Nulla ante est, sodales a tempor quis, condimentum id velit. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras consequat elementum velit tempus mattis. Phasellus ultrices sodales orci in facilisis.'
            )
          ]
        ),

        html.Div(
          children = [
            html.H3(
              children=[
                'Keywords:'
              ]
            ),

            html.P(
              children = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
            )
          ]
        )
      ]
    )
  ]
)

if __name__ == '__main__':
  app.run_server(debug=True)
