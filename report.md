# Analysing the genderbased sensitivity towards socio-economic factors in higher education 
**Date: 2025-03-13**

**Authors:**
| Name    | Specific contribution to this report |
| -------- | ------- |
| Nestor Hilchenbach  | Data Analysis; Writing background, objectives, theoretical framework, findings, discussion, conclusion    |
| Jette Mischke | Writing findings, discussion, conclusion, editing; data analysis     |
| Thorben Weidelt    | Writing findings, data analysis methods, framework; data analysis; framework; citations; editing   |
| Enes Kizilbey |1.1, 4.4, 4.5, 5.1, 6.1(Data analyses and writing)|
| Siri Malin Weber | Data preprocessing; Streamlit Programming; Writing theoretical framework, data collection, limitations, conclusion |

## 1. Introduction

### 1.1 Background

The motivation for this research stems from personal experiences within our group, where we have observed that female students from financially disadvantaged families often encounter more significant socio-economic barriers than their male counterparts. Societal expectations and cultural norms frequently shape educational paths, influencing career trajectories and life choices. 

A compelling example of our group member Enes’s family experience illustrates this phenomenon. 

Enes grew up in a household with four siblings, two brothers and two sisters. Despite sharing the same home, same parents, and same financial situation, the educational paths of the siblings diverged significantly. While Enes and his brother pursued higher education, learned foreign languages, and embraced a more modern lifestyle, their two sisters followed a different route. They discontinued their education after secondary school and remained closer to traditional family roles 

This stark contrast in educational outcomes raised an important question: **Are there similar patterns exist beyond individual cases? Do female students across Europe, that come from disadvantaged socio-economic backgrounds, experience similar barriers in higher education ?**

In general, socioeconomical status (SES) has shown to be influencing the performance of students. Showing significant differences in their academic achievement, performance measured by test scores or even participance in extracurricular activities [1]. Factors like access to higher-quality schools, private tutoring or support by parents with academic degrees explain these effects. But it is important to note that there are many examples of students outperforming their SES, as well as underperforming students while coming from a background of high SES. Individual motivation and support systems can be seen as offsetting factors [1]. In our research we want to explore whether such effects and barriers vary regarding gender. Past research has shown that this phenomenon has impact on numeracy test results leading to gender gaps as early as grade three [2]. With our analysis we want to explore whether such disparities also exist among European students, especially when attaining higher education. According to our findings, among Eurostudent Survey countries, while the majority of bachelor, master and PhD students are female [3], we suspect this to change among students in weaker socio-economic positions. Within our research, we will encounter two of the 17 SDGs, part of the “Agenda 2030” set out by the United Nations. “SDG 4: Quality Education” as well as “SDG 5: Gender Equality” [3].  
The SDG 4 stands for quality of education that is inclusive and fair for everyone. It highlights the need for equal access to education, especially for people from marginalized or disadvantaged backgrounds. The SDG 5 focuses on achieving gender equality and empowering women and girls. It takes socioeconomic factors into account that hinder the access of individuals for a better life. Both are goals that go hand in hand with our ideas and objectives.

### 1.2 Objectives

This data exploration aims to provide a basic understanding of the interplay of gender and socio-economic status in students’ educational attainment. We want to analyse to what extent these socio-economic barriers and aggravating effects could be considered as gender sensitive.  

We aim to identify gender-based differences of socioeconomic differences on educational attainment in European countries, by examining relevant indicators such as financial background, parental academic achievement or impairment using python-based analysis. The goal is to uncover patterns which illustrate how these effects differ with gender and assess the potential factors that contribute to these differences. 

Secondly, we want to compare our findings across the European countries who are participating in the survey. By comparing the results from a cross-national perspective, we believe to gain valuable insights on regional trends, as well as country-specific characteristics. For that, we want to calculate an index to be able to compare the situation of specific countries. The index is intended to describe tertiary education access by looking at the gender distribution of people from different backgrounds and the gender distribution of people with financial problems. 

Finally, we want to present our findings by incorporating our results in an interactive, python-based dashboard. We believe visualizing them this way will allow the readers to interact with the data and gain a deep understanding of the transformative force of gender on the socioeconomic barriers in educational attainment.  

Ultimately, we want to raise understanding and awareness of the disparities and interactions between gender and socio-economic status we may encounter.

### 1.3 Research Question

This has led us to formulate our research question as following: 
**To what extent does the socioeconomic background of European students impact higher educational attainment with regard to gender?**

