from dash import html
import dash_bootstrap_components as dbc
from main import app
from components import form_component

if __name__ == '__main__':
  app.layout = dbc.Container(
    style = {'paddingTop': '64px', 'paddingBottom': '64px', 'maxWidth': '720px'},
    children = [
      dbc.Row(
        style = {'marginBottom': '24px'},
        children = [
          dbc.Col(
            children = [
              html.H1(children = ['Audiofile to text']),
            ]
          ),
        ]
      ),
      form_component.render()
    ]
  )

  app.run_server(debug=True)
