# Data_Analysis_TotalFertilityRate
 
This is a data analysis of South Korea's Total Fertility Rate (TFR) done using Jupyter Notebook.

By importing python libraries, I have done:
1. Visualized related datasets 
2. Found correlation between variables
3. Predicted future TFR using different statistical techniques

After performing multiple statistical analysis on several relevent factors, correlation has been found which may result into the solution on decreasing TFR and aging society in South Korea.  

## 1. South Korea's Population Pyramid

### 2008 Population Pyramid vs 2024 Population Pyramid
<img src="https://github.com/Yunhu-So/Data_Analysis_TFR_2024/blob/main/Graphs/Population%20Pyramid%20in%202008.png" width="500"> <img src="https://github.com/Yunhu-So/Data_Analysis_TFR_2024/blob/main/Graphs/Population%20Pyramid%20in%202024.png" width="500">

I have noticed that the number of youth population had decreased while the numbers of the working-age population and elderly population had increased over 2 decades.
This indicates that the pace of population aging is fast, and it presents the possibility of an aging society. 

To further investigate on this phenomenon, I took a look into the number of birth and total fertility rate.

## 2. South Korea's Number of Birth and Total Fertility Rate (TFR)
<img src="https://github.com/Yunhu-So/Data_Analysis_TFR_2024/blob/main/Graphs/Number%20of%20Birth%20and%20TFR%20graph.png" width="800">

The graph illustrates South Korea's number of birth and TFR over 50 years.
A negative trend is found as Both the number of birth and total fertility rate have gradually decreased.
Such continuity of negative trend may become a serious issue, so I have tried predicting future values by creating regression models.

## 3. Linear Regression Analysis vs Polynomial Regression Analysis

<img src="https://github.com/Yunhu-So/Data_Analysis_TFR_2024/blob/main/Graphs/Linear%20Regression%20Analysis.png" width="800">
I have predicted future number of birth and TFR for next 10 years based on the given dataset.
As expected, the linear regression analysis showed a gradual negative trend over next 10 years.

<img src="https://github.com/Yunhu-So/Data_Analysis_TFR_2024/blob/main/Graphs/Polynomial%20Regression%20Analysis.png" width="800">
To further investigate using alternative models, I have used polynomial regression analysis since our given data spans several decades and has some non-linear trends in some period of time.
By adjusting the polynomial degree into 3, the trend aligned more with the linear regression model (negative trend)

<img src="https://github.com/Yunhu-So/Data_Analysis_TFR_2024/blob/main/Graphs/Polynomial%20Regression%20Fit%20for%20TFR.png" width="800">
To check the polynomial regression fit for TFR, I have created chart for it as well.

I have considered different possible factors that might have affected in such results.

## 4. Crude Marriage Rate
<img src="https://github.com/Yunhu-So/Data_Analysis_TFR_2024/blob/main/Graphs/Crude%20Marriage%20Rate%20Graph.png" width="800">

By looking at the graph, I noticed that people tend to not get married as time passes by. Even though they do get married, married couples decide not to bear children as shown in TFR illustartion. I was curious what might have affected such results.

## 5. Private Education Expense
<img src="https://github.com/Yunhu-So/Data_Analysis_TFR_2024/blob/main/Graphs/Private%20Education%20Expense.png" width="800">

Private education expense has been in positive trend except for 2020. I assume this happened due to the break out of Covid-19, which has created social distancing and preventive measures. Yet, the rate has reached its peak in 2021 when the government implemented 'living with Covid-19' plan.
Meanwhile, I was curious if this was the only factor that burden couples to bear no children in their marriage.

## 6. Consumer Price Index
<img src="https://github.com/Yunhu-So/Data_Analysis_TFR_2024/blob/main/Graphs/Consumer%20Price%20Index%20Graph.png" width="800">

As obsereved in the graph, prices constantly increases. By considering correlation between Per Capita Income and inflation, individuals struggle in living their own lives, which make them not to have children.

## Regression Analysis between Crude Marriage Rate and TFR
<img src="https://github.com/Yunhu-So/Data_Analysis_TFR_2024/blob/main/Graphs/Linear%20Regression%20CMR%20vs%20TFR.png" width="500"> <img src="https://github.com/Yunhu-So/Data_Analysis_TFR_2024/blob/main/Graphs/Polynomial%20Regression%20CMR%20vs%20TFR.png" width="500">

Based on the regression analysis on Crude Marriage Rate and TFR, it is clear that as crude marriage rates increases, so does TFR. Correlation is found in such factors.

## Conclusion
One possible reason could be the increase in life expectancy caused by technological improvements. However, we can see from our analysis that other factors do exist. To solve decreasing trend in TFR, we should take a look into crude marriage rate, to check whether people are getting married. We have found out its rate is decreasing. 

South Korea must focus on different policies to encourage people to get married as we can we from section 5 & 6 that living in South Korea is getting more harsh as time passes. By not only discussing negative trend in TFR, but also by taking a look at the overall living situation in South Korea, we may solve the serious issue that is happening in our country.
