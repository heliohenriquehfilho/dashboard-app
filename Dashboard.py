from ast import fix_missing_locations
from turtle import width
import dash
from dash import dcc
from dash import html
import pandas as pd
from numpy import NaN
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import scipy as sp
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.simplefilter("ignore")

colors = {
    'bg': '#111111',
    'text': '#7FDBFF'
}

flp_2017_jan = pd.read_excel(r"Dados\campus fpolis 2017\janeiro.xlsx")
flp_2017_fev = pd.read_excel(r'Dados\campus fpolis 2017\fevereiro.xlsx')
flp_2017_mar = pd.read_excel(r'Dados\campus fpolis 2017\março.xlsx')
flp_2017_abr = pd.read_excel(r'Dados\campus fpolis 2017\abril.xlsx')
flp_2017_mai = pd.read_excel(r'Dados\campus fpolis 2017\maio.xlsx')
flp_2017_jun = pd.read_excel(r'Dados\campus fpolis 2017\junho.xlsx')
flp_2017_jul = pd.read_excel(r'Dados\campus fpolis 2017\julho.xlsx')
flp_2017_ago = pd.read_excel(r'Dados\campus fpolis 2017\agosto.xlsx')
flp_2017_set = pd.read_excel(r'Dados\campus fpolis 2017\setembro.xlsx')
flp_2017_out = pd.read_excel(r'Dados\campus fpolis 2017\outubro.xlsx')
flp_2017_nov = pd.read_excel(r'Dados\campus fpolis 2017\novembro.xlsx')
flp_2017_dez = pd.read_excel(r'Dados\campus fpolis 2017\dezembro.xlsx')
flp_2017 = pd.concat([flp_2017_jan, flp_2017_fev, flp_2017_mar, flp_2017_abr, flp_2017_mai, flp_2017_jun, flp_2017_jul, flp_2017_ago, flp_2017_set, flp_2017_out, flp_2017_nov, flp_2017_dez]).copy()

flp_2018_jan = pd.read_excel(r'Dados\campus fpolis 2018\janeiro.xlsx')
flp_2018_fev = pd.read_excel(r'Dados\campus fpolis 2018\fevereiro.xlsx')
flp_2018_mar = pd.read_excel(r'Dados\campus fpolis 2018\março.xlsx')
flp_2018_abr = pd.read_excel(r'Dados\campus fpolis 2018\abril.xlsx')
flp_2018_mai = pd.read_excel(r'Dados\campus fpolis 2018\maio.xlsx')
flp_2018_jun = pd.read_excel(r'Dados\campus fpolis 2018\junho.xlsx')
flp_2018_jul = pd.read_excel(r'Dados\campus fpolis 2018\julho.xlsx')
flp_2018_ago = pd.read_excel(r'Dados\campus fpolis 2018\agosto.xlsx')
flp_2018_set = pd.read_excel(r'Dados\campus fpolis 2018\setembro.xlsx')
flp_2018_out = pd.read_excel(r'Dados\campus fpolis 2018\outubro.xlsx')
flp_2018_nov = pd.read_excel(r'Dados\campus fpolis 2018\novembro.xlsx')
flp_2018_dez = pd.read_excel(r'Dados\campus fpolis 2018\dezembro.xlsx')
flp_2018 = pd.concat([flp_2018_jan, flp_2018_fev, flp_2018_mar, flp_2018_abr, flp_2018_mai, flp_2018_jun, flp_2018_jul, flp_2018_ago, flp_2018_set, flp_2018_out, flp_2018_nov, flp_2018_dez]).copy()

