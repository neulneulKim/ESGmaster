import pandas as pd
import streamlit as st

DATA_PATH = "./"
SEED = 42
df = pd.read_csv("df_0702_등급맵핑.csv")
st.write(df)