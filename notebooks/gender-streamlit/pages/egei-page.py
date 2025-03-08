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

#egei index (by thorben)
# Define the categories, subcategories, their weightings, and negative weighting
included_categories = {
    "Educational background": [
        ("Low education background (ISCED 0-2)", 11.00177),
        ("Medium education background (ISCED 3-4)", 11.00177),
        ("Short-cycle tertiary education background (ISCED 5)", 11.00177),
        ("Tertiary education background (ISCED 6-8)", 11.00177)
    ],
    "Financial difficulties": [
        ("with financial difficulties", 4.398494666),  # Higher weight for more severe state
        ("with somewhat financial difficulties", 4.398494666),
        ("without financial difficulties", 4.398494666)
    ],
    "Severity of impairment": [
        ("severely limited in studies", 8.9170966),  # More severe
        ("limited in studies", 8.9170966),
        ("not limited at all in studies", 8.9170966)
    ],
    "Parental wealth": [ #Combined weight = 32.008387
        ("very well-off", 6.40167),
        ("somewhat well-off", 6.40167),
        ("average", 6.40167),
        ("not very well-off", 6.40167),
        ("not at all well-off", 6.40167)
    ]    
}
# Define negative weighting for specific subcategories (negative sign indicates negative impact for FLINTA)
negative_weighting = {
    "Financial difficulties": [
        "with financial difficulties",  # Negative impact for FLINTA
        "with somewhat financial difficulties"  # Negative impact for FLINTA
    ],
    "Severity of impairment": [
        "severely limited in studies",  # Negative impact for FLINTA
        "limited in studies"  # Negative impact for FLINTA
    ]
}

# Create a dictionary to store the gender equality index (GEI) values for each country
gei_results = {}

# Get unique list of countries
countries = gender_df["country"].unique()

# Iterate over each country
for country in countries:
    country_data = gender_df[gender_df["country"] == country]  # Filter data for this country
    
    category_ratios = []  # Store weighted ratios per category
    
    # Iterate through each category
    for category, subcategories in included_categories.items():
        subcategory_ratios = []  # Store ratios for all subcategories in this category
        total_weight = 0  # Keep track of total weight for weighted average
        
        # Check if the category has negative weighting
        is_negative = category in negative_weighting and negative_weighting[category]
        
        # Iterate over subcategories in each category
        for subcategory, weight in subcategories:
            flinta_col = f"{category} , {subcategory}, FLINTA*"
            male_col = f"{category} , {subcategory}, Male"
            
            if flinta_col in gender_df.columns and male_col in gender_df.columns:
                x = country_data[flinta_col].values[0]  # FLINTA* value
                y = country_data[male_col].values[0]  # Male value

                # Avoid division by zero and check for valid values
                if y > 0 and pd.notna(x) and pd.notna(y):
                    # Calculate the ratio based on the connotation
                    if is_negative:
                        ratio = y / x  # Reversed ratio for negative connotation
                    else:
                        ratio = x / y  # Normal ratio for positive connotation
                    
                    # Weight the ratio by the subcategory's weight
                    subcategory_ratios.append(ratio * weight)
                    total_weight += weight
        
        # Compute the weighted average ratio for this category
        if total_weight > 0:
            category_ratio = np.sum(subcategory_ratios) / total_weight
            category_ratios.append(category_ratio)
    
    # Compute the log of the ratios for each category
    if category_ratios:
        ln_ratios = [np.log(r) for r in category_ratios if r > 0]  # Avoid log(0)
        
        if ln_ratios:
            # Compute the average of the logarithmic values
            ln_R_bar = np.mean(ln_ratios)
            GEI = np.exp(ln_R_bar) * 100  # Compute the final Gender Equality Index (GEI) score

            # Store result
            gei_results[country] = GEI

# Convert results to DataFrame
egei_df = pd.DataFrame(list(gei_results.items()), columns=["Country", "GEI"])

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

st.title("GEITEA-Index")
st.write("Gender Equality Index for Tertiary Education Access")

col1, col2 = st.columns([0.4,0.6])

with col1:
    with st.container(border=True):
        st.subheader("Explanation")
        st.write("This Index is inspired by the EGEI-Index from Eduardo Bericat and weights different factors:")
        st.markdown("* Educational dackground")
        st.markdown("* Financial difficulties")
        st.markdown("* Severety of impairment in tertiary education")
        st.markdown("* Parental wealth")
        
        

with col2:
    ax, fig = new_plot("None")
    sns.barplot(x='Country',
                y='GEI',
                palette=palette_disc,
                data=egei_df,
                ax=ax,
                order=egei_df.sort_values('GEI', ascending=False)['Country'])
    plt.ylabel('GEITEA-Index (%)')
    plt.xlabel('Country')
    plt.ylim(80,110)
    ax.axhline(100,color=palette_disc[20])
    st.pyplot(fig)
    st.caption(" 100< - Inequality favoring women | 100= - Equality | 100> - Inequality favoring men")