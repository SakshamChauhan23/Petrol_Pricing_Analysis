"""Importing Important Libraries"""
from __future__ import annotations
from optparse import Values
from string import hexdigits
from tkinter.font import names
from turtle import width
from matplotlib.pyplot import legend, margins, title
import numpy as np
import pandas as pd
import plotly.express as px

"""Loading the Dataset"""
df = pd.read_csv(r'C:\Users\SAKSHAM\Desktop\Coding\Sample DA Practise\Analysis of Petrol Price World Wide\Petrol Dataset June 20 2022.csv',encoding='Latin-1')


"""Data Preparation and Cleaning"""
df.head()
df.columns
df.isnull().sum()
"""As per the results we found total sum is zero thus there are no Null Values"""


"""Data Exploration"""

#PERCENTAGE OF DAILY OIL CONSUMPTIONS (BARRELS) BY TOP 10% COUNTRIES
highest_consumption = df.nlargest(10, 'Daily Oil Consumption (Barrels)')
highest_consumption.head()

#Pie Chart Representation of DAILY OIL CONSUMPTIONS BY TOP 10% Countries
fig = px.pie(highest_consumption.head(10),values='Daily Oil Consumption (Barrels)',names='Country',hole=0.425)
fig.update_layout(title='Daily Oil Consumption by Top 10 Countries',font_size=15,title_x=0.45,annotations=[dict(text=  'OC(Barrels)',font_size=18,showarrow=False,height=880,width=700)])
fig.update_traces(textfont_size=15,textinfo='percent')
fig.show()

"""With the given pie chart we can conclude that world half of the petroleum is being consumed by United States and China
On the other hand India being the third largets consumer with 7.62% of World's Petrol """


#Top 10 Countries that contribute to the World's Share
highest_consumption['World Share'].unique()

#Pie Chart Representation of World Share BY TOP 10% Countries
fig=px.pie(highest_consumption.head(10),values='World Share',names='Country',hole=0.46)
fig.update_layout(title='World Share BY TOP 10% Countries',font_size=15,title_x=0.45,annotations=[dict(text='World Share',font_size=18, showarrow=False,height=800,width=700)])
fig.update_traces(textfont_size=15,textinfo='percent')
#fig.show()


#Yearly Gallon per Capita of Top 10 Countries
"""Copy the dataset at first so that original dataset won't get affected"""
df0=df

df0_yearlygallon1=df0.sort_values(by=["Yearly Gallons Per Capita","Price Per Gallon (USD)"],ascending=False)
fig = px.bar(df0_yearlygallon1.head(10),x='Country',y='Yearly Gallons Per Capita',text_auto=True)
fig.update_layout(legend_orientation='h',legend=dict(x=0,y=1,traceorder='normal'),title="Yearly Gallon per Capita of Top 10 Countries",margin=dict(l=0,r=0,t=30,b=0))
fig.show()


#Sort Price Per Liter (USD Column)
df0_priceperliter = df0.sort_values(by="Price Per Liter (USD)",ascending=False)
print(df0_priceperliter)


#Price Per Liter (USD) of petrol- Top 10 Countries
fig = px.bar(df0_priceperliter.head(10),x='Country',y='Price Per Liter (USD)',text_auto=True)
fig.update_layout(legend_orientation='h',xaxis_tickangle=-45,title_x=0.45, legend=dict(x=0,y=1,traceorder='normal'),title='Price Per Liter (USD) of petrol',margin=dict(l=0,r=0,t=30,b=0))
fig.show()

"""As per the graph North Korea has marginally almost triple the Price Per Litre compared to second
No wonder Why there's less number of Drivers in North Korea"""

"""Now we are going to Perform all the above analysis again to specific countries
1. India 2. Iraq 3. Pakistan 4. Bangladesh 5. Afghanistan """

ind = df0[df0['Country']=='India']
pak = df0[df0['Country']=='Pakistan']
iraq = df0[df0['Country']=='Iraq']
ban = df0[df0['Country']=='Bangladesh']
afg = df0[df0['Country']=='Afganistan']

asia = pd.concat([ind,pak,iraq,ban,afg])
print(asia)

#VISUALIZATION OF DAILY OIL CONSUMPTION (BARRELS) (Bar Graph)

fig = px.bar(asia.head(10),x='Country',y='Daily Oil Consumption (Barrels)',text_auto=True)
fig.update_layout(legend_orientation='h',xaxis_tickangle=-45,title_x=0.45,legend=dict(x=0,y=1,traceorder='normal'),title = 'Daily Oil Consumption (Barrels)',margin=dict(l=0,r=0,t=30,b=0))
fig.show()
"""Daily Oil Consumption is largest in India 4.43 M and least in Afganistan 35K"""

#VISUALIZATION OF DAILY OIL CONSUMPTION (BARRELS) (Pie Chart)

fig = px.pie(asia, values='Daily Oil Consumption (Barrels)',names='Country',hole=0.4)
fig.update_layout(title='Percentage of Daily Oil Consumption (Barrels)',font_size=15,title_x=0.45,annotations=[dict(text='DOC%',font_size=20, showarrow=False,height=800,width=700)])
fig.update_traces(textfont_size=15,textinfo='percent')

fig.show()

#VISULAIZATION OF WORLD SHARE (Bar Graph)

fig = px.bar(asia.head(10), x='Country',y='World Share',text_auto=True)
fig.update_layout(legend_orientation='h',legend=dict(x=0,y=1,traceorder='normal'),title="World Share of Petrol",margin=dict(l=0,r=0,t=30, b=0))
fig.show()

"""INDIA is contributing the highest among other four countries with 4.600% whereas Afganistan contributes to the least 0.0362%"""

fig = px.bar(asia.head(10),x='Country',y='Price Per Litre (USD)',text_auto=True)
fig.update_layout(legend_orientation='h',xaxis_tickangle=-45,title_x=0.45,legend=dict(x=0,y=1,traceorder='normal'),title = 'Price Per Litre (USD) of petrol',margin = dict(l=0,r=0,t=30,b=0))
fig.show()