flp_2019_jan = pd.read_excel(r'Dados\campus fpolis 2019\janeiro.xlsx')
flp_2019_fev = pd.read_excel(r'Dados\campus fpolis 2019\fevereiro.xlsx')
flp_2019_mar = pd.read_excel(r'Dados\campus fpolis 2019\março.xlsx')
flp_2019_abr = pd.read_excel(r'Dados\campus fpolis 2019\abril.xlsx')
flp_2019_mai = pd.read_excel(r'Dados\campus fpolis 2019\maio.xlsx')
flp_2019_jun = pd.read_excel(r'Dados\campus fpolis 2019\junho.xlsx')
flp_2019_jul = pd.read_excel(r'Dados\campus fpolis 2019\julho.xlsx')
flp_2019_ago = pd.read_excel(r'Dados\campus fpolis 2019\agosto.xlsx')
flp_2019_set = pd.read_excel(r'Dados\campus fpolis 2019\setembro.xlsx')
flp_2019_out = pd.read_excel(r'Dados\campus fpolis 2019\outubro.xlsx')
flp_2019_nov = pd.read_excel(r'Dados\campus fpolis 2019\novembro.xlsx')
flp_2019_dez = pd.read_excel(r'Dados\campus fpolis 2019\dezembro.xlsx')
flp_2019 = pd.concat([flp_2019_jan, flp_2019_fev, flp_2019_mar, flp_2019_abr, flp_2019_mai, flp_2019_jun, flp_2019_jul, flp_2019_ago, flp_2019_set, flp_2019_out, flp_2019_nov, flp_2019_dez]).copy()

flp_2017.loc[(flp_2017.ta < 13)|(flp_2017.ta > 14.2)] = NaN
flp_2017 = flp_2017.dropna(axis=0)

flp_2018[(flp_2018.ta<13) | (flp_2018.ta > 14.2)] = NaN
flp_2018= flp_2018.dropna(axis=0)

flp_2019[(flp_2019.ta > 14.2)| (flp_2019.ta < 13)] = NaN
flp_2019[(flp_2019.tc > 14.2)| (flp_2019.tc < 13)] = NaN
flp_2019 = flp_2019.dropna(axis = 0)

flp_2017_2019 = pd.concat([flp_2017, flp_2018, flp_2019]).copy()
flp_2017_2019 = flp_2017_2019.set_index('horario')
flp_2017_2019_med = flp_2017_2019.resample("d").mean().copy()
flp_2017_2019_med = flp_2017_2019_med.fillna(method="ffill")

clima_2017 = pd.read_csv(r"Dados\Dados ClimáticosFlorianópolis-2017.csv", parse_dates=['Data'], index_col=['Data'])
clima_2018 = pd.read_csv(r"Dados\Dados ClimáticosFlorianópolis2018.csv", parse_dates=['Data'], index_col=['Data'])
clima_2019 = pd.read_csv(r"Dados\Dados ClimáticosFlorianópolis2019.csv", parse_dates=['Data'], index_col=['Data'])

clima_2017_2019 = pd.concat([clima_2017, clima_2018, clima_2019]).copy()
clima_2017_2019_med = clima_2017_2019.resample("d").mean().copy()

df = pd.concat([flp_2017_2019_med, clima_2017_2019_med]).copy()


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

fig = make_subplots(rows=3, cols=1,shared_xaxes=True,vertical_spacing=0.002)
fig.add_trace(go.Scatter(x=df.index, y=df.TempIns, name="Temperatura"),row=3, col=1)
fig.add_trace(go.Scatter(x=df.index, y=df.Chuva, name="Chuva"),row=2, col=1)
fig.add_trace(go.Scatter(x=df.index, y=df.p3, name="Potencia Trifásica"),row=1, col=1)
fig.update_layout(title_text="Relação Potencia Trifásica, Chuva e Temperatura",plot_bgcolor=colors['bg'],paper_bgcolor=colors['bg'],font_color=colors['text'])


