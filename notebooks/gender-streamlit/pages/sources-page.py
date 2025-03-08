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

#streamlit run C:\Users\sirim\source\gender-streamlit\app.py

# Load data
file_path = "C:/Users/sirim/source/gender-streamlit/cleaned_data.xlsx"
gender_df = pd.read_excel(file_path)
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

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
        st.write(title)
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

st.title("Sources")
st.write("Index: Bericat, E. The European Gender Equality Index: Conceptual and Analytical Issues. Soc Indic Res 108, 1–28 (2012).")
st.page_link("https://doi.org/10.1007/s11205-011-9872-z", label="Link", icon="🌎")
st.write("Index: Palmisano, F., Biagi, F. & Peragine, V. Inequality of Opportunity in Tertiary Education: Evidence from Europe. Res High Educ 63, 514–565 ")
st.page_link("https://doi.org/10.1007/s11162-021-09658-4", label="Link", icon="🌎")
st.write("PhD Graduates: She Figures")
st.page_link(" https://projects.research-and-innovation.ec.europa.eu/en/knowledge-publications-tools-and-data/interactive-reports/she-figures-2024#chapters", label="Link", icon="🌎")

st.subheader("Dataset")
st.write(gender_df)
st.caption("https://database.eurostudent.eu/drm/")