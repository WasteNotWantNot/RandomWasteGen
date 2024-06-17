import streamlit as st
import pandas as pd
import numpy as np
import json

with open('skips.json','r') as f:
  skips = json.load(f)

st.title('Random Waste Generator')
st.text('Select from the Dropdowns below to generate your weight:')
col1, col2, col3 = st.columns([2,1,1])
with col1:
    type = st.selectbox('Skip Type:', options = skips.keys(), key=1 )
with col2:
    size = st.selectbox('Skip Size:', options = skips[type].keys(), key = 2)
with col3:
    mn = skips[type][size]['Min']
    mx = skips[type][size]['Max']
    if (mn == 'NA' ):
        val = 'Input Ticket Value'
    else: 
        rng = np.random.random_sample()
        range = mx - mn
        num = round(range * rng, 3)
        val = round (mn + num, 3)
    st.text(f'Tonnage of Skip:\n{val}')