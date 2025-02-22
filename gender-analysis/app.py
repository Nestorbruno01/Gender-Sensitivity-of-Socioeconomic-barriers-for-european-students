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

#streamlit run C:\Users\sirim\source\gender-analysis\app.py

# Load data
file_path = "C:/Users/sirim/source/gender-analysis/gender_data.xlsx"
gender_df = pd.read_excel(file_path)
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

#define inequality-index
def egei(country):
    impair=gender_df.loc[gender_df['country']==country,"Severity of impairment , severely limited in studies, FLINTA*"]/gender_df.loc[gender_df['country']==country,"Severity of impairment , severely limited in studies, Male"]
    fin_diff=gender_df.loc[gender_df['country']==country,"Financial difficulties , with financial difficulties, FLINTA*"]/gender_df.loc[gender_df['country']==country,"Financial difficulties , with financial difficulties, Male"]
    edu_bg=gender_df.loc[gender_df['country']==country,"Educational background , Low education background (ISCED 0-2), FLINTA*"]/gender_df.loc[gender_df['country']==country,"Educational background , Low education background (ISCED 0-2), Male"]
    att_par=gender_df.loc[gender_df['country']==country,"Highest educational attainment of parents (aggregated) , No higher tertiary education (ISCED 2011 0-4), FLINTA*"]/gender_df.loc[gender_df['country']==country,"Highest educational attainment of parents (aggregated) , No higher tertiary education (ISCED 2011 0-4), Male"]
    par_weal=gender_df.loc[gender_df['country']==country,"Parental wealth , not at all well-off, FLINTA*"]/gender_df.loc[gender_df['country']==country,"Parental wealth , not at all well-off, Male"]
    index=2.718281828459045**((math.log(impair)+math.log(fin_diff)+math.log(edu_bg)+math.log(att_par)+math.log(par_weal))/5)*100
    return index

#add inequality index to df
gender_df['EGEI-Index']=gender_df['country'].apply(egei)

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

st.title("Socioeconomic Background & Higher Education Attainment")
st.write("Analyzing the impact of socioeconomic status on education with respect to gender.")

if st.button("See further analysis (PhD graduates)"):
    st.switch_page("pages/phd-page.py")

col1, col2, col3 = st.columns([0.39,0.26,0.35])

with col1:
    #Barchart: female student percentage for each country
    ax, fig = new_plot('Amount of FLINTA*s in each country') 
    sns.barplot(x='country',
                y='All students , All students, FLINTA*',
                palette=palette_disc,
                data=gender_df,
                ax=ax,
                order=gender_df.sort_values('All students , All students, FLINTA*', ascending=False)['country'])
    plt.ylim(0,100)
    plt.ylabel('Amount of FLINTA* students (%)')
    plt.xlabel('Country')
    ax.axhline(gender_df["All students , All students, FLINTA*"].mean(),color=palette_disc[20])
    st.pyplot(fig)

with col2:
    #interactive piechart: Average gender distribution all countries
    st.write('Average Gender Distribution of All Students Across Countries')
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

