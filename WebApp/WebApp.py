# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 21:59:07 2021

@author: saideep
"""
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from sklearn.compose import ColumnTransformer
import json
import tempfile
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

import re 
from datetime import datetime, timedelta
import pickle
import numpy as np
import string
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from typing import Callable
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler, OneHotEncoder, FunctionTransformer

import pickle
covid_model = pickle.load(open('covid_new_model.sav', 'rb'))
flu_model = pickle.load(open('flu_new_model.sav', 'rb'))
hep_model = pickle.load(open('hp_new_model.sav', 'rb'))
var_model = pickle.load(open('var_new_model.sav', 'rb'))
serious_pred_d=0
non_serious_pred_d=0
# start the App
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, 
    external_stylesheets=external_stylesheets,
    # to verify your own website with Google Search Console
    meta_tags=[{'name': 'google-site-verification', 'content': 'Wu9uTwrweStHxNoL-YC1uBmrsXYFNjRCqmSQ8nNnNMs'}])
app.title = 'Adverse events with Vacinations'


server = app.server
######################
# Getting vaccinations and manufactoror details for drop down colums  
vac_dict={'Varzos':['MERCK & CO. INC.','GLAXOSMITHKLINE BIOLOGICALS'],'Hepatitis':['GLAXOSMITHKLINE BIOLOGICALS','MERCK & CO. INC.','SMITHKLINI BEECHAM','DYNAVAX TECHNOLOGIES CORPORATION'],'Flu':['PARKE-DAVIS','CONNAUGHT LABORATORIES','LEDERLE LABORATORIES','PFIZER\WYETH','MEDEVA PHARMA, LTD.','PARKDALE PHARMACEUTICALS','SANOFI PASTEUR','MEDIMMUNE VACCINES, INC.','EVANS VACCINES','GLAXOSMITHKLINE BIOLOGICALS','NOVARTIS VACCINES AND DIAGNOSTICS','CSL LIMITED','PROTEIN SCIENCES CORPORATION','SEQIRUS, INC.','AVENTIS PASTEUR' ],'Covid':['MODERNA','PFIZER\BIOTECH','JANSEEN']}
vaccinations=[]
manufactotor=[]
for i,j in vac_dict.items():
    vaccinations.append(i)
    manufactotor+=j


###############################


prediction_col1 =  dbc.Col([ 
                html.Br(),
                dbc.Row([html.H3(children='Predict Adverse Reactions')]),
                dbc.Row([
                    dbc.Col(html.Label(children='Age:'), width={"order": "first"}, style = {'padding': '15px 0px 0px 0px',"font-weight": "bold"}),
                    dcc.Slider(0, 100, 1,value=10,id='AGE',marks=None,tooltip={"placement": "bottom", "always_visible": True})
                ]), 
                dbc.Row([
                    dbc.Col(html.Label(children='Vaccination Type:'), width={"order": "first"}, style = {'padding': '5px 0px 5px 0px',"font-weight": "bold"}),
#                     dbc.RadioItems(
#                         id='Vaccination_type',
#                         options=[
#                             {'label': 'Covid 19', 'value': 'Covid'},
#                             {'label': 'FLU Influenza', 'value': 'Flu'},
#                             {'label': 'Hepatities', 'value': 'Hepatitis'},
#                             {'label': 'Varzos', 'value': 'Varzos'}
#                             ],
#                         style = {"width": "60%", 'padding': '5px 0px 10px 10px', 'display': 'inline-block' },
#                         labelStyle={'display': 'inline-block'},
#                         inline=True # arrange list horizontally
                    dcc.Dropdown(
                        id='Vaccination_type',
                        multi=False,
                        clearable=True,
                        disabled=False,
                        style = {"width": "50%", 'padding': '5px 0px 5px 10px', 'display': 'inline-block'}
                    )
                    
                ]),
                 dbc.Row([
                    dbc.Col(html.Label(children='Vaccine Manufacturer:'), width={"order": "first"}, style = {'padding': '15px 0px 0px 0px',"font-weight": "bold"}),
                    dcc.Dropdown(
                        id='manufactorer',
                        multi=False,
                        clearable=True,
                        disabled=False,
                        style = {"width": "50%", 'padding': '5px 0px 5px 10px', 'display': 'inline-block'}
                    )
                
                ]),
                dbc.Row([
                    dbc.Col(html.Label(children='Sex:'), width={"order": "first"}, style = {'padding': '5px 0px 5px 0px',"font-weight": "bold"}),
                    dbc.RadioItems(
                        id='sex',
                        options=[
                            {'label': 'Male', 'value': '1'},
                            {'label': 'Female', 'value': '0'}
                            ],
                        style = {"width": "50%", 'padding': '5px 0px 5px 10px', 'display': 'inline-block' },
                        value = 'Male',
                        labelStyle={'display': 'inline-block'},
                        inline=True # arrange list horizontally
                    )
                ]), 
                dbc.Row([
                    dbc.Col(html.Label(children='Symptom:'), width={"order": "first"}, style = {'padding': '15px 0px 0px 0px',"font-weight": "bold"}),
                    dbc.Col(dbc.Input(id='Symptom', type='text',value= 'None', placeholder='Type your symptom', style = {'padding': '5px 0px 5px 10px', 'width': '200px'}))
                ]), 
                dbc.Row([
                    dbc.Col(html.Label(children='Patient Died?'), width={"order": "first"}, style = {'padding': '5px 0px 5px 0px',"font-weight": "bold"}),
                    dbc.RadioItems(
                        id='DIED',
                        options=[
                            {'label': 'Yes', 'value': '1'},
                            {'label': 'No', 'value': '0'}
                            ],
                        style = {"width": "50%", 'padding': '5px 0px 10px 10px', 'display': 'inline-block' },
                        value = 'No',
                        labelStyle={'display': 'inline-block'},
                        inline=True # arrange list horizontally
                    )
                ]), 
                dbc.Row([
                    dbc.Col(html.Label(children='Is Symptom Life Threatening?:'), width={"order": "first"}, style = {'padding': '5px 0px 5px 0px',"font-weight": "bold"}),
                    dbc.RadioItems(
                        id='Life_THREAT',
                        options=[
                            {'label': 'Yes', 'value': '1'},
                            {'label': 'No', 'value': '0'}
                            ],
                        style = {"width": "50%", 'padding': '5px 0px 10px 10px', 'display': 'inline-block' },
                        value = 'No',
                        labelStyle={'display': 'inline-block'},
                        inline=True # arrange list horizontally
                    )
                ]), 
                dbc.Row([
                    dbc.Col(html.Label(children='Is Patient Hospitlized?:'), width={"order": "first"}, style = {'padding': '5px 0px 5px 0px',"font-weight": "bold"}),
                    dbc.RadioItems(
                        id='HOSPITALISED',
                        options=[
                            {'label': 'Yes', 'value': '1'},
                            {'label': 'No', 'value': '0'}
                            ],
                        style = {"width": "50%", 'padding': '5px 0px 10px 10px', 'display': 'inline-block' },
                        value = 'No',
                        labelStyle={'display': 'inline-block'},
                        inline=True # arrange list horizontally
                    )
                ]),  
                dbc.Row([
                    dbc.Col(html.Label(children='How many days patient hospitalized?:'), width={"order": "first"}, style = {'padding': '15px 0px 0px 0px',"font-weight": "bold"}),
                    dbc.Col(dbc.Input(id='HOSPDAYS', type='number',value= '0', style = {'padding': '5px 0px 5px 10px', 'width': '200px'}))
                ]),
                
                dbc.Row([
                    dbc.Col(html.Label(children='Is Patient having any Disabilities?:'), width={"order": "first"}, style = {'padding': '5px 0px 5px 0px',"font-weight": "bold"}),
                    dbc.RadioItems(
                        id='ANY_DISABLITIES',
                        options=[
                            {'label': 'Yes', 'value': '1'},
                            {'label': 'No', 'value': '0'}
                            ],
                        style = {"width": "50%", 'padding': '5px 0px 10px 10px', 'display': 'inline-block' },
                        value = 'No',
                        labelStyle={'display': 'inline-block'},
                        inline=True # arrange list horizontally
                    )
                ]), 
                dbc.Row([
                    dbc.Col(html.Label(children='Is Patient Recovered from Symptoms?:'), width={"order": "first"}, style = {'padding': '5px 0px 5px 0px',"font-weight": "bold"}),
                    dbc.RadioItems(
                        id='RECOVD',
                        options=[
                            {'label': 'Yes', 'value': '1'},
                            {'label': 'No', 'value': '0'}
                            ],
                        style = {"width": "50%", 'padding': '5px 0px 10px 10px', 'display': 'inline-block' },
                        value = 'No',
                        labelStyle={'display': 'inline-block'},
                        inline=True # arrange list horizontally
                    )
                ]), 
                dbc.Row([
                    dbc.Col(html.Label(children='Any Other Medications?:'), width={"order": "first"}, style = {'padding': '15px 0px 0px 0px',"font-weight": "bold"}),
                    dbc.Col(dbc.Input(id='OTHER_MEDS', type='text',value= 'None', placeholder = 'Type the medications taked symptoms', style = {'padding': '5px 0px 5px 10px', 'width': '200px'}))
                ]),
                dbc.Row([
                    dbc.Col(html.Label(children='Is Patient having any Current Illiness?:'), width={"order": "first"}, style = {'padding': '15px 0px 0px 0px',"font-weight": "bold"}),
                    dbc.Col(dbc.Input(id='CUR_ILL', type='text',value= 'None', placeholder = 'Type your symptoms', style = {'padding': '5px 0px 5px 10px', 'width': '200px'}))
                ]),
                dbc.Row([
                    dbc.Col(html.Label(children='Is Patient having any Medical History?:'), width={"order": "first"}, style = {'padding': '15px 0px 0px 0px',"font-weight": "bold"}),
                    dbc.Col(dbc.Input(id='HISTORY', type='text',value= 'None', placeholder = 'Any history of ', style = {'padding': '5px 0px 5px 10px', 'width': '200px'}))
                ]),
                dbc.Row([
                    dbc.Col(html.Label(children='Is Patient having any Allergies?:'), width={"order": "first"}, style = {'padding': '15px 0px 0px 0px',"font-weight": "bold"}),
                    dbc.Col(dbc.Input(id='ALLERGIES', type='text',value= 'None', placeholder = 'Type your symptoms', style = {'padding': '5px 0px 5px 10px', 'width': '200px'}))
                ]),
                dbc.Row([
                    dbc.Col(html.Label(children='Is Patient having any Birth Defect:'), width={"order": "first"}, style = {'padding': '5px 0px 5px 0px',"font-weight": "bold"}),
                    dbc.RadioItems(
                        id='BIRTH_DEFECT',
                        options=[
                            {'label': 'Yes', 'value': '1'},
                            {'label': 'No', 'value': '0'}
                            ],
                        style = {"width": "50%", 'padding': '5px 0px 10px 10px', 'display': 'inline-block' },
                        value = 'No',
                        labelStyle={'display': 'inline-block'},
                        inline=True # arrange list horizontally
                    )
                ]),                    
                html.Br(),
                dbc.Row([dbc.Button('Submit', id='submit-val', n_clicks=0, color="primary")]),
                html.Br(),
                dbc.Row([html.Div(id='container-button-basic')])
            ], style = {'padding': '0px 0px 0px 150px'})

prediction_col2 =  dbc.Col([ html.Br(), html.Div(dcc.Graph(id='hist-graph'))], style = {'padding': '0px 0px 0px 0px'})


# sales_col_map = dbc.Col([
#         html.Br(),
#         dbc.RadioItems(
#             id = 'recent_sales_city',
#             options=[{"label": x, "value": x} for x in [0,1]],
#             value='abc',
#             labelStyle={'display': 'inline-block'},
#             labelCheckedStyle={"color": "red"},
#             inline=True, # arrange list horizontally
#             style={"justify-content":"space-between", "font-size":"24px", "margin-left": "0px"}
#         ),
#         html.Br(),
#         html.Div(dcc.Graph(id='sales_map'))
#     ], style = {'padding': '0px 0px 0px 60px'})

# sales_col_table = dbc.Col([ 
#         html.Br(),
#         #html.Div(dash_table.DataTable(id='sales_table', columns=[{"name": i, "id": i} for i in sales.columns], data = sales.to_dict('records') )
#         html.Div(children='Home Sales Within Last 7 Days'),
#         html.Br(), 
#         html.Div(id='sales_table')

#     ], style = {'padding': '0px 0px 0px 20px'})

   

##############################################################
# prepare the layout
app.layout = html.Div([
    html.H1(children='Predict Adverse Drug Reactions by vaccinations'),
    html.Div(children='''vaccinations are Covid,FLU Influenza,Hepatities,Varzos '''),
    html.Br(),
    
    dcc.Tabs(style = {'width': '100%',"font-weight": "bold"}, children=[
        # this is the first tab
        
        # this is the 3rd tab
        dcc.Tab(label='Seriousness Prediction', children = [
            dbc.Row([prediction_col1, prediction_col2])
            
        ]), # the end of the 3rd tab

        # this is the 4th tab
#         dcc.Tab(label='vaccine Manufactorer Prediction', children = [
#             dbc.Row([sales_col_map]),
#             dbc.Row([sales_col_table])
#         ]) # the end of the 4th tab




    ], colors={
        "border": "white",
        "primary": "gold",
        "background": "cornsilk"}) # end of all tabs

], style = {
'background-image': 'url("/assets/image 3.jpg")',
'background-repeat': 'no-repeat',
'background-size': 'cover'
}) # the end of app.layout


####################################################################################################################
# creating the call back for manufactotar drop down
@app.callback(
    Output("manufactorer", "options"),
    Input("manufactorer", "search_value"), Input("Vaccination_type", "value")
)
def batch_options(search_value, Vaccination_type):
    if Vaccination_type is None:
        return [{"label": i, "value": i} for i in manufactotor]
    else:
        return [{"label": i, "value": i} for i in vac_dict[Vaccination_type]]
    
    
@app.callback(
    Output("Vaccination_type", "options"), Input("Vaccination_type", "search_value")
)
def material_options(search_value):
    return [{"label": i, "value": i} for i in vaccinations]
    print(vaccinations,vac_dict[Vaccination_type])

# create call back fror prediction
@app.callback(
    Output('container-button-basic', 'children'),
    Output('hist-graph', 'figure'),
    # Inputs will trigger your callback; State do not. If you need the the current “value” - aka State - of other dash components within your callback, you pass them along via State.
    Input('submit-val', 'n_clicks'),
    State('AGE', 'value'),
    State('Vaccination_type', 'value'),
    State('manufactorer', 'value'), 
    State('sex', 'value'),
    State('Symptom', 'value'),
    State('DIED', 'value'),
    State('Life_THREAT', 'value'),
    State('HOSPITALISED', 'value'),
    State('HOSPDAYS', 'value'),
    State('ANY_DISABLITIES', 'value'),
    State('RECOVD', 'value'),
    State('OTHER_MEDS', 'value'),
    State('CUR_ILL', 'value'),
    State('HISTORY', 'value'),
    State('ALLERGIES', 'value'),
    State('BIRTH_DEFECT', 'value')) 

def update_output(n_clicks, AGE, Vaccination_type, manufactorer, sex, Symptom, DIED,Life_THREAT, HOSPITALISED, HOSPDAYS,ANY_DISABLITIES,RECOVD,OTHER_MEDS,CUR_ILL,HISTORY,ALLERGIES,BIRTH_DEFECT):
    
    if Vaccination_type == 'Covid':
        df = pd.DataFrame.from_dict({
        "AGE_YRS":[AGE],
        "SEX":[sex],
        "SYMPTOM_TEXT":[Symptom],
        'DIED':[DIED],
        'L_THREAT':[Life_THREAT],
        'HOSPITAL':[HOSPITALISED],
        'HOSPDAYS': [HOSPDAYS],
        'DISABLE':[ANY_DISABLITIES],
        'RECOVD': [RECOVD],
        'OTHER_MEDS': [OTHER_MEDS],
        'CUR_ILL':[CUR_ILL],
        'HISTORY':[HISTORY],
        'BIRTH_DEFECT':[BIRTH_DEFECT],
        'ALLERGIES': [ALLERGIES],
        'JANSSEN':[1 if manufactorer=='JANSSEN' else 0],
        'MODERNA': [1 if manufactorer=='MODERNA' else 0],
        'PFIZER\BIONTECH':[1 if manufactorer=='PFIZER\BIOTECH' else 0]

        })
        prediction = covid_model.predict_proba(df)
        pred = prediction[0][0]
        non_serious_pred = str(round(pred,2))
        non_serious_pred_d = round(round(pred,2)*100)
        serious_pred_d = 100 - non_serious_pred_d
        serious_pred = str(round(1-pred,2)) 
    elif Vaccination_type == 'Flu':
        df = pd.DataFrame.from_dict({
        "AGE_YRS":[AGE],
        "SEX":[sex],
        "SYMPTOM_TEXT":[Symptom],
        'DIED':[DIED],
        'L_THREAT':[Life_THREAT],
        'HOSPITAL':[HOSPITALISED],
        'HOSPDAYS': [HOSPDAYS],
        'DISABLE':[ANY_DISABLITIES],
        'RECOVD': [RECOVD],
        'OTHER_MEDS': [OTHER_MEDS],
        'CUR_ILL':[CUR_ILL],
        'HISTORY':[HISTORY],
        'BIRTH_DEFECT':[BIRTH_DEFECT],
        'ALLERGIES': [ALLERGIES],
        'AVENTIS': [1 if manufactorer=='AVENTIS PASTEUR' else 0],
        'CONNAUGHT':[1 if manufactorer=='CONNAUGHT LABORATORIES' else 0],
        'CSL':[1 if manufactorer=='CSL LIMITED' else 0],
        'EVANS': [1 if manufactorer=='EVANS VACCINES' else 0],
        'GLAXOSMITHKLINE':[1 if manufactorer=='GLAXOSMITHKLINE BIOLOGICALS' else 0],
        'LEDERLE': [1 if manufactorer=='LEDERLE LABORATORIES' else 0],
        'MEDEVA': [1 if manufactorer=='MEDEVA PHARMA, LTD.' else 0],
        'MEDIMMUNE':[1 if manufactorer=='MEDIMMUNE VACCINES, INC.' else 0],
        'NOVARTIS':[1 if manufactorer=='NOVARTIS VACCINES AND DIAGNOSTICS' else 0],
        'PARKDALE': [1 if manufactorer=='PARKDALE PHARMACEUTICALS' else 0],
        'PARKE':[1 if manufactorer=='PARKE-DAVIS' else 0],
        'PFIZER': [1 if manufactorer=='PFIZER\WYETH' else 0],
        'PROTEIN': [1 if manufactorer=='PROTEIN SCIENCES CORPORATION' else 0],
        'SANOFI':[1 if manufactorer=='SANOFI PASTEUR' else 0],
        'SEQIRUS': [1 if manufactorer=='SEQIRUS, INC.' else 0]
        })
        prediction = flu_model.predict_proba(df)
        pred = prediction[0][0]
        non_serious_pred = str(round(pred,2))
        non_serious_pred_d = round(round(pred,2)*100)
        serious_pred_d = 100 - non_serious_pred_d
        serious_pred = str(round(1-pred,2))    
    elif Vaccination_type == 'Hepatitis':
        df = pd.DataFrame.from_dict({
        "AGE_YRS":[AGE],
        "SEX":[sex],
        "SYMPTOM_TEXT":[Symptom],
        'DIED':[DIED],
        'L_THREAT':[Life_THREAT],
        'HOSPITAL':[HOSPITALISED],
        'HOSPDAYS': [HOSPDAYS],
        'DISABLE':[ANY_DISABLITIES],
        'RECOVD': [RECOVD],
        'OTHER_MEDS': [OTHER_MEDS],
        'CUR_ILL':[CUR_ILL],
        'HISTORY':[HISTORY],
        'BIRTH_DEFECT':[BIRTH_DEFECT],
        'ALLERGIES': [ALLERGIES],
        'DYNAVAX': [1 if manufactorer=='DYNAVAX TECHNOLOGIES CORPORATION' else 0],
        'GLAXOSMITHKLINE':[1 if manufactorer=='GLAXOSMITHKLINE BIOLOGICALS' else 0],
        'MERCK':[1 if manufactorer=='MERCK & CO. INC.' else 0],
        'SANOFI': [1 if manufactorer=='SANOFI PASTEUR' else 0],
        'SMITHKLINE': [1 if manufactorer=='SMITHKLINE BEECHAM' else 0]})
        prediction = hep_model.predict_proba(df)
        pred = prediction[0][0]
        non_serious_pred = str(round(pred,2))
        non_serious_pred_d = round(round(pred,2)*100)
        serious_pred_d = 100 - non_serious_pred_d
        serious_pred = str(round(1-pred,2))    
    elif Vaccination_type == 'Varzos':
        df = pd.DataFrame.from_dict({
        "AGE_YRS":[AGE],
        "SEX":[sex],
        "SYMPTOM_TEXT":[Symptom],
        'DIED':[DIED],
        'L_THREAT':[Life_THREAT],
        'HOSPITAL':[HOSPITALISED],
        'HOSPDAYS': [HOSPDAYS],
        'DISABLE':[ANY_DISABLITIES],
        'RECOVD': [RECOVD],
        'OTHER_MEDS': [OTHER_MEDS],
        'CUR_ILL':[CUR_ILL],
        'HISTORY':[HISTORY],
        'BIRTH_DEFECT':[BIRTH_DEFECT],
        'ALLERGIES': [ALLERGIES],
        'GLAXOSMITHKLINE': [1 if manufactorer=='GLAXOSMITHKLINE BIOLOGICALS' else 0],
        'MERCK':[1 if manufactorer=='MERCK & CO. INC.' else 0]})
        prediction = var_model.predict_proba(df)
        pred = prediction[0][0]
        non_serious_pred = str(round(pred,2))
        non_serious_pred_d = round(round(pred,2)*100)
        serious_pred_d = 100 - non_serious_pred_d
        serious_pred = str(round(1-pred,2))    

        fig = go.Figure(go.Bar(
            x=[non_serious_pred_d,serious_pred_d],
            y=['Non Serious', 'Serious'],
            orientation='h'))

        fig.update_xaxes(
            scaleanchor = "x",
            scaleratio = 1,
            range=(1, 100),
            )

    

#     fig = px.histogram(his_df, x = 'Price', histnorm ='percent', nbins = 20, width = 00, height  = 600)
#     fig.add_vline(x=p_25, line_width=3, line_dash="dash", line_color="green", annotation_text=f"25th Percentile: ${p_25:,}", annotation_position="top left")
#     fig.add_vline(x=p_75, line_width=3, line_dash="dash", line_color="green", annotation_text=f"75th Percentile: ${p_75:,}", annotation_position="top right")
#     fig.add_vline(x=p_50, line_width=3, line_dash="dash", line_color="green", annotation_text=f"50th Percentile (Median Price): ${p_50:,}", annotation_position="top")
#     fig.add_vrect(x0=p_25, x1=p_75, line_width=0, fillcolor="red", opacity=0.2)


    return f'Patient is  {serious_pred_d}% serious and {non_serious_pred_d}% non serious for this vaccination {Vaccination_type}',fig
##############################
# # create call back for recently sales
# @app.callback(
#     Output('sales_table', 'children'),
#     Output('sales_map', 'figure'),
#     Input('recent_sales_city', 'value')
# )
# def update_recent_sales_table (city):
#     selected_df = sales[sales.city==city]
#     selected_df = selected_df[['url', 'pred_price_diff', 'property_type', 'sold_date', 'address', 'price', 'dollar_per_sq_feet', 'hoa', 'beds', 'baths', 'sq_feet', 'lot_size', 'year_built', 'days_on_market', 'lat', 'long']]
#     selected_df = selected_df.to_dict('records')
#     for i in selected_df:
#         i['url'] = [html.A(html.P('Redfin Link'), href=i['url'], target="_blank")]
#     selected_df = pd.DataFrame(selected_df)
#     selected_df = selected_df.sort_values(['dollar_per_sq_feet'], ascending = [True])
#     selected_df['price'] = selected_df.apply(lambda x:  f'${x["price"]:,}', axis =1)
#     selected_df['dollar_per_sq_feet'] = selected_df.apply(lambda x:  f'${int(x["dollar_per_sq_feet"])}', axis =1)
#     selected_df.columns = ['URL', 'Delta %', 'Property Type', 'Sold Date', 'Address', 'Price', '$ PSF', 'HOA','Beds', 'Baths', 'SQ Feet', 'Lot Size', 'Year Built', 'DOM', 'Lat', 'Long']
#     sale_table = dbc.Table.from_dataframe(selected_df.drop(columns = ['Lat', 'Long']), striped=True, bordered=True, hover=True, size = 'sm')
     
#     #################
#     fig = px.scatter_mapbox(data_frame=selected_df, lat='Lat', lon='Long', 
#             #opacity=0.5, 
#             hover_name="Address", 
#             hover_data=["Price"],
#             zoom=10, width=600, height=400
#         )
#     fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},  # remove the white gutter between the frame and map
#             # hover appearance
#             hoverlabel=dict( 
#                 bgcolor="white",     # white background
#                 font_size=16,        # label font size
#                 font_family="Inter") # label font
#         )



#     return sale_table, fig

#############################
print('****************************************************')
print('Current time: Run App : ' + str(datetime.now()))
# run the app 
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
    