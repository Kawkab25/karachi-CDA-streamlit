# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 15:44:58 2023

@author: kawka
"""
import pandas as pd
import streamlit as st
df = pd.read_csv("Billionaire.csv")


all_countries = sorted(df['Country'].unique()) 
#can do this statement in two different lines
#creating containers for streamlit layout
st.title('Billionaire Dataset')
col1, col2 = st.columns(2)
selected_country = col1.selectbox('Select your Country', all_countries)
#subset on selected country
subset_country  = df[df['Country']== selected_country]
#get unique sources from the selected country
sources = sorted(subset_country['Source'].unique())
#display multiselect option on source
selected_source = col1.multiselect('Select source of income', sources)
#subset on selected source
subset_source = subset_country[subset_country['Source'].isin(selected_source)]
#use isin with multiselect
#columns 2
main_string = '{} - Billionaire'.format(selected_country)
#main_string = selected_country + ' - Billionaires'
col2.header(main_string)
col2.dataframe(subset_country)
col2.header('Source wise info:')
col2.dataframe(subset_source)