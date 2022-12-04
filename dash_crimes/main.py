import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)

# -------------------------------------------------------------------------------------------------
# Import Data
df = pd.read_csv('crimedata.csv')
df.fillna(0, inplace=True)
df['total_crimes'] = df.murders + df.rapes + df.robberies + df.assaults + df.burglaries + df.larcenies + \
                     df.autoTheft + df.arsons
df['crime_per_person'] = df['total_crimes'] / df['population']
df['household_size'] = df['householdsize'].round(0)

for ct in ['murders', 'rapes', 'robberies', 'assaults', 'burglaries', 'larcenies', 'autoTheft', 'arsons']:
    df[f'{ct}_per_person'] = df[ct] / df['population']

fig7 = px.scatter(
    df,
    x='PolicCars',
    y='crime_per_person'
)

fig7.update_layout(
    title=dict(
        text='<b>Percentage of Police Cars vs. Average Crimes Number on Person</b>',
        x=0.5,
        font_size=20
    ),
    xaxis=dict(
        title='Police Cars',
    ),
    yaxis=dict(
        title='Crimes/Person'
    ),
    paper_bgcolor='#f3fcff'
)
# -------------------------------------------------------------------------------------------------
# App layout
colors = {
    'background': '#f3fcff',
    'text': '#1c9cce'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Crimes in US Communities Analyse',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(style={'padding': '30px'}, children=[
        html.P('State:'),
        dcc.Dropdown(
            id='dropdown1',
            options=df.state.unique(),
            value='NY',
            clearable=False,
            style={'marginBottom': '10px', 'width': '50%'}
        ),
        dcc.Graph(
            id='graph1'
        ),
    ]),

    html.Div(style={'padding': '30px'}, children=[
        html.P('State:'),
        dcc.Dropdown(
            id='dropdown2',
            options=df.state.unique(),
            value='NY',
            clearable=False,
            style={'marginBottom': '10px', 'width': '50%'}
        ),
        html.P('Community:'),
        dcc.Dropdown(
            id='dropdown3',
            options=[],
            value='NewYorkcity',
            clearable=False,
            style={'marginBottom': '10px', 'width': '50%'}
        ),
        dcc.Graph(
            id='graph2'
        ),
    ]),

    html.Div(style={'padding': '30px'}, children=[
        html.P('Employment Status:'),
        dcc.Dropdown(
            id='dropdown4',
            options=['Employed', 'Unemployed'],
            value='Employed',
            clearable=False,
            style={'marginBottom': '10px', 'width': '50%'}
        ),
        dcc.Graph(
            id='graph3'
        ),
    ]),

    html.Div(style={'padding': '30px'}, children=[
        html.P('Crime Type:'),
        dcc.Dropdown(
            id='dropdown5',
            options=['murders', 'rapes', 'robberies', 'assaults', 'burglaries', 'larcenies', 'autoTheft', 'arsons'],
            value='murders',
            clearable=False,
            style={'marginBottom': '10px', 'width': '50%'}
        ),
        dcc.Graph(
            id='graph4'
        ),
    ]),

    html.Div(style={'padding': '30px'}, children=[
        html.P('Born status:'),
        dcc.Dropdown(
            id='dropdown6',
            options=['Foreign Born', 'Same State'],
            value='Foreign Born',
            clearable=False,
            style={'marginBottom': '10px', 'width': '50%'}
        ),
        dcc.Graph(
            id='graph5'
        ),
    ]),

    html.Div(style={'padding': '30px'}, children=[
        html.P('Police Race Percentage:'),
        dcc.Dropdown(
            id='dropdown7',
            options=['White', 'Black', 'Hispano', 'Asian'],
            value='White',
            clearable=False,
            style={'marginBottom': '10px', 'width': '50%'}
        ),
        dcc.Graph(
            id='graph6'
        ),
    ]),

    html.Div(style={'padding': '30px'}, children=[
        dcc.Graph(
            id='graph7',
            figure=fig7
        ),
    ]),
])


# -------------------------------------------------------------------------------------------------
# Callbacks
@app.callback(
    Output('graph1', 'figure'),
    Input('dropdown1', 'value')
)
def update_state(state):
    df1 = df.groupby('state').agg(
        {'murders': 'sum', 'rapes': 'sum', 'robberies': 'sum', 'assaults': 'sum', 'burglaries': 'sum',
         'larcenies': 'sum', 'autoTheft': 'sum', 'arsons': 'sum'}).loc[state].reset_index()

    fig = px.bar(
        df1,
        x='index',
        y=state
    )

    fig.update_layout(
        title=dict(
            text='<b>Number of Crimes of Each Type</b>',
            x=0.5,
            font_size=20
        ),
        xaxis=dict(
            title='Crimes type'
        ),
        yaxis=dict(
            title='Crimes number'
        ),
        paper_bgcolor='#f3fcff'
    )

    return fig


@app.callback(
    Output('dropdown3', 'options'),
    Input('dropdown2', 'value')
)
def update_dropdown(state):
    return df[df['state'] == state]['communityName'].unique()


@app.callback(
    Output('graph2', 'figure'),
    [Input('dropdown2', 'value'),
     Input('dropdown3', 'value')]
)
def update_community(state, community):
    df1 = df[df['communityName'] == community].iloc[0][
        ['racepctblack', 'racePctWhite', 'racePctAsian', 'racePctHisp']].reset_index()

    target = df1.columns[1]

    fig = px.pie(
        df1,
        values=target,
        names=['Black', 'White', 'Asian', 'Hispano']
    )

    fig.update_layout(
        title=dict(
            text='<b>Community Races</b>',
            x=0.5,
            font_size=20
        ),
        paper_bgcolor='#f3fcff'
    )

    return fig


@app.callback(
    Output('graph3', 'figure'),
    Input('dropdown4', 'value')
)
def update_employment(status):
    if status == 'Unemployed':
        target = 'PctUnemployed'
        title = 'Percentage of Unemployed'
    else:
        target = 'PctEmploy'
        title = 'Percentage of Employed'

    fig = px.scatter(
        df,
        x=target,
        y='crime_per_person'
    )

    fig.update_layout(
        title=dict(
            text='<b>Employed(Unemployed) percentage vs. Average Crimes Number on Person</b>',
            x=0.5,
            font_size=20
        ),
        xaxis=dict(
            title=title,
        ),
        yaxis=dict(
            title='Crimes/Person'
        ),
        paper_bgcolor='#f3fcff'
    )

    return fig


@app.callback(
    Output('graph4', 'figure'),
    Input('dropdown5', 'value')
)
def update_crime_type(crime_type):
    fig = px.scatter(
        df,
        x='PctNotSpeakEnglWell',
        y=f'{crime_type}_per_person'
    )

    fig.update_layout(
        title=dict(
            text='<b>Percentage of bad English speakers vs. Average Crimes Number on Person</b>',
            x=0.5,
            font_size=20
        ),
        xaxis=dict(
            title='Percentage of bad English speakers',
        ),
        yaxis=dict(
            title='Crimes/Person'
        ),
        paper_bgcolor='#f3fcff'
    )

    return fig


@app.callback(
    Output('graph5', 'figure'),
    Input('dropdown6', 'value')
)
def update_born_place(born):
    if born == 'Foreign Born':
        target = 'PctForeignBorn'
        title = 'Percentage Foreign Born'
    else:
        target = 'PctBornSameState'
        title = 'Percentage Born Same State'

    fig = px.scatter(
        df,
        x=target,
        y='crime_per_person'
    )

    fig.update_layout(
        title=dict(
            text='<b>Percentage of born status vs. Average Crimes Number on Person</b>',
            x=0.5,
            font_size=20
        ),
        xaxis=dict(
            title=title,
        ),
        yaxis=dict(
            title='Crimes/Person'
        ),
        paper_bgcolor='#f3fcff'
    )

    return fig


@app.callback(
    Output('graph6', 'figure'),
    Input('dropdown7', 'value')
)
def update_police_race(police_race):
    if police_race == 'White':
        target = 'PctPolicWhite'
        title = 'Percentage of White Police'
    elif police_race == 'Black':
        target = 'PctPolicBlack'
        title = 'Percentage of Black Police'
    elif police_race == 'Hispano':
        target = 'PctPolicHisp'
        title = 'Percentage of Hispano Police'
    else:
        target = 'PctPolicAsian'
        title = 'Percentage of Asian Police'

    fig = px.scatter(
        df,
        x=target,
        y='crime_per_person'
    )

    fig.update_layout(
        title=dict(
            text='<b>Percentage of Race Police vs. Average Crimes Number on Person</b>',
            x=0.5,
            font_size=20
        ),
        xaxis=dict(
            title=title,
        ),
        yaxis=dict(
            title='Crimes/Person'
        ),
        paper_bgcolor='#f3fcff'
    )

    return fig


# -------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
