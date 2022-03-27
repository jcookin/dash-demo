from turtle import colormode
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df_cities = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig_cities = px.bar(df_cities, x="Fruit", y="Amount", color="City", barmode="group")

df_bubbles = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

fig_bubbles = px.scatter(df_bubbles, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

app.layout = html.Div(children=[
    html.H1(children='Dash Demo', id="title", className="app-header"),

    html.Div(children='''
        Dash: A web application framework for your data visualization''',
        id="subtitle",
        className="app-header"),

    dcc.Graph(
        id='cities-graph',
        figure=fig_cities,
    ),
    
    dcc.Graph(
        id="bubbles-graph",
        figure=fig_bubbles
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
