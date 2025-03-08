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
st.sidebar.page_link("pages/egei-page.py",label="GEITEA-Index", icon=":material/functions:")
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

st.title("Gender-Sensitivity to Socioeconomic Background & Higher Education Attainment")
#st.write("Analyzing the impact of socioeconomic status on education with respect to gender.")

col1, col2 = st.columns([0.4,0.6])

with col1:
    #interactive piechart: Average gender distribution all countries
    st.subheader('Average Gender Distribution of All Students Across Countries')
    options = ["Overall","Low educational background"]
    selection = st.segmented_control("Filter", options, selection_mode="single", default="Overall", label_visibility="collapsed")

    if selection == "Overall":
        # Calculate the average percentages across countries
        flinta_avg = gender_df["All students , All students, FLINTA*"].mean()
        male_avg = gender_df["All students , All students, Male"].mean()
        # Plot pie chart
        ax, fig = new_plot("None") 

    elif selection == "Low educational background":
        # Convert and clean the columns
        flinta_avg = gender_df['Educational background , Low education background (ISCED 0-2), FLINTA*'].mean()
        male_avg = gender_df['Educational background , Low education background (ISCED 0-2), Male'].mean()
        #plot the pie chart
        ax, fig = new_plot('None')
    
    plt.pie([flinta_avg, male_avg],
            labels=["FLINTA*", "Male"],
            colors=[palette_disc[0],palette_disc[24]],
            autopct="%.1f%%",
            startangle=90,
            wedgeprops={"edgecolor": "white"},
            textprops={'color':'w'})
    st.pyplot(fig)

