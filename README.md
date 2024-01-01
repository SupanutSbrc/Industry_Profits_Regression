An analysis employs a linear regression model to examine the impact of variables, including fixed assets ratio, financial debt ratio, cash conversion cycle, sales, and industry on the gross profit of companies.

Data Collection:

The data collected were randomly picked from listed firms in the stock exchange market of Thailand (SET). The sample data consisted of 15 companies from 2011-2014. Financial statements were obtained from annual reports from each company's site. The analysis used stacked data for the period 2011-2014 which resulted in 60 total observation


Variables:

Logarithm of Sales

Fixed Financial Asset Ratio

Financial Debt Ratio

Standardization of Cash Conversion Cycle

Dependent Variable:

Gross Operating Profit


Regression Analysis:

The independent variables are fixed financial assets, natural logarithm of sales, financial debt ratio, and standardization of the cash conversion cycle. Industry dummy variables were also included. The number of industries was 3, resulting in 2 industry dummy variables. The total number of observations is 60, representing stacked data for the period 2011-2014 for listed firms in the stock exchange market of Thailand. Following the regression gross profit is regressed against the stated variables including dummy variables. 

                            OLS Regression Results
==============================================================================
Dep. Variable:           gross_profit   R-squared:                       0.808
Model:                            OLS   Adj. R-squared:                  0.786
Method:                 Least Squares   F-statistic:                     37.22
Date:                Mon, 01 Jan 2024   Prob (F-statistic):           2.57e-17
Time:                        16:22:54   Log-Likelihood:                 21.272
No. Observations:                  60   AIC:                            -28.54
Df Residuals:                      53   BIC:                            -13.88
Df Model:                           6
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.3668      0.304      1.206      0.233      -0.243       0.977
fixed_fa       0.2530      0.030      8.520      0.000       0.193       0.313
fin_debt       0.3970      0.126      3.151      0.003       0.144       0.650
CCC           -0.0431      0.035     -1.227      0.225      -0.114       0.027
ln_sales      -0.0177      0.012     -1.467      0.148      -0.042       0.007
d1            -0.0388      0.063     -0.619      0.539      -0.165       0.087
d2             0.0879      0.059      1.481      0.145      -0.031       0.207
==============================================================================
Omnibus:                       22.019   Durbin-Watson:                   1.993
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              101.702
Skew:                          -0.698   Prob(JB):                     8.23e-23
Kurtosis:                       9.223   Cond. No.                         315.
==============================================================================


The regression equation shows that there is a negative relationship between the cash conversion cycle and profitability, which is consistent with the general statement that a lower cash conversion cycle will generate more profits. Moreover, the fixed financial asset ratio also shows a positive correlation with gross operating profits. Two results stand out as unexpected in this analysis. The negative relationship between the natural logarithm of sales and gross profit and the positive relationship between financial debt ratio and gross profit.


Multicollinearity Analysis:

The regression model was tested for multicollinearity. The result is as follows:

Variance Inflation Factor (VIF):
   Variable       VIF
0  fixed_fa  2.406750
1  fin_debt  1.356490
2       CCC  2.272408
3  ln_sales  1.462590
4        d1  1.608481
5        d2  1.441563

Variance Inflation Factor (VIF) is used to detect whether one predictor has a strong linear association with the remaining predictors. As seen above, all variables have a variance inflation factor between 2 to 5, indicating that there are moderate correlations between variables, but still acceptable. 