## 2. Theoretical Framework

The problem arising around socio-economic disparities and different opportunities due to those disparities is a highly relevant topic. It is broadly accepted that people having lower financial resources or not having parents with academic background are often disadvantaged when it comes to attainment of higher education. 

Munir et al. [1] highlighted that the SES of students heavily influences educational opportunities. Students coming from families with higher SES consistently perform better in academics due to increased access to better quality education, materials and also parental support, as the parents’ education is playing a big role in the educational performance of their children. Correspondingly, financial barriers appear to be disproportionally affecting students coming from families with a low SES.  

Research in general but also regarding this topic has become more intersectional the past years and thus has led to the question whether different genders are differently affected by those circumstances. 

When investigating how gender interacts with the SES in impacting students’ performance, Paterson et al [2] analysed numeracy skills. They found that especially the parents education level had a profound impact on the students’ performance, but there were differences in regards to gender. While a high level of education for the father had positive effects on both boys and girls, a higher education of the mother particularly had a positive impact on the girls, highlighting the importance of role models in the attempt of reducing gender gaps.  

For the investigation of gender equality in education Subrahmanian [4] has differentiated between two categories, gender parity and gender equality. Gender parity is defined as a quantitative goal, meaning an equal amount of male and female students participate in education.  Gender equality is a more qualitative goal as it is defined by equality in environments, processes and outcomes.  To achieve gender equality, both measures are important to map change and progress. With the statistical analysis conducted by this project, we focus on quantitative measures and thus on gender parity as a goal. 

Indices are often used to derive a statement from quantitative data. In recent decades, many indices have been developed to describe gender equality. According to Bericat [5], these often have their own definition of the concept. It is therefore important when carrying out a statistical analysis to precisely define the framework and the objective of the analysis. 

## 3. Methodology

### 3.1 Data Collection

The project uses a dataset made by eurostudent.eu [6] to analyze how different aspects of the socioeconomic background influence the attainment of European students. For that we search for correlations and trends with a focus on gender-specific differences.  

This dataset includes information about 25 European countries obtained through a self-assessment survey. It included various categories that provided insights into the socioeconomic backgrounds of the students. Each student self-identified within a specific sub-category in that category, which revealed the significance of that factor. Additionally, each sub-category included a gender distribution expressed in percentages. 

The dataset without any processing was useless to do data analysis because it was made to look aesthetic in excel. This is why we had to drop the first rows and columns in addition to dropping all empty rows and columns. 

The original dataset was also oriented in a way that was not intuitive, so we exchanged the rows and columns so that every row now represents the data of a country. This made it possible to calculate the arithmetic mean of specific features. 

Another issue was the description of the columns which were originally split up into 3 cells for each column. We joined them back together to make specific columns easier to find. We have grouped the gender options “Female, None, prefer not to assign myself to the categories offered” into one new category which is called “FLINTA*”. This is a German abbreviation for female, lesbian, intersexual, non-binary, trans and agender people. We decided on this category because these people have faced systemic barriers historically due to the patriarchal system. This system is still part of our society and thus also in the structures of university and education in general and we want to analyze whether these patriarchal barriers still exist in our context today. Additionally, it simplifies our research. 

We deleted all columns that are not important for our research question and changed the datatypes of columns only consisting of numeric values.  

Moreover, we added three additional columns. The columns “GDP per capita” and “unemployment” were taken from “World Bank, World Development Indicators” [7], and the data for the column “PhD female graduates” was found at “She Figures 2021, Gender in Research and Innovation” [8].

### 3.2 Data Analysis Methods

To find patterns and visualize the dataset we used several libraries and methods within Python. To generate plots and visualisations for a Streamlit app the libraries seaborn, matplotlib and geopandas were used.  

To interpret differences of gender distributions in different socioeconomic groups we calculated the algebraic differences between the proportion of male or FLINTA* students overall and the proportion of male or FLINTA* students of a specific socioeconomic group (e.g.  students with low parental wealth). To investigate correlations between different variables we used scatterplots and attempted linear regressions.  

