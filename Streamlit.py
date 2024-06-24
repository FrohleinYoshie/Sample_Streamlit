import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.write('### 1. CSVデータを生成して、テーブル表示する')
filename = 'money.csv'
if st.button(f'{filename}を生成'):
    df = pd.DataFrame({
        'ID': pd.date_range(start='2021-01-01', freq='D'),
        'money': np.random.rand() * 30,
    })
    df.to_csv(filename, index=False)

data = pd.read_csv(filename)
#st.write(data)

fig = px.line(data, x='ID', y='money', title='温度の時系列データ', markers=True)
#st.plotly_chart(fig)

col1, col2 = st.columns(2)

with col1:
    col1.line_chart(st.write(data))
with col2:
    col2.write(fig)
    