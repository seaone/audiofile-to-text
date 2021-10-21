import os
import base64
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from flask.scaffold import F
from main import app
from utils import recognize, kw
from components import result_component

UPLOAD_DIRECTORY = 'uploads'

def render():
  return dbc.Row(
    children = [
      dbc.Col(
        children = [
          dbc.Form(
            id = 'form',
            children = [
              dbc.Row(
                children = [
                  dbc.Col(
                    children = [
                      dcc.Upload(
                        id = 'upload-data',
                        accept = 'audio/wav',
                        children = [
                          html.Div()
                        ],
                        style = {
                          'width': '100%',
                          'height': '96px',
                          'lineHeight': '96px',
                          'borderWidth': '1px',
                          'borderStyle': 'dashed',
                          'borderColor': '#ced4da',
                          'borderRadius': '.25rem',
                          'textAlign': 'center',
                          'cursor': 'pointer',
                        }
                      )
                    ]
                  )
                ]
              ),

              dbc.Row(
                style = {
                  'marginTop': '24px'
                },
                children = [
                  dbc.Col(
                    width = 'auto',
                    children = [
                      dbc.Select(
                        id = 'dropdown',
                        placeholder = 'Language',
                        size = 'lg',
                        options = [
                          {'label': '',},
                          {'label': 'Russian', 'value': 'ru'},
                          {'label': 'English', 'value': 'en'},
                        ]
                      )
                    ]
                  ),

                  dbc.Col(
                    width = 'auto',
                    children = [
                      dbc.Button(
                        id = 'submit-button',
                        type = 'button',
                        size = 'lg',
                        children = ['Process']
                      )
                    ]
                  )
                ]
              ),
              
              html.Div(
                id = 'warning',
                style = {
                  'marginTop': '24px'
                }  
              )
            ]
          ),

          html.Div(
            id = 'result',
            style = {
              'marginTop': '48px'
            }
          )
        ]
      )
    ]
  )

@app.callback(
  Output(component_id = 'result', component_property = 'children'),
  Output(component_id = 'warning', component_property = 'children'),
  Input(component_id = 'submit-button', component_property = 'n_clicks'),
  Input(component_id = 'dropdown', component_property = 'value'),
  Input(component_id = 'upload-data', component_property = 'contents'),
  State(component_id = 'dropdown', component_property = 'value'),
  State(component_id = 'upload-data', component_property = 'contents')
)
def handle_submit(submitInput, langInput, fileInput, langState, fileState):
  ctx = dash.callback_context
  result = ''
  keywords = ''

  if ctx.triggered[0]['prop_id'].split('.')[0] == 'dropdown' or ctx.triggered[0]['prop_id'].split('.')[0] == 'upload-data':
    return '', ''

  if submitInput:
    if fileState and langState:
      pathToFile = os.path.join(os.getcwd(), UPLOAD_DIRECTORY, 'audio.wav')
      saveFile(fileState, pathToFile)
      result = recognize.recognize(pathToFile, langState)
      keywords = getKeywords(result, langState)

      return result_component.render(result, keywords), ''

    else:
      return '', dbc.Alert(color = 'warning', children = ['Please select a file and choose a language'])
  
  return '', ''

@app.callback(
  Output(component_id = 'upload-data', component_property = 'children'),
  Input(component_id = 'upload-data', component_property = 'filename')
)
def handle_upload_file(filename):
  if filename:
    return filename

  default = (
    'Drag and Drop or ', 
    html.A(
      children=[
        'Select Files'
      ],
      style={
        'fontWeight': 700
      }
    )
  )

  return default



def saveFile(file, path):
  data = file.encode('utf8').split(b';base64,')[1]
  with open(path, 'wb') as fp:
    fp.write(base64.decodebytes(data))

  return os.path.join(os.getcwd(), UPLOAD_DIRECTORY, 'audio.wav')

  

def getKeywords(text, lang):
  if text != '':
    keywordList = []

    for item in kw.extract(text, lang):
      keywordList.append(item[0])

    return ', '.join(keywordList)

  return ''