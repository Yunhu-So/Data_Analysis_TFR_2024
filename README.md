# Data Analysis of South Korea's Total Fertility Rate (TFR)

This project analyzes South Korea’s Total Fertility Rate (TFR), demographic structure, and socio-economic factors using Jupyter Notebooks. The analysis includes visualization, correlation study, and regression-based prediction of future TFR trends.

## Objectives
- Visualize demographic changes and fertility-related datasets
- Identify correlations between TFR and relevant social/economic factors
- Predict future TFR using linear and polynomial regression

## 1. South Korea's Population Pyramid
### 2008 vs. 2024 Comparison

<img src="Graphs/Population%20Pyramid%20in%202008.png" width="500"> <img src="Graphs/Population%20Pyramid%20in%202024.png" width="500">

Youth population has decreased, while working-age and elderly groups have increased. This indicates rapid population aging.

## 2. Number of Births and TFR

<img src="Graphs/Number%20of%20Birth%20and%20TFR%20graph.png" width="800">

Both the number of births and TFR have steadily decreased for decades. This persistent negative trend motivated regression-based forecasting.

## 3. Regression Analyses
### Linear Regression

<img src="Graphs/Linear%20Regression%20Analysis.png" width="800">

Projects a continued decline in births and TFR over the next 10 years using OLS.

### Polynomial Regression

<img src="Graphs/Polynomial%20Regression%20Analysis.png" width="800">

A 3rd-degree polynomial captures mild curvature yet preserves the overall downward trend.

### Polynomial Regression Fit for TFR

<img src="Graphs/Polynomial%20Regression%20Fit%20for%20TFR.png" width="800">

Polynomial fit confirms the decreasing trajectory.

## 4. Crude Marriage Rate (CMR)

<img src="Graphs/Crude%20Marriage%20Rate%20Graph.png" width="800">

Marriage rates have declined over time, and even among married couples, fewer children are being born.

## 5. Private Education Expenditure

<img src="Graphs/Private%20Education%20Expense.png" width="800">

Private education spending increased steadily, with a dip in 2020 due to COVID-19. Rising costs may discourage families from having children.

## 6. Consumer Price Index (CPI)

<img src="Graphs/Consumer%20Price%20Index%20Graph.png" width="800">

Prices have risen continuously. Combined with stagnant income growth, this may create economic burdens that suppress fertility.

## 7. Regression: CMR vs. TFR

<img src="Graphs/Linear%20Regression%20CMR%20vs%20TFR.png" width="500"> <img src="Graphs/Polynomial%20Regression%20CMR%20vs%20TFR.png" width="500">

Result: Crude marriage rate exhibits a positive association with TFR in this sample (correlation, not causation).

## Conclusion

- South Korea’s TFR shows a persistent long-term decline (1973–2023 in the compiled series).
- Correlations suggest that declining marriage rates, rising living costs, and private education burdens contribute to the trend.
- Policy implications: In addition to financial support, encouraging marriage and reducing child-rearing costs may be critical to addressing the fertility decline.

## Repository Structure
- `Code/` — Jupyter notebooks for each analysis module  
- `Graphs/` — Exported figures (PNG)  
- `Reference/` — Input datasets (Excel)  
- `requirements.txt` — Python dependencies

## Environment & Reproducibility
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook Code/
```

## Data Sources & Coverage
- `Total Population in 2008/2024 All Age Range.xlsx`: age-by-sex population (baseline vs. recent)
- `TFR.xlsx`: annual total fertility rate (≈1973–2023)
- `stat_106001.xls`, `stat_423001.xls`, `stat_424401.xls`: crude marriage rate, CPI and related aggregates

Data are annual national aggregates compiled from Korean statistical releases; see each notebook for `usecols` and cleaning steps.

## Recommended Notebook Order
1) `population_pyramid.ipynb`
2) `number_of_birth_vs_TFR.ipynb`
3) `linear_regression.ipynb`
4) `polynomial_regression.ipynb`
5) `crude_marriage_rate.ipynb`
6) `crude_marriage_rate_vs_TFR.ipynb`
7) `private_education_expense.ipynb`
8) `consumer_price_index.ipynb`


## Limitations
- Reported relationships are correlational; they do not establish causation.
- Linear/polynomial models are baseline, illustrative projections with non-trivial uncertainty.
- National aggregates may mask regional heterogeneity and cohort effects.
