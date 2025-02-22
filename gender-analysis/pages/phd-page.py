import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import math

# Load data
file_path = "C:/Users/sirim/source/gender-analysis/gender_data.xlsx"
gender_df = pd.read_excel(file_path)
st.set_page_config(layout="wide",initial_sidebar_state="collapsed")

#used colour palette - continouus
palette_cont = sns.color_palette('RdYlGn', as_cmap=True)
palette_cont_rev = palette_cont.reversed()

#used colour palette - discrete
palette_disc = sns.color_palette('RdYlGn',len(gender_df))
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

st.title("Further Analysis of PhD graduates")
st.write("The data coming form other datasets was integrated to our original dataset.")

if st.button("Back to Main Page"):
    st.switch_page("app.py")

col1, col2, col3 = st.columns([0.3,0.3,0.4])

with col1:
    # Barchart: Full country names and FLINTA* percentages
    countries = [
        'Iceland', 'Estonia', 'Finland', 'Lithuania', 'Latvia', 'Denmark',
        'Spain', 'Croatia', 'Czech Republic', 'Austria', 'France', 'Germany',
        'Hungary', 'Ireland', 'Malta', 'Georgia', 'Azerbaijan', 'Switzerland'
    ]
    flinta_percentages = [
        65.96, 61.62, 58.48, 59.03, 58.29, 57.60, 58.15, 59.11,
        57.41, 56.27, 56.29, 50.65, 54.55, 54.13, 58.94, 53.36,
        50.95, 46.97
    ]
    # Overall average
    average_value = sum(flinta_percentages) / len(flinta_percentages)
    #Add average to countries
    data = list(zip(flinta_percentages, countries))
    data.append((average_value, "Average"))
    #Sort all data in descending order by percentage
    sorted_data = sorted(data, key=lambda x: x[0], reverse=True)
    sorted_percentages, sorted_countries = zip(*sorted_data)
    #Change colours
    colors = [palette_disc[2] if country == "Average" else palette_disc[8] for country in sorted_countries]
    #Create barchart
    ax, fig = new_plot("None")
    bars = ax.barh(sorted_countries, sorted_percentages, color=colors)
    #Invert the y-axis so the highest value is at the top
    ax.invert_yaxis()
    #Add labels to each bar at the edge
    ax.bar_label(bars, label_type="edge", color="white")
    #Update axis labels and title
    ax.set_xlabel('All students, FLINTA* (%)')
    st.write("FLINTA*s in Higher Education")
    st.pyplot(fig)

with col2:
    #Barchart: FLINTA PhD graduates by country
    countries = [
        'Iceland', 'Estonia', 'Finland', 'Lithuania', 'Latvia', 'Denmark',
        'Spain', 'Croatia', 'Czech Republic', 'Austria', 'France', 'Germany',
        'Hungary', 'Ireland', 'Malta', 'Georgia', 'Azerbaijan', 'Switzerland'
    ]
    flinta_percentages = [
        65.96, 61.62, 58.48, 59.03, 58.29, 57.60, 58.15, 59.11, 
        57.41, 56.27, 56.29, 50.65, 54.55, 54.13, 58.94, 53.36, 
        50.95, 46.97
    ]
    #calculate average
    average_value = sum(flinta_percentages) / len(flinta_percentages)
    #add average to countries
    data = list(zip(flinta_percentages, countries))
    data.append((average_value, "Average"))
    #sort the data in descending order by percentage
    sorted_data = sorted(data, key=lambda x: x[0], reverse=True)
    sorted_percentages, sorted_countries = zip(*sorted_data)
    #change colours
    colors = [palette_disc[2] if country == "Average" else palette_disc[8] for country in sorted_countries]
    # 5. Create the horizontal bar chart
    ax, fig = new_plot('None')
    bars = ax.barh(sorted_countries, sorted_percentages, color=colors)
    # 6. Invert the y-axis so the highest value is at the top
    ax.invert_yaxis()
    # 7. Label each bar with its integer-rounded percentage
    ax.bar_label(bars, label_type="edge", color="white")
    # 8. Set axis labels and title
    ax.set_xlabel('All students, FLINTA* (%)')
    plt.tight_layout()
    st.write("Proportion (%) of women among doctoral graduates (ISCED 8) Euro Student")
    st.pyplot(fig)

with col3:
    # Barchart: women, doctoral graduates, worldwide
    countries = [
        "Albania", "Canada", "Montenegro", "North Macedonia", "Brazil", 
        "Italy", "Serbia", "Bulgaria", "Romania", "Luxembourg",
        "France", "Croatia", "Slovenia", "Poland", "Latvia",
        "Estonia", "Norway", "Sweden", "Israel", "Finland",
        "Lithuania", "Netherlands", "Iceland", "Switzerland",
        "Andorra", "Slovakia", "Spain", "Greece", "Thailand",
        "Gabon", "United Kingdom", "EU-27", "Hungary", "Belgium",
        "Germany", "Czech Republic", "Austria", "Bosnia and Herzegovina",
        "Japan"
    ]
    values = [
        66.41, 66.20, 64.29, 59.63, 59.16,
        58.74, 55.16, 54.68, 54.66, 54.32,
        53.48, 53.14, 52.76, 52.39, 52.32,
        50.91, 50.59, 50.52, 50.12, 50.03,
        49.34, 49.28, 49.24, 48.93, 48.64,
        48.28, 48.03, 47.98, 47.50,
        47.16, 46.93, 46.72, 46.48, 45.93,
        44.91, 44.82, 44.67, 44.19, 31.96
    ]
    # Calculate average
    average_value = sum(values) / len(values)
    # Add average to countries
    data = list(zip(values, countries))
    data.append((average_value, "Average"))
    # Sort the data in descending order by value
    sorted_data = sorted(data, key=lambda x: x[0], reverse=True)
    sorted_values, sorted_countries = zip(*sorted_data)
    # change colours for average
    colors = [palette_disc[2] if country == "Average" else palette_disc[8] for country in sorted_countries]
    # 5. Create a horizontal bar chart
    ax, fig = new_plot("None")
    bars = ax.barh(sorted_countries, sorted_values, color=colors)
    # 6. Label each bar with its integer-rounded value plus '%'
    ax.bar_label(bars, label_type="edge", color="white")
    # 7. Invert the y-axis so the highest value is at the top
    ax.invert_yaxis()
    # 8. Set axis labels and title
    ax.set_ylabel("Country")
    plt.tight_layout()
    st.write("Proportion (%) of women among doctoral graduates, global")
    st.pyplot(fig)

st.subheader("Conclusion")
st.write("What is our conclusion?")