with col2:
    with st.container(border=True):
        #Interactive stacked barchart: Distribution in genders
        # selection for y-axis
        options = ["Financial Difficulties",
                "Dependency on Income Source",
                "Severety of Impairment",
                "Parental Education",
                "Parental Wealth"]
        st.subheader("Normalised Distributions by Gender")
        selection = st.radio("",options, label_visibility="collapsed")
        
        if selection=="Financial Difficulties":
            fin_diff_columns_flinta = [
                "Financial difficulties , with financial difficulties, FLINTA*",
                "Financial difficulties , with somewhat financial difficulties, FLINTA*",
                "Financial difficulties , without financial difficulties, FLINTA*"
            ]

            fin_diff_columns_male = [
                "Financial difficulties , with financial difficulties, Male",
                "Financial difficulties , with somewhat financial difficulties, Male",
                "Financial difficulties , without financial difficulties, Male"
            ]

            # Extract and sum data for visualization
            distribution = pd.DataFrame({
                "Gender": ["FLINTA*", "Male"],
                "With Difficulties": [gender_df[fin_diff_columns_flinta[0]].sum(), gender_df[fin_diff_columns_male[0]].sum()],
                "Somewhat Difficulties": [gender_df[fin_diff_columns_flinta[1]].sum(), gender_df[fin_diff_columns_male[1]].sum()],
                "Without Difficulties": [gender_df[fin_diff_columns_flinta[2]].sum(), gender_df[fin_diff_columns_male[2]].sum()]
            })
        elif selection=="Dependency on Income Source":
            income_columns_flinta = [
                "Dependency on income source , dependent on family, FLINTA*",
                "Dependency on income source , dependent on self-earned income, FLINTA*",
                "Dependency on income source , dependent on public student support, FLINTA*",
                "Dependency on income source , other, FLINTA*"
            ]

            income_columns_male = [
                "Dependency on income source , dependent on family, Male",
                "Dependency on income source , dependent on self-earned income, Male",
                "Dependency on income source , dependent on public student support, Male",
                "Dependency on income source , other, Male"
            ]

            # Extract and sum data for visualization
            distribution = pd.DataFrame({
                "Gender": ["FLINTA*", "Male"],
                "Dependent on Family": [gender_df[income_columns_flinta[0]].sum(), gender_df[income_columns_male[0]].sum()],
                "Dependent on Self-earned Income": [gender_df[income_columns_flinta[1]].sum(), gender_df[income_columns_male[1]].sum()],
                "Dependent on Public Support": [gender_df[income_columns_flinta[2]].sum(), gender_df[income_columns_male[2]].sum()],
                "Other Sources": [gender_df[income_columns_flinta[3]].sum(), gender_df[income_columns_male[3]].sum()]
            })
        elif selection=="Severety of Impairment":
            columns_flinta = [
                "Severity of impairment , severely limited in studies, FLINTA*",
                "Severity of impairment , limited in studies, FLINTA*",
                "Severity of impairment , not limited at all in studies, FLINTA*"
            ]

            columns_male = [
                "Severity of impairment , severely limited in studies, Male",
                "Severity of impairment , limited in studies, Male",
                "Severity of impairment , not limited at all in studies, Male"
            ]

            # Extract and sum data for visualization
            distribution = pd.DataFrame({
                "Gender": ["FLINTA*", "Male"],
                "Severely limited in Studies": [gender_df[columns_flinta[0]].sum(), gender_df[columns_male[0]].sum()],
                "Limited in Studies": [gender_df[columns_flinta[1]].sum(), gender_df[columns_male[1]].sum()],
                "Not limited at all in Studies": [gender_df[columns_flinta[2]].sum(), gender_df[columns_male[2]].sum()]
            })
        elif selection=="Parental Education":
            columns_flinta = [
                "Highest educational attainment of parents (aggregated) , No higher tertiary education (ISCED 2011 0-4), FLINTA*",
                "Highest educational attainment of parents (aggregated) , Tertiary education (ISCED 2011 5-8), FLINTA*",
                "Highest educational attainment of parents (aggregated) , Do not know, FLINTA*"
            ]

            columns_male = [
                "Highest educational attainment of parents (aggregated) , No higher tertiary education (ISCED 2011 0-4), Male",
                    "Highest educational attainment of parents (aggregated) , Tertiary education (ISCED 2011 5-8), Male",
                    "Highest educational attainment of parents (aggregated) , Do not know, Male"
            ]

            # Extract and sum data for visualization
            distribution = pd.DataFrame({
                "Gender": ["FLINTA*", "Male"],
                "No higher tertiary Education": [gender_df[columns_flinta[0]].sum(), gender_df[columns_male[0]].sum()],
                "Tertiary Education": [gender_df[columns_flinta[1]].sum(), gender_df[columns_male[1]].sum()],
                "Do not know": [gender_df[columns_flinta[2]].sum(), gender_df[columns_male[2]].sum()]
            })
        elif selection=="Parental Wealth":
            columns_flinta = [
                "Parental wealth , very well-off, FLINTA*",
                "Parental wealth , somewhat well-off, FLINTA*",
                "Parental wealth , average, FLINTA*",
                "Parental wealth , not very well-off, FLINTA*",
                "Parental wealth , not at all well-off, FLINTA*"]

            columns_male = [
            "Parental wealth , very well-off, Male",
                "Parental wealth , somewhat well-off, Male",
                "Parental wealth , average, Male",
                "Parental wealth , not very well-off, Male",
                "Parental wealth , not at all well-off, Male"]

            # Extract and sum data for visualization
            distribution = pd.DataFrame({
                "Gender": ["FLINTA*", "Male"],
                "Very well-off": [gender_df[columns_flinta[0]].sum(), gender_df[columns_male[0]].sum()],
                "Somewhat well-off": [gender_df[columns_flinta[1]].sum(), gender_df[columns_male[1]].sum()],
                "Average": [gender_df[columns_flinta[2]].sum(), gender_df[columns_male[2]].sum()],
                "Not very well-off": [gender_df[columns_flinta[3]].sum(), gender_df[columns_male[3]].sum()],
                "Not at all well-off": [gender_df[columns_flinta[4]].sum(), gender_df[columns_male[4]].sum()]
            })
    

        # Normalize the values so that each gender sums to 100%
        distribution.set_index("Gender", inplace=True)
        edu_distribution = distribution.div(distribution.sum(axis=1), axis=0) * 100  # Convert to percentages

        # Plot normalized stacked bar chart
        ax, fig = new_plot("None")
        edu_distribution.plot(kind="bar", stacked=True, colormap=palette_cont, ax=ax)
        # Labels and title
        plt.xlabel("Gender")
        plt.ylabel("Percentage (%)")
        plt.xticks(rotation=0)  # Keep gender labels horizontal
        plt.legend(title=selection)
        st.pyplot(fig)

#st.subheader("Conclusion")
#st.write("This analysis provides insights into how socioeconomic background affects educational attainment, with gender as a key factor. Further improvements could include more features and deeper statistical analysis.")
#st. write("Those features could be the average age of motherhood or mariage of FLINTA*s in different countries.")