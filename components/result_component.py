from dash import html

def render(text, keywords):
  return (
    html.Div(
      children = [
        html.H2(
          children = [
            'Result:'
          ]
        ),
        html.P(
          id = 'text',
          children = [text]
        )
      ]
    ),

    html.Div(
      children = [
        html.H3(
          children = [
            'Keywords:'
          ]
        ),

        html.P(
          id = 'keywords',
          children = [keywords]
        )
      ]
    )
  )
  