with col3:
    with st.container(border=True):
        #Interactive stacked barchart: Distribution in genders
        # selection for y-axis
        options = ["Educational Background",
                "Financial Difficulties",
                "Dependency on Income Source",
                "Severety of Impairment",
                "Parental Education",
                "Parental Wealth"]
        st.write("Normalised Distributions by Gender")
        selection = st.radio("",options, label_visibility="collapsed")
        if selection =="Educational Background":
            edu_columns_flinta = [
                "Educational background , Low education background (ISCED 0-2), FLINTA*",
                "Educational background , Medium education background (ISCED 3-4), FLINTA*",
                "Educational background , Short-cycle tertiary education background (ISCED 5), FLINTA*",
                "Educational background , Tertiary education background (ISCED 6-8), FLINTA*",
                "Educational background , Don't know, FLINTA*"
            ]
            edu_columns_male = [
                "Educational background , Low education background (ISCED 0-2), Male",
                "Educational background , Medium education background (ISCED 3-4), Male",
                "Educational background , Short-cycle tertiary education background (ISCED 5), Male",
                "Educational background , Tertiary education background (ISCED 6-8), Male",
                "Educational background , Don't know, Male"
            ]

            # Extract data for visualization
            distribution = pd.DataFrame({
                "Gender": ["FLINTA*", "Male"],
                "Low Education": [gender_df[edu_columns_flinta].sum().sum(), gender_df[edu_columns_male].sum().sum()],
                "Medium Education": [gender_df[edu_columns_flinta[1]].sum(), gender_df[edu_columns_male[1]].sum()],
                "Short-cycle Tertiary": [gender_df[edu_columns_flinta[2]].sum(), gender_df[edu_columns_male[2]].sum()],
                "Tertiary Education": [gender_df[edu_columns_flinta[3]].sum(), gender_df[edu_columns_male[3]].sum()],
                "Don't know": [gender_df[edu_columns_flinta[4]].sum(), gender_df[edu_columns_male[4]].sum()]
            })
        elif selection=="Financial Difficulties":
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
        plt.legend(title="Educational Background")
        st.pyplot(fig)

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
    
    merged_gdf['Difference'] = merged_gdf['All students , All students, FLINTA*'] - merged_gdf['Severity of impairment , severely limited in studies, FLINTA*']

    ax, fig = new_plot("None")
    divider = make_axes_locatable(ax)
    merged_gdf.plot(column='Difference',
                    ax = ax,
                    legend = True,
                    cmap=palette_cont,#'autumn'
                    missing_kwds={ "color": '#0e1117', "label": "Missing values"},
                    legend_kwds={'shrink': 0.5, "orientation":"horizontal"},
                    edgecolor='white')
    ax.set_xlim(-25, 50) 
    ax.set_ylim(27, 73) 
    ax.set_axis_off()
    
    st.write("Likelihood of Impairment in FLINTA*, adjusted, inversed")
    st.pyplot(fig)

with col2:
    # Barchart: differences in gender representation (Nestor)
    # Calculate the difference between the two columns
    gender_df["FLINTA_Difference"] = (
        gender_df["Educational background , Low education background (ISCED 0-2), FLINTA*"] - 
        gender_df["All students , All students, FLINTA*"]
    )
    # Sort data by the calculated difference in ascending order
    ranking_df = gender_df.sort_values(by="FLINTA_Difference", ascending=False)
    # Define custom colors: Red for negative values, Green for positive values
    colors = [palette_disc[0] if val < 0 else palette_disc[24] for val in ranking_df["FLINTA_Difference"]]
    # Plot horizontal bar chart
    ax1, fig = new_plot('Difference in FLINTA* Representation: Background of Low Education vs. All Students')
    sns.barplot(data=ranking_df,
                x="FLINTA_Difference",
                y="country",
                palette=colors,
                ax=ax1)
    # Labels
    ax1.set_xlabel("Difference in FLINTA* Share (Low educational background - All Students)")
    ax1.set_ylabel("Country")
    #interactive: GDP-points showing
    gdp = st.toggle('Show GDP')
    if gdp:
        # Create secondary axis for GDP
        ax2 = ax1.twiny()
        # Plot GDP as a scatter plot on the secondary axis
        ax2.scatter(gender_df["GDP per capita($)"], ranking_df["country"], color=palette_disc[12], marker="o", label="GDP")
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

col1,col2,col3 = st.columns([0.3,0.3,0.2])


with col1:
    # Regression line: GDP and Flinta attainment (Jette)
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

with col2:
    st.write("Calculated EGEI-Index")
    ax, fig = new_plot("None")
    sns.barplot(x='country',
                y='EGEI-Index',
                palette=palette_disc,
                data=gender_df,
                ax=ax,
                order=gender_df.sort_values('EGEI-Index', ascending=False)['country'])
    plt.ylabel('EGEI-Index')
    plt.xlabel('Country')
    ax.axhline(100,color=palette_disc[20])
    st.pyplot(fig)

    

with col3:
    st.write("Space for more")

#-----------------

#egei index fehler finden warum 2 länder keinen wert haben

# look at egai index code (wait for jette)
# make map and gdp points interactive (list of enes)
# EGEI-Index Visualization 
# add mean to first plot


#index
st.write(gender_df['EGEI-Index'])

# Display raw data
st.subheader("Raw Data Preview")
st.write(gender_df.head())

# Print column names for debugging
st.subheader("Dataset Columns")
st.write(gender_df.columns.tolist())

# Data Overview
st.subheader("Data Summary")
st.write(gender_df.describe())

st.subheader("Conclusion")
st.write("This analysis provides insights into how socioeconomic background affects educational attainment, with gender as a key factor. Further improvements could include more features and deeper statistical analysis.")
st. write("Those features could be the average age of motherhood or mariage of FLINTA*s in different countries.")