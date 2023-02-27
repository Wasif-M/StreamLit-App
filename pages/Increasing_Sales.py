import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
st.title("Increasing Sales :red[Prediction] Model ")
img=plt.imread('sales-878979_.jpg')
st.image(img)

df=pd.read_csv('Advertising.csv')
st.dataframe(df)
df['total_spend']=df['TV']+df['radio']+df['newspaper']
f1=px.histogram(df['total_spend'],marginal='box',nbins=20)
col1,col2=st.columns(2)
col1.plotly_chart(f1,use_container_width=True)
f1=px.histogram(df['sales'],marginal='box',nbins=20)
col1.plotly_chart(f1,use_container_width=True)