For the conceptualisation of an index, we followed Bericat [3]. The index is described as Gender Equality Index for Tertiary Education Access (GEITEA). It is composed of 4 categories and 15 subcategories. Category selection criteria were the availability of data in the dataset and their descriptive relevance. The four categories applied were educational background, financial difficulties, severity of impairment in tertiary education and parental wealth (for details on subcategories view the Jupyter notebooks in the repository). To calculate values for categories we calculated FLINTA\* to male ratios. A value of R = 1 would then indicate perfect parity, a lower value indicates inequality favourable to men, a value R > 1 would indicate inequality favourable for FLINTA\*. What needs to be noted here, is that there is a problem in the dichotomy of FLINTA\* and male, as the FLINTA\* category contains genders that hold a different status and distribution within society than the categories of male and female. To accurately represent their status within this index would be a very complex issue. 

To summarize the ratios Ri into one number the GEITEA contains the arithmetic mean of the natural logarithms of the ratios. After calculating the arithmetic mean, the antilogarithm is applied. By this transformation the ratio function changes from a multiplicative into an additive function, thus each category has a linear effect on the final index [5]. This was also visible in a sensitivity analysis performed with the index. There were some subcategories included in which a higher representation was negative (e.g. severe impairment or financial difficulties in studies). For these we inversed the calculated ratio. We furthermore applied explicit weighting (weighting that is explicitly included and not due to the operationalization on the different categories after calculating the ratios. For that we included numbers from Palmisano [11] who attempted to quantify causes of inequality within education. We multiplied the final category ratio of each category with a corresponding correlation value from Palmisano and afterwards divided the sum by the total weight before calculating the logarithm. This did not totally eradicate implicit weights from our index, as the impact of a subcategory on the corresponding category value is still only affected by the operative decisions that we made.

![Fig.1: Index_description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/index-image.jpg)

### 3.3 Limitations

Due to the decision for this specific dataset there can’t be any conclusions made about graduations of higher education. This is the reason why adding an additional column with information about the percentage number of female PhD-Graduates seemed to be an important step towards an answer to our research question. 

Furthermore, all our findings must be interpreted with precaution. The dataset only includes data about European students. As we don’t have any information about people who are not attaining university it is difficult to draw assumptions.  

Seeing that there are for example more Males being dependent on self-earned income could on the one hand mean that they are more sensible to their socio-economic background. But on the other hand, it might also indicate a data gap. In theory, it could mean that the Males are still able to study regardless their socio-economic disadvantages whereas FLINTA*s with the same background stop appearing in our dataset because they are not able to study when facing difficulties. 

Additionally, there are inherent limitations in objectivity in the calculation of the indices. By weighting the different factors, subjective decisions on the way how these are calculated are inevitable. In combination with implicit weighting, this leads to hardly avoidable impact of personal bias to the study.

## 4. Findings

### 4.1 Overall higher attainment of FLINTA\*s at universities

On average, FLINTA* students are more represented at European universities than males, with a distribution of 57,3% and 42,7%.  

Since there are more FLINTA\*s among all students, attaining higher education, the proportion of FLINTA\*s across all the sub-categories is usually higher than males. We can see that in the example of the average of European students with a low educational background, the distribution is 60,1% FLINTA\*s and 39,1% Males, which is similar to the overall dispersion. 

### 4.2 Average attainment across socioeconomic classes

We examine the deviation in attainment across specific socioeconomic characteristics by gender. The diagrams show the European average. The deviation between the classifications in one category were always quite small.

![Fig.2: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Screenshot%202025-03-03%20153947.png)

![Fig.3: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Screenshot%202025-03-03%20153947.png)

![Fig.4: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Screenshot%202025-03-03%20153947.png)

The distribution from “Not at all well-off” to “Very well-off” in the category Parental wealth is very similar between FLINTA\*s and Males. Looking at Financial Difficulties, we can see that among FLINTA\*s the most common reality was to have “Somewhat Financial Difficulties”, as for male students all indicators were quite equally assigned.

![Fig.5: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Screenshot%202025-03-03%20153947.png)

When it comes to “Severity of impairment” 40% of Male students assigned themselves to be “Not limited at all in Studies” and with that it was the most attained factor in that category. For FLINTA*s that was the opposite and “Not limited at all in Studies” was the least attained factor, with “Limited in Studies” being the highest. The difference between the distributions regarding to gender had a difference ratio from 5% to 10%.

![Fig.6: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Screenshot%202025-03-03%20154003.png)

Male students were more dependent on self-earned income, whereas FLINTA*s were more dependent on the family as an income source. 

### 4.3 Relation of gender distribution in higher edutcation to countries GDP

![Fig.7: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Screenshot%202025-03-03%20153947.png)

Since we suspected that the Gross Domestic Product (GDP) might also have an impact on the attainment of FLINTA\*s, for example through higher financial resources to invest in public services coming with a higher GDP, we investigated this using scatter plots and a regression line. The regression line shows an increase of 1% in attainment with the rise of the GDP from 20000$ GDP per capita to 100000$ GDP per capita. Furthermore, we calculated the Pearson correlation coefficient of FLINTA\*s Attainment in higher education in all fields and the GDP. The results are that r = 0.095, which shows a very weak positive connection between the two variables. The significance test gave a t-statistic of 0.46 and a p-value of 0.65, which means the correlation is not statistically important. Because of this, there is no strong linear relationship between the variables and the small correlation could be linked to random chance. 

### 4.4 Analysis of Socio-Economic Variables for FLINTA Students*

The analysis of socio-economic variables for FLINTA\* students is based on a baseline (All students FLINTA\* %) representing the overall distribution of these students in each country. Deviations from this baseline provide a quick measure of whether FLINTA* students are more or less common in a specific socio-economic category than would be expected by chance. A positive deviation indicates overrepresentation, whereas a negative value implies underrepresentation. 

On the **income dependency** front, FLINTA\* students across the 23 countries are generally overrepresented in the **dependent on family category** by an average of approximately +4.9 percentage points. In particular, Finland (+11.87) and Croatia (+10.77) show a strong reliance on family support, while Germany (+7.38), Estonia (+7.28), and Lithuania (+7.04) also exceed the overall trend. In contrast, countries such as France (+0.44) and Spain (+1.53) display only a slight tilt, with Sweden (–0.49) being the only nation with a marginal negative deviation. (see below)

![Fig.8: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Bild2.png)

**When considering dependency on self-earned income**, the average deviation is approximately –2.37 percentage points. This suggests that FLINTA\* students are generally underrepresented in financing themselves through work, although Lithuania (+6.38), Sweden (+3.78), Georgia (+3.39), Latvia (+2.77), and the Netherlands (+1.90) buck the trend. Significant negative deviations are observed in Azerbaijan (–24.75), Portugal (–6.54), Romania (–5.22), as well as Austria (–4.38) and Spain (–3.77). (see below) 

![Fig.9: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Bild3.png)

**For dependency on public student support**, the overall average is slightly negative at –approximately 0.5 percentage points. However, some countries stand out with strong positive values, such as Azerbaijan (+18.03), Georgia (+15.66), Croatia (+11.50) and Lithuania (+9.47), while Estonia (–14.73) and Slovakia (–7.62) report pronounced underrepresentation. Meanwhile, Denmark (+0.76) and Poland (- 0.18) are near the baseline. (see below)

![Fig.10: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Bild4.png)

Turning to **financial difficulties**, the analysis distinguishes among students facing full financial difficulties, those with somewhat financial difficulties, and those not experiencing financial hardships. **FLINTA\* students experiencing financial difficulties** are slightly overrepresented on average by approximately +1.5 percentage points. Malta (+6.88) leads this trend, whereas Germany (–4.83) and Portugal (–3.58) fall significantly below the baseline. (see below)

![Fig.11: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Bild5.png)

**For students with somewhat financial difficulties**, the average deviation is approximately +3.7 percentage points, with Latvia (+8), Netherlands (+ 6.5) and the Czech Republic (+6) showing the strongest overrepresentation. Azerbaijan (–0.04) and Georgia (–0.85) remain nearly balanced. (see below)

![Fig.12: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Bild6.png)

Conversely, among **students without financial difficulties**, there is an average underrepresentation of –3.25 percentage points. Iceland (+0.94) is closest to the baseline, yet Slovakia (–7.81), Romania (–8.14), Malta (-6.74) and Poland (-5,8) stand out as significant negative outliers. (see below) 

![Fig.13: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Bild7.png)

Regarding **parental wealth**, FLINTA\* students from **very well-off families** are moderately underrepresented, with an overall deviation of –5.3 percentage points. Denmark (+4.26) shows the least underrepresentation, while Lithuania (–17.70) and Romania (–16.00) display the most pronounced negative deviations, along with France (–10.74). (see below)

![Fig.14: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Bild8.png)

In the **somewhat well-off category**, the average deviation is approximately –2.4 percentage points. Here, Azerbaijan (+6.22) and Latvia (+3.15) exhibit overrepresentation, whereas Sweden (+0.72), Finland (-0.02) and Denmark (–1.68) remain near the baseline; Lithuania (–7.62), Portugal (-6.2), Spain (-5.5) and Romania (–5.28) are notable negative outliers. (see below)

![Fig.15: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Bild9.png)

When looking at **families of average wealth**, FLINTA\* students are slightly overrepresented by an average of approximately +2.0 percentage points, with Malta (+4.6), Lithuania (+4.24) and Denmark (+4.17) at the forefront, Romania (–0.37) and Azerbaijan (-0.3) hover near the baseline, and Latvia (-2.8) being the only underrepresented country with a moderate significance. (see below)

![Fig.16: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Bild10.png)

In the category of **not very well-off**, there is a slight underrepresentation overall approximately –0.5 percentage points. Yet, Georgia (+5.84) and Netherlands (+4.9) indicate highest overrepresentation, while Austria, Czech Republic Hungary and Iceland very close to the baseline. Malta (–9.69) and Azerbaijan (–6.5) are the most pronounced negative outliers. (see below) 

![Fig.17: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Bild11.png)

For families that are **not at all well-off**, the average deviation is –0.6 percentage point, countries such as Latvia (+8.94) and Denmark (+8.43) show strong overrepresentation. Georgia (+6.61), Netherlands (+7.3) and Croatia (+7.55) also register notable positive values. In contrast, Azerbaijan (-18.9), Lithuania (–12.70) and Finland (–9.78) exhibit the most pronounced underrepresentation. (see below)

![Fig.18: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Bild12.png)

Finally, the analysis of **parental education** considers families with no higher tertiary education versus those with tertiary education. In families **lacking higher tertiary education**, FLINTA\* students are overrepresented by an average of +3.0 percentage points. Countries such as Sweden (+6.9), Poland (+6) and Latvia (+6) are prominent in this regard. On the other hand, Ireland (-0.8) and Azerbaijan (-1.6) are the only underrepresented countries in this category. (see below) 

![Fig.19: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Bild13.png)

By contrast, in **families with tertiary education** the overall trend is a slight underrepresentation, with an average deviation of –2.1 percentage points. Denmark (+1.9) and Malta (+1.60) show the highest overrepresentation. Ireland (+0.01) and Georgia (-0.1) are very near to the baseline, whereas Romania (–7.59), Slovakia (–6.45), Croatia (–5.5) and Poland (–5.6) are significant negative outliers. (see below)

![Fig.20: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Bild14.png)

Overall, these findings offer a comprehensive view of the socio-economic landscape for FLINTA* students across 23 countries, highlighting where they are overrepresented or underrepresented in terms of income dependency, financial difficulties, parental wealth, and education relative to expected baseline levels. 

### Proportion of Women Among Doctoral Graduates 

Women PhD graduation data indicates that in average, across Eurostudent Survey countries, 56.54% of PhD graduates are women. While this percentage surpasses even 60% in Iceland (65.96%) and Estonia (61.62%), countries such as Croatia, Lithuania, Malta, Finland, Latvia, Spain, Denmark and Czech Republic are among the countries that have above average proportion of women among PhD graduates across all countries.  

On the other hand, countries; France, Austria, Ireland and Georgia remain below average, yet still achieve a high percentage, ranging from 53%-56%. There is only one country, Switzerland (46.97%), that has less than 50% women among PhD graduates, with the fallowing countries Germany (50.65%) and Azerbaijan (50.95%) together being the top three countries from the bottom of the list. (see below) 

![Fig.21: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Bild15.png)

In contrast, since Eurostudent Survey does not include all European countries, global data for Women among PhD graduates is worth looking at. Global data is mostly composed of European countries, but it includes some of the North and South American, Asian and African countries as well, allowing for further analysis and comparison. 

According to the global data, highest top countries in the list are being Albania (66.41%), Canada (66.2%) and Montenegro (64.29%), reaching significant proportions above 60% point. EU average being 46.72% which is observed to fall below all Eurostudent Survey countries. By contrast, Japan is the only significant outlier, being the last country in the list with 31.96% which is way below than all countries in the data. Bosnia Herzegovina with 44.19% point is the closest observation to Japan in the list, being at the second position from the bottom.  (see below) 

![Fig.22: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Bild16.png)

### Index Results

![Fig.23: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Screenshot%202025-03-03%20154120.png)

The results of the GEITEA index varied between 102.37 for the Netherlands and 84.88 for Azerbaijan. 8 out of 25 participating countries scored higher than 100, thus indicating an advantage for FLINTA\*s in tertiary education access. The other 17 countries scored lower than 100, indicating an advantage for male people in tertiary education access. The average score is 96.9, the standard deviation is 4.422. If the index is calculated by only considering representation within different groups of parental wealth and educational background, most countries score above 100. The reason why a lot of countries scored below 100 in the final calculation is usually due to a significant overrepresentation of FLINTA\*s in groups with financial difficulties and with impairment within studies.

### Live survey

![Fig.24: description](https://github.com/Nestorbruno01/Gender-Sensitivity-of-Socioeconomic-barriers-for-european-students/blob/main/figures/Screenshot%202025-03-03%20154613.png)

During the gallery walk as a part of the conference week there was a live poll made with everyone being interested in the research question. There were three questions asked with one being the gender of the person.  The possible options were “FLINTA*, Male and Prefer not to assign”. The two following questions were asking for challenging and helping factors in attaining a university degree. The possible answers in both questions were “Financial Situation, Parental Education, School support, Cultural/family expectations, None”.  

It is clear to see, that the financial situation is decisive for one's academic journey. While there are a lot of students feeling limited in their possibilities due to their struggles with financing their studies many other students find their financial situation to be a big advantage. Nevertheless, there are no big differences between the genders except some more FLINTA*s feeling encouraged by parental education.  

## 5. Discussion

### 5.1 Providing equal opportunities

The findings show that a vast majority of Eurostudent countries, in all levels of higher educational degrees including PhD’s, have higher FLINTA\* proportion. Although this may be interpreted as FLINTA\* students have high access to tertiary education regardless of background, further analyses of sub-socio-economic variables reveal that this is not always the case. Our findings illustrate that while a big majority of countries succeed in providing equal opportunities regardless of the socio-economic disadvantages, there are countries such as Azerbaijan whose FLINTA\* students from lower socio-economic background groups are notably underrepresented, indicating a potential lack of access to higher education within specific backgrounds.  

For instance, Azerbaijan is the only country in which FLINTA\* students with no parental tertiary education are underrepresented, whereas FLINTA\* students with parental tertiary education are slightly overrepresented. This may indicate that FLINTA\* students in Azerbaijan who have access to higher education are more likely to come from families   with middle or higher socio-economic classes. Furthermore, in Azerbaijan, FLINTA\* students with somewhat well-off wealthy families are significantly overrepresented with +6.2% (highest in the category). Conversely FLINTA\*s from families with not at all well-off financial situation, in other words FLINTA\* students with poor families, are excessively underrepresented with –18.9% (lowest in the category). Moreover, when “not at all well-off" and “not well-off" categories are combined, indicating all FLINTA\* students from poor or somewhat poor families, FLINTA\* individuals are less likely to access higher education with dramatic underrepresentation of -25.3%.  

Based on the Azerbaijan’s case, we are confident to say that our hypothesis is valid. However, as we mentioned earlier, most countries achieved to reverse this trend. 

### 5.2 Why do fewer males study?

Due to that the question came up how this trend has shifted. The answer is found when looking at the attainment of different genders within secondary education. According to the last Pisa-studies, there are significant differences between the performance of males and females within school. Females in Europe score slightly higher on average over all fields of study and boys are a lot more likely to underachieve. This trend has been analysed in Europe in 2018 and there are only few changes visible to this in 2022. A reason for this may be the cultural image of attainment within studies in Europe being labelled as ‘uncool’, particularly for male people within their teenage years [5,6]. 

### 5.3 Financial Indicators: The Role of financial Dependence

The results of our analysis on income dependency reveal that financial hardship by itself does not directly link to gender disparities in access to higher education. FLINTA\* representation does not appear to change greatly among students who are facing financial difficulties. This indicates that, when only isolating this indicator, financial struggles impact students across Europe in a similar manner.  

This picture changes substantially though, when students are required to rely on self-earned income to finance their education. In this case, FLINTA\* students in majority of countries appear to be underrepresented, most noticeably in southern and eastern European countries with rare exceptions, the most extreme case being Azerbaijan. This shows that lack of financial self-independency creates a barrier, to which FLINTA\*s are more susceptible for.  

Reasons for this can be multifaceted. One being potentially lower wages and job opportunities for FLINTA\* students, which makes self-financing higher education less feasible and/or cultural and societal implications that impact FLINTA\* students differently than male students. This aligns to the “Gender Equality Index” in 2024 [3], where eastern and southern European countries scored significantly lower in categories “Work” and “Care activities”, explaining the added obstacles FLINTA\* students face when attaining education, while being financially independent.  

Similarly in eastern European countries, parental wealth appears to show a gendered effect, as FLINTA\* students appear to be less likely to come from low-income families than male students. This suggests that financial difficulties at the family level in fact do influence FLINTA\* students disproportionally, different to general financial difficulties.  

These findings reinforce prior research, where the educational attainment of marginalized groups is closely linked to the existence of financial support structures [4]. The lack of financial safety nets can disproportionately exclude them from higher education. 

The GDP does not significantly influence the attainment of FLINTA\*s in higher education, showing a weak and statistically insignificant correlation between both variables. 

### 5.5 Overcoming generational education gaps

In contrast to financial indicators, low parental education shows a different trend. Here, FLINTA\* students have appeared to be generally overrepresented among students coming from a low-educational background, especially in northern and western European countries with only rare exceptions, suggesting that FLINTA\* students in these regions are more likely to overcome parental education disadvantages than their male counterparts. 

Again, there may be various possibilities to explain this phenomenon. As an example, one potentially being having strong social policies, supporting students with low-educational background, aiming to create social mobility and justice.  

However, this trend is less visible in southern and eastern Europe, where the overrepresentation of FLINTA\* students in these categories weaker or even appears to be reversed in some cases, suggesting that the role of parental education in accessing higher education vary based on socioeconomical and cultural differences. In regions, where education is seen more as a privilege than a necessity, FLINTA\* students may be facing more structural and cultural barriers than males. What needs to be added here is that the subnational differences within regions are often bigger than the differences between neighbouring countries, for example the differences between rural and urban regions within a country [9].

### 5.6 Gender and severe impairment 

The findings on students with severe impairment reveal an unexpected trend, as FLINTA\* students are overrepresented across Europe in this group. Especially in northern and western European countries, suggesting that having a severe impairment does not create a disproportionate barrier for FLINTA\* students, contradicting our assumption of FLINTA\* students being more likely to be excluded from higher education when living with severe impairment.  It’s more likely the other way around in these regions. This could be attributed to social stigma, which may discourage men from seeking support systems and utilizing available social resources. 

### 6. Conclusion

Overall, the high representation of FLINTA\* students across  Eurostudent countries illustrates that, there is significant achievement towards gender equality in higher education. However, FLINTA\* students in countries such as Azerbaijan and possibly in other parts of the world, remain to experience various social-economic and cultural disadvantages in an uneven way. 

We observe that FLINTA* students are more likely to be underrepresented when required to finance their education independently. Whereas for male students, it is more likely that they enter job market during their studies, providing them financial independency and early career experience. Furthermore, male students are underrepresented in higher education. Possible reasoning for this may be that since males have more job opportunities that have the potential to provide a higher income than a job that requires a university degree, they may be choosing to have a career in those areas rather than pursuing higher education, decreasing value of university degrees can be a supporting argument for this reasoning as well.  

Finally, FLINTA* students from low-educational backgrounds are overrepresented in all countries except Azerbaijan and Ireland. Ireland is fallowing similar educational policies as of UK and USA. They have a fix fee named “Student Contribution”. It is also known as a registration fee, and it covers student services and examinations. The amount of contribution varies from one institution to another. The maximum rate of the student contribution for the academic year 2023-2024 was €3,000. Whereas this figure is mostly around €400 in Germany. In addition, the semester fee in Germany includes public transportation as well. Although, Ireland has a grant system based on social constraints of students, it lacks a comprehensive student financing system like Germany’s Bafög, making access to education limited for those from disadvantaged backgrounds. These factors may be explanatory for the underrepresentation. Therefore, designing comprehensive social policies are crucial to address such challenges.

### 6.2 Implications for Sustainability:

Our research revealed both progress and challenges connected to sustainability. 
The fact that more FLINTA*s are pursuing higher education can be seen as an achievement in terms of access to quality education, which is also a target of the SDG 4. 
 
On the other hand, the research reveals significant sustainability issues tied to obstacles in the job market and the stability of the workforce in higher education.  
As the findings suggest, male students are more likely to find jobs that provide financial independence, while FLINTA* students have more difficulties in financing their education, which leads to an unequal distribution of resources and opportunities and if male students are more likely to enter the workforce early due to better job opportunities outside of university education, it raises concerns about long-term economic and social sustainability which profit from workforce adaptability.

### 6.3 Recommendations

To further promote educational equity in Europe, it will be substantial to implement targeted interventions in support of underprivileged and disadvantaged students as early as possible. This includes the expansion of inclusive education practices, as well as reforms to support both FLINTA* students as well as males, to better support young students when facing gendered challenges or dealing with any sort of impairment. 

To limit the socioeconomic challenges of young students, we need to increase scholarships and financial aid for FLINTA\* students and underrepresented males. This can be highly effective and crucial as support for students coming from low-income families, who can depend on family support. Going further, subsidising equal work opportunities, as well as increasing minimum wages can lift the burden from young students, especially FLINTA\*, who appear to not have the same opportunities to support themselves as male students.  

Combining social policies targeting educational inequalities with increased funding for financial aids as well as scholarships supporting students from lower-income families, educational institutions as well as policymakers can work towards a more equal education system, improve social mobility and close gender gaps. 

### Future Research Directions

For an even more detailed view on the problem there needs to be more focus on regional differences in socio-economic impacts on FLINTA\* students and underrepresented in higher education. As our research has already shown, cultural circumstances seem to be an important factor to look at. Furthermore, it would be interesting to explore how self-financing affects educational access differently for FLINTA\*s and Males. This comes together with other intersectional investigations such as connections between education and disability in the genders. Finally, the impacts of the constantly progressing gender equality policies in Europe need to be evaluated in long-term studies to see how higher education access and attendance improves. 

## 7. References

[1] Munir, J., Faiza, M., Jamal, B., Daud, S., & Iqbal, K. (2023). The Impact of Socio-economic Status on Academic Achievement. Journal of Social Sciences Review, 3(2), 695-705. https://doi.org/10.54183/jssr.v3i2.308 

[2] Paterson, Molly & Parasnis, Jaai & Rendall, Michelle, 2024. "Gender, socioeconomic status, and numeracy test scores," Journal of Economic Behavior & Organization, Elsevier, vol. 227(C). https://doi.org/10.1016/j.jebo.2024.106751. 

[3] Eurostat(educ_uoe_enrt03): Tertiary Education Statistics (Accessed: Dec 27, 2024). https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Tertiary_education_statistics (September 2024) 

[4] United Nations. (2024). Ziele für nachhaltige Entwicklung – Bericht 2024 [PDF]. United Nations Publications. https://www.un.org/Depts/german/millennium/SDG_2024.pdf 

[5] Ramya, Subrahmanian. (2005). Gender equality in education: Definitions and measurements. International Journal of Educational Development. 25. 395-407. 10.1016/j.ijedudev.2005.04.003. 

[6] Eurostudent. (2024). EUROSTUDENT Data Reporting Module (DRM). https://database.eurostudent.eu/drm/ (Accessed: December 02, 2024) 

[7] World Bank. (2024). World Development Indicators. https://databank.worldbank.org/source/world-development-indicators (Accessed: January 06, 2025) 

[8] European Commission: Directorate-General for Research and Innovation. (2021). She figures 2021 : gender in research and innovation : statistics and indicators. Publications Office. https://data.europa.eu/doi/10.2777/06090. 

[9] Bericat, E. The European Gender Equality Index: Conceptual and Analytical Issues. Soc Indic Res 108, 1–28 (2012). https://doi.org/10.1007/s11205-011-9872-z 

[10] European Institute for Gender Equality (2024). Gender Equality Index 2024: Sustaining momentum on a fragile path. Publications Office of the EU. ISBN: 978-92-94-86258-7. DOI: 10.2839/9523460 

[11] Palmisano, F., Biagi, F. & Peragine, V. Inequality of Opportunity in Tertiary Education: Evidence from Europe. Res High Educ 63, 514–565 (2022). https://doi.org/10.1007/s11162-021-09658-4 

[12] Directorate-General for Education, Youth, Sport and Culture, PISA 2018 and the EU: Striving for social fairness through education. Publications Office of the EU. ISBN: 978-92-76-10360-8, DOI: 10.2766/964797 

[13] OECD (2023), PISA 2022 Results (Volume I): The State of Learning and Equity in Education, PISA, OECD Publishing, Paris, https://doi.org/10.1787/53f23881-en. 

[14] Cascella, C., Pampaka, M., & Williams, J. (2024). Gender Attitudes Within and Between European Countries: Regional Variations Matter. SAGE Open, 14(3). https://doi.org/10.1177/21582440241259912 (Original work published 2024)
