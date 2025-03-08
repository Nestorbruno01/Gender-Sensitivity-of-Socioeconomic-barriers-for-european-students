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

options = ["High Financial Difficulties",
                "Severely Impaired",
                "Low Parental Education",
                "Low Parental Wealth",
                "Dependency on self-earned income"]

#insteresting columns
list = ['Financial difficulties , with financial difficulties, FLINTA*',
        'Severity of impairment , severely limited in studies, FLINTA*',
        'Highest educational attainment of parents (aggregated) , No higher tertiary education (ISCED 2011 0-4), FLINTA*',
        'Parental wealth , not at all well-off, FLINTA*',
        'Dependency on income source , dependent on self-earned income, FLINTA*']

#Sidebar
#https://fonts.google.com/icons
st.sidebar.header("Menu")
with st.sidebar.container(border=True):
    st.markdown("*To what extent does the impact of socioeconomic disparities on European students differ with regard to gender?*")
st.sidebar.page_link("app.py", label="Overall", icon=":material/home:")
st.sidebar.page_link("pages/heatmap-page.py", label="Comparisons", icon=":material/compare_arrows:")
with st.sidebar:
    with st.container(border=True):
        selection = st.radio("",options, label_visibility="collapsed")
st.sidebar.page_link("pages/egei-page.py",label="GEITEA-Index", icon=":material/functions:")
st.sidebar.page_link("pages/phd-page.py",label="PhD Graduates", icon=":material/school:")
st.sidebar.page_link("pages/survey-page.py", label="Survey", icon=":material/ar_stickers:")
st.sidebar.page_link("pages/sources-page.py", label="Sources", icon=":material/auto_stories:")

if selection == "High Financial Difficulties":
    column = list[0]
elif selection == "Severely Impaired":
    column = list[1]
elif selection == "Low Parental Education":
    column = list[2]
elif selection == "Low Parental Wealth":
    column = list[3]
elif selection == "Dependency on self-earned income":
    column = list[4]

#used colour palette - continouus
palette_cont = sns.color_palette('RdBu', as_cmap=True)
palette_cont_rev = palette_cont.reversed()

#used colour palette - discrete
palette_disc = sns.color_palette('RdBu',len(gender_df))
palette_disc_rev = palette_disc[::-1]

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

st.title(f"Comparisons - {selection}")
col1, col2 = st.columns([0.6,0.4])

with col1:
    #Modify original dataframe to merge with Geodataframe
    gender_df_map = gender_df
    countries_to_be_added = ['SL','BLR','UA', 'ALB',
                            'MV','BLG','LX','BG','IT','UK','SN',
                            'BH','NM','RSN','MNE','KOS',]
    placeholder_value = np.nan
    for i in countries_to_be_added:
        new_row = {col: placeholder_value for col in gender_df_map.columns}
        new_row['country'] = i
        # Append the new row to the DataFrame
        gender_df_map = pd.concat([gender_df_map, pd.DataFrame([new_row])], ignore_index=True)
    gdf = gpd.read_file("C:/Users/sirim/source/gender-analysis/map")
    filtered_gdf = gdf[gdf['CONTINENT'].str.contains("Europe", na=False)]
    filtered_gdf = filtered_gdf.drop([18], axis=0).reset_index(drop=True)
    #Add row from main gdf to filtered gdf
    row_to_append = gdf.iloc[145]
    #Added Azerbaijan to Europe
    filtered_gdf = pd.concat([filtered_gdf, row_to_append.to_frame().T], ignore_index=True)
    row_to_append = gdf.iloc[146]
    #Added Georgia to Europe
    filtered_gdf = pd.concat([filtered_gdf, row_to_append.to_frame().T], ignore_index=True)
    kuerzel = ["NO", "FR", "SE", "BLR", "UA", "PL", "AT", "HU", "MV", "RO", "LT", "LV", "EE", "DE", "BLG", "GR", "ALB", "HR", "CH", "LX", "BG", "NL", "PT", "ES", "IE", 
            "IT", "DK", "UK", "IS", "SN", "FI", "SK", "CZ", "BH", "NM", "SB", "MNE", "KOS", "AZ", "GE"]
    filtered_gdf['Kuerzel'] = kuerzel
    # Sort the DataFrame by column names alphabetically
    df_sorted = filtered_gdf.sort_values(by='Kuerzel', ascending=True)
    gender_df_map = gender_df_map.sort_index(ascending=True)
    filtered_gdf = filtered_gdf.sort_index(ascending=True)

    filtered_gdf = filtered_gdf.sort_values(by='Kuerzel', ascending=True)
    gender_df_map = gender_df_map.sort_values(by='country', ascending=True)
    gender_df_map = gender_df_map.reset_index(drop=True)
    gender_df_map = gender_df_map.rename(columns={'country': 'Kuerzel'})
    merged_gdf = filtered_gdf.merge(gender_df_map, on='Kuerzel')
    
    merged_gdf['Difference'] = merged_gdf[column] - merged_gdf['All students , All students, FLINTA*']

    ax, fig = new_plot("None")
    divider = make_axes_locatable(ax)
    merged_gdf.plot(column='Difference',
                    ax = ax,
                    legend = True,
                    cmap=palette_cont,
                    missing_kwds={ "color": '#0e1117', "label": "Missing values"},
                    legend_kwds={'shrink': 0.5, "orientation":"horizontal"},
                    edgecolor='white')
    ax.set_xlim(-25, 51) 
    ax.set_ylim(35.5, 72) 
    ax.set_axis_off()
    
    st.pyplot(fig)