dfb = df.resample("b").mean().copy()
figb = make_subplots(rows=3, cols=1,shared_xaxes=True,vertical_spacing=0.002)
figb.add_trace(go.Scatter(x=dfb.index, y=dfb.TempIns, name="Temperatura"),row=3, col=1)
figb.add_trace(go.Scatter(x=dfb.index, y=dfb.Chuva, name="Chuva"),row=2, col=1)
figb.add_trace(go.Scatter(x=dfb.index, y=dfb.p3, name="Potencia Trifásica"),row=1, col=1)
figb.update_layout(title_text="Relação Potencia Trifásica, Chuva e Temperatura - Dias úteis",plot_bgcolor=colors['bg'],paper_bgcolor=colors['bg'],font_color=colors['text'])

df['p3Mean'] = df.p3.rolling(7).mean()
df['TempInsMean'] = df.TempIns.rolling(7).mean()
df['ChuvaMean'] = df.Chuva.rolling(7).mean()
fig7 = make_subplots(rows=3, cols=1,shared_xaxes=True,vertical_spacing=0.002)
fig7.add_trace(go.Scatter(x=df.index, y=df.TempInsMean, name="Temperatura"),row=3, col=1)
fig7.add_trace(go.Scatter(x=df.index, y=df.ChuvaMean, name="Chuva"),row=2, col=1)
fig7.add_trace(go.Scatter(x=df.index, y=df.p3Mean, name="Potencia Trifásica"),row=1, col=1)
fig7.update_layout(title_text="Relação Potencia Trifásica, Chuva e Temperatura - Media Móvel Semanal",plot_bgcolor=colors['bg'],paper_bgcolor=colors['bg'],font_color=colors['text'])

df['p3Mean30'] = df.p3.rolling(30).mean()
df['TempInsMean30'] = df.TempIns.rolling(30).mean()
df['ChuvaMean30'] = df.Chuva.rolling(30).mean()
fig30 = make_subplots(rows=3, cols=1,shared_xaxes=True,vertical_spacing=0.002)
fig30.add_trace(go.Scatter(x=df.index, y=df.TempInsMean30, name="Temperatura"),row=3, col=1)
fig30.add_trace(go.Scatter(x=df.index, y=df.ChuvaMean30, name="Chuva"),row=2, col=1)
fig30.add_trace(go.Scatter(x=df.index, y=df.p3Mean30, name="Potencia Trifásica"),row=1, col=1)
fig30.update_layout(title_text="Relação Potencia Trifásica, Chuva e Temperatura - Media Móvel Mensal",plot_bgcolor=colors['bg'],paper_bgcolor=colors['bg'],font_color=colors['text'])

df['p3Mean182'] = df.p3.rolling(182).mean()
df['TempInsMean182'] = df.TempIns.rolling(182).mean()
df['ChuvaMean182'] = df.Chuva.rolling(182).mean()
fig182 = make_subplots(rows=3, cols=1,shared_xaxes=True,vertical_spacing=0.002)
fig182.add_trace(go.Scatter(x=df.index, y=df.TempInsMean182, name="Temperatura"),row=3, col=1)
fig182.add_trace(go.Scatter(x=df.index, y=df.ChuvaMean182, name="Chuva"),row=2, col=1)
fig182.add_trace(go.Scatter(x=df.index, y=df.p3Mean182, name="Potencia Trifásica"),row=1, col=1)
fig182.update_layout(title_text="Relação Potencia Trifásica, Chuva e Temperatura - Media Movel Semestral",plot_bgcolor=colors['bg'],paper_bgcolor=colors['bg'],font_color=colors['text'])

df['p3Mean365'] = df.p3.rolling(365).mean()
df['TempInsMean365'] = df.TempIns.rolling(365).mean()
df['ChuvaMean365'] = df.Chuva.rolling(365).mean()
fig365 = make_subplots(rows=3, cols=1,shared_xaxes=True,vertical_spacing=0.002)
fig365.add_trace(go.Scatter(x=df.index, y=df.TempInsMean365, name="Temperatura"),row=3, col=1)
fig365.add_trace(go.Scatter(x=df.index, y=df.ChuvaMean365, name="Chuva"),row=2, col=1)
fig365.add_trace(go.Scatter(x=df.index, y=df.p3Mean365, name="Potencia Trifásica"),row=1, col=1)
fig365.update_layout(title_text="Relação Potencia Trifásica, Chuva e Temperatura - Média Movel Anual",plot_bgcolor=colors['bg'],paper_bgcolor=colors['bg'],font_color=colors['text'])

