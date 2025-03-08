import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import math
import geopandas as gpd
import fiona
from mpl_toolkits.axes_grid1 import make_axes_locatable
import qrcode # type: ignore
from io import BytesIO

#streamlit run C:\Users\sirim\source\gender-streamlit\app.py

# Load data
file_path = "C:/Users/sirim/source/gender-streamlit/cleaned_data.xlsx"
gender_df = pd.read_excel(file_path)
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

#used colour palette - continouus
palette_cont = sns.color_palette('RdBu', as_cmap=True)
palette_cont_rev = palette_cont.reversed()

#used colour palette - discrete
palette_disc = sns.color_palette('RdBu',len(gender_df))
palette_disc_rev = palette_disc[::-1]

#used colour palette - blue&red
palette_gender = sns.color_palette('RdBu')

#backgorund color & text color
bg_color=st.get_option('theme.backgroundColor')
text_color = st.get_option("theme.textColor")

#define new plot
def new_plot (title):
    if title is not "None":
        st.subheader(title)
    fig,ax = plt.subplots()
    ax.set_facecolor('none')
    fig.patch.set_alpha(0)  # Fully transparent figure
    ax.patch.set_alpha(0)
    ax.tick_params(colors='white')  # Make ticks white
    ax.xaxis.label.set_color('white')  # Make X-axis label white
    ax.yaxis.label.set_color('white')  # Make Y-axis label white
    ax.title.set_color('white')  # Make title white
    ax.spines['bottom'].set_color('white')  # X-axis line
    ax.spines['left'].set_color('white') #Y-axis line
    ax.spines['top'].set_color('white')  # X-axis line
    ax.spines['right'].set_color('white') #Y-axis line
    return ax, fig 
    #then add code
    #end with: st.pyplot(fig)

#Sidebar
#https://fonts.google.com/icons
st.sidebar.header("Menu")
with st.sidebar.container(border=True):
    st.markdown("*To what extent does the impact of socioeconomic disparities on European students differ with regard to gender?*")
st.sidebar.page_link("app.py", label="Overall", icon=":material/home:")
st.sidebar.page_link("pages/heatmap-page.py", label="Comparisons", icon=":material/compare_arrows:")
st.sidebar.page_link("pages/egei-page.py",label="EGEI-Index", icon=":material/functions:")
st.sidebar.page_link("pages/phd-page.py",label="PhD Graduates", icon=":material/school:")
st.sidebar.page_link("pages/survey-page.py", label="Survey", icon=":material/ar_stickers:")
st.sidebar.page_link("pages/sources-page.py", label="Sources", icon=":material/auto_stories:")

qr = qrcode.make("https://conference-week-app.streamlit.app")
buffer = BytesIO()
qr.save(buffer, format="PNG")
buffer.seek(0)

st.title("How about you?")

col1,col2 = st.columns([0.6,0.4])

with col2:
    st.page_link("https://conference-week-app.streamlit.app", label="Survey")

with col1:
    st.image(buffer, caption="Scan this QR Code", use_container_width=True)

