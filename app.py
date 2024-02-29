import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd
st.header(':red[Jan Gustaffson vs Etienne Gardé]')
with st.container(border=True):
    st.header('Spielstand 96:0')


# Add histogram data
x1 = np.random.randn(90) 
x2 = x1 * x1
fig = px.scatter(pd.DataFrame({'x1': x1, 'x2': x1}),
                 x='x1',
                 y='x2',
                 color='x1')

# Plot!
with st.container(border=True):
    st.header(':red[Youtube Statistiken]')
    st.plotly_chart(fig, use_container_width=True)
with st.container(border=True):
    st.header(':red[Spiel Genauigkeit]')
    st.plotly_chart(fig, use_container_width=True)
with st.container(border=True):
    st.header(':red[Beste Position für Gardé]')
    st.plotly_chart(fig, use_container_width=True)
with st.container(border=True):
    st.header(':red[Dauer des Spiels]')
    st.plotly_chart(fig, use_container_width=True)