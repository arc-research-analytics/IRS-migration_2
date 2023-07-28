import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title='Money Mover Dashboard', 
    layout="wide", 
    page_icon="💰"
    )

hide_default_format = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        section.main > div:has(~ footer ) {
        padding-bottom: 5px;}
        div.block-container{padding-top:1.5rem;}
       </style>
       """

st.markdown(hide_default_format, unsafe_allow_html=True)

summary = st.sidebar.radio(
    'Summary level:',
    ('11-County Metro Region', 'Single County')
    )

county = ''

if summary == '11-County Metro Region':
    county = ''
else:
    county = st.sidebar.selectbox(
        'Select metro county:',
        ('Cherokee County', 
        'Clayton County', 
        'Cobb County', 
        'DeKalb County', 
        'Douglas County', 
        'Fayette County', 
        'Forsyth County', 
        'Fulton County', 
        'Gwinnett County', 
        'Henry County', 
        'Rockdale County'),
    )

summary_dict = {
    '11-County Metro Region':'metro Atlanta',
    'Single County':f'{county}'
}

# MIGRATION DIRECTION vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
mig_direction = st.sidebar.radio(
    f'Flow direction:',
    ('In', 'Out')
)

direction_lower = mig_direction.lower()

mig_direction_dict = {
    'In': 'into',
    'Out': 'out of'
}

mig_direction_dict2 = {
    'In': 'originations',
    'Out': 'destinations'
}

mig_direction_dict3 = {
    'In': 'Origination',
    'Out': 'Destination'
}
# MIGRATION DIRECTION ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


# SLIDERvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
slider_years = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
slider_start = slider_years[0]
slider_end = slider_years[-1]

years = st.sidebar.slider(
    'Year range:',
    slider_start,slider_end,(2019,2021)
)
# convert years selected to list
years = list(years)

# get full range of years included by the slider
def fill_in_years(lst):
    n1 = lst[0]
    n2 = lst[-1]
    lst[:] = range(n1, n2 + 1)
    return lst

full_years = fill_in_years(years)

# SLIDER^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


# sidebar spacing
if summary == 'Single County':
    st.sidebar.text("")

else:
    st.sidebar.text("")
    st.sidebar.text("")
    st.sidebar.text("")
    st.sidebar.text("")
    st.sidebar.text("")
    st.sidebar.text("")
