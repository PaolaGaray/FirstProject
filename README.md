**Project Title: Reducing Gender Inequality to Support GDP Growth**
    by Lucie Stenger, Paola Angela, Nicole Pinto, Garima Sharma

# Project overview

This project explores the impact of reducing gender inequality in the workforce on GDP growth across various countries. By analysing key indicators related to gender inequality, labour force participation, and economic performance, we aim to establish a correlation between gender equality and GDP growth. The hypothesis is that increasing women's participation in the paid workforce, promoting equal pay, and enhancing gender diversity in leadership will lead to significant economic benefits.

# Questions / Hypotheses

1) Unpaid Domestic Work and Labor Force Participation:
Hypothesis: If the proportion of time women spend on unpaid domestic and care work is replaced by time spent in paid employment, GDP will increase.
Data Required:
Labor force participation rates by gender.
Time spent by women on unpaid domestic and care work.
GDP growth rates, sectoral contributions to GDP, and employment rates.

2) Equal Pay for Equal Work:
Hypothesis: If policies that promote equal pay for equal work are implemented and enforced, the pay disparity between men and women will decrease, resulting in increased household income and GDP growth.
Data Required:
Pay disparity data.
Household income levels.
Consumption patterns and GDP growth rates.

3) Human Development Index (HDI) and Gender Equality:
Hypothesis: If gender equality improves, as reflected in higher female labor force participation, better pay equity, and increased educational opportunities, then the Human Development Index (HDI) will improve, leading to sustained economic growth.
Data Required:
HDI scores and components (e.g., life expectancy, education level, income per capita).
Gender-specific data on education, health, and income.
Correlation between HDI improvements and GDP growth in countries with varying levels of gender equality.


# Dataset 

**Country Selection**
The analysis will focus on the following countries, selected from different regions:
1) Europe: Norway, Greece, France, Germany
2) Americas: United States, Brazil, Colombia
3) Asia-Pacific: Japan, New Zealand, Pakistan
4) Africa: Ghana, Cameroon

**Data Sources:**

1) World Policy Analysis Centre: Gender Equality in the Economy data (downloadable datasets).
2) Kaggle: Labor Force Participation Rate dataset.
3) World Bank: Gender Equality datasets and economic performance indicators.
4) OECD: Gender Wage pay gap dataset.


## Main dataset issues

1) Raw datafile had metadata/explanations in the first 5 rows, which made the file irregular and caused an error (An error occurred: Error tokenizing data. C error: Expected 3 fields in line 5, saw 69) during the import.
2) Pandas couldn't read the excel format, so we had to download openpyxl library.
3) Inconsistency in the names of data frames and other variables in our different notebook’s branches so when we merged files, we had to redefine them.
4) GitHub technical challenges with the merges, especially when a collaborator imported an additional library for the purpose of their specific analysis.



## Solutions for the dataset issues
1) Delete those first top rows
2) Downloaded the openpyxl library on our indivdual branches
3) Discussed, formed a concesus on the terminoloy and then renamed. For the future: better to align before starting with data cleaning
4) Ongoing challenge. Need support from teaching staff to resolve.

# Conclussions
The analysis reveals a significant challenge in understanding the relationship between gender equality and economic growth: certain countries achieve high GDP levels despite low female labor force participation. This divergence highlights the complexity of linking gender equality directly to economic performance, especially in economies where growth is driven by sectors with traditionally low female employment or shaped by strong cultural norms. To address this, it's essential to examine sectoral contributions to GDP, explore relevant case studies, and consider the long-term benefits of increased female participation in the workforce.

# Next steps
1) Expand Data Collection
2) Develop Predictive Models
3) Policy Impact Assessment


