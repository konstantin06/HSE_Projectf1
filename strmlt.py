import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


df = pd.read_csv('newmnc.csv')
def strmlt():
    fig, ax = plt.subplots(figsize=(15, 5))
    x = list(df['position'])
    y = list(df['grid'])
    plt.scatter(x, y)
    plt.title('Correlation Monaco GP')
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.yticks(y)
    plt.xticks(x)
    plt.grid(True)
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))
    (np.unique(x)), color='red')
    return fig

st.title('Web app')
st.header('dataset')
st.dataframe(df, height=300)

if st.button('Show graph'):
    st.pyplot(strmlt())
else:
    st.info('Click on the button')