with col2:
    # Barchart: differences in gender representation (Nestor)
    # Calculate the difference between the two columns
    gender_df["FLINTA_Difference"] = (
        gender_df[column]-
        gender_df["All students , All students, FLINTA*"]
    )
    # Sort data by the calculated difference in ascending order
    ranking_df = gender_df.sort_values(by="FLINTA_Difference", ascending=False)
    # Define custom colors: Red for negative values, Green for positive values
    colors = [palette_disc[0] if val < 0 else palette_disc[24] for val in ranking_df["FLINTA_Difference"]]
    # Plot horizontal bar chart
    ax1, fig = new_plot('None')
    sns.barplot(data=ranking_df,
                x="FLINTA_Difference",
                y="country",
                palette=colors,
                ax=ax1)
    # Labels
    ax1.set_xlabel("Difference in FLINTA* Share")
    ax1.set_ylabel("Country")
    #interactive: GDP-points showing
    gdp = st.toggle('Show GDP')
    if gdp:
        # Create secondary axis for GDP
        ax2 = ax1.twiny()
        # Plot GDP as a scatter plot on the secondary axis
        ax2.scatter(ranking_df["GDP per capita($)"], ranking_df["country"], color=palette_disc[12], marker="o", label="GDP")
        # Labels and legend for secondary axis
        ax2.set_xlabel("GDP")
        ax2.legend(loc="lower right")
        ax2.tick_params(colors='white')  # Make ticks white
        ax2.xaxis.label.set_color('white')  # Make X-axis label white
        ax2.yaxis.label.set_color('white')  # Make Y-axis label white
        ax2.title.set_color('white')  # Make title white
        ax2.spines['bottom'].set_color('white')  # X-axis line
        ax2.spines['left'].set_color('white') #Y-axis line
        ax2.spines['top'].set_color('white')  # X-axis line
        ax2.spines['right'].set_color('white') #Y-axis line
    st.pyplot(fig)

    with st.expander("Correlation with the GDP?"):
        # Regression line: GDP and Flinta attainment (Jette)
        st.write("No.")
        ax, fig = new_plot("FLINTA*s studying vs GDP per capita ($)")
        plt.scatter(gender_df['GDP per capita($)'], gender_df['All students , All students, FLINTA*'], color=palette_disc[18], label='Data points')
        plt.xlabel('GDP per capita ($)')
        plt.ylabel('All FLINTA*s in higher education')
        plt.grid(True)
        # Add a linear regression line
        from sklearn.linear_model import LinearRegression
        regressor = LinearRegression()
        regressor.fit(gender_df[['GDP per capita($)']], gender_df['All students , All students, FLINTA*'])
        plt.plot(gender_df['GDP per capita($)'], regressor.predict(gender_df[['GDP per capita($)']]), color=palette_disc[3], label='Regression Line')

        # Show the plot
        plt.legend()
        st.pyplot(fig)