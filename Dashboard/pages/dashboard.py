import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title('this is the dashboard page')

df = sns.load_dataset('titanic')
st.dataframe(df)

fig = px.sunburst(df,path=['pclass','sex','survived'],
            values='age',title='survival by class and gender',width=500, height=500,
            template='plotly_dark',color='age',color_continuous_scale='brbg')
# st.plotly_chart(fig)

fig