df = df.fillna(method="ffill")

p3_col = df['p3'].tolist()
date_col = df.index.tolist()

figs = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 149.879553,
    mode = "gauge+number+delta",
    title = {'text': "Consumo Médio"},
    delta = {'reference': 89.429454},
    gauge = {'axis': {'range': [11.847000, 569.564387]},
             'steps' : [
                 {'range': [11.847000, 210.260432], 'color': "lightgray"},
                 {'range': [210.260432, 569.564387], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 569.564387}}))
figs.update_layout(plot_bgcolor=colors['bg'],paper_bgcolor=colors['bg'],font_color=colors['text'])

figs2 = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 21.610357,
    mode = "gauge+number+delta",
    title = {'text': "Temperatura Média"},
    delta = {'reference': 24.120833},
    gauge = {'axis': {'range': [10.027273, 30.891667]},
             'steps' : [
                 {'range': [10.027273, 21.875000], 'color': "lightgray"},
                 {'range': [21.875000, 30.891667], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 30.891667}}))
figs2.update_layout(plot_bgcolor=colors['bg'],paper_bgcolor=colors['bg'],font_color=colors['text'])

app.layout = html.Div([
    html.H3(['Dashboard de relação da potência trifásica com a temperatura e a chuva'], style={'background-color':'#050018', 
                                                                                                'color':'#ffcc5c', 
                                                                                                'align-objects':'center', 
                                                                                                'display': 'flex', 
                                                                                                'flex-direction':'row', 
                                                                                                'align-objects':'center', 
                                                                                                'justify-content':'center', 
                                                                                                'width': '400', 
                                                                                                'font-size':'16', 
                                                                                                'text-align':'center', 
                                                                                                'margin':'-8px',
                                                                                                'padding': '14px',
                                                                                                'border-style': 'solid',
                                                                                                'border-color': '#111111'}),
        html.Div([
            dcc.Graph(figure=fig, style={'padding':'5px', 'width':'50%', 'height':'30%', 'margin':'-8px'}),
            dcc.Graph(figure=figb, style={'padding':'5px', 'width':'50%', 'height':'30%', 'margin':'-8px'}),
        ], style={
            'display':'flex',
            'flex-direction':'row',
            'justify-content':'center',
            'align-content':'center',
            'background':'#050018',
            'margin':'-8px',
            'padding':'14px'
        }),
        html.Div([
            dcc.Graph(figure=fig7, style={'padding':'5px', 'width':'50%', 'height':'30%', 'margin':'-8px'}),
            dcc.Graph(figure=fig365, style={'padding':'5px', 'width':'50%', 'height':'30%', 'margin':'-8px'})
        ], style={
            'display':'flex',
            'flex-direction':'row',
            'justify-content':'center',
            'align-content':'center',
            'background':'#050018',
            'margin':'-8px',
            'padding':'14px'
            }),
        html.Div([
            dcc.Graph(figure=figs, style={'padding':'5px', 'width':'50%', 'height':'30%', 'margin':'-8px'}),
            dcc.Graph(figure=figs2, style={'padding':'5px', 'width':'50%', 'height':'30%', 'margin':'-8px'})
        ], style={
            'display':'flex',
            'flex-direction':'row',
            'justify-content':'center',
            'align-content':'center',
            'background':'#050018',
            'margin':'-8px',
            'padding':'14px'
            }),
], style={'margin':'0px', 'background-color':'#050018'})

if __name__ == '__main__':
    app.run_server(debug=True)