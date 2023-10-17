An analysis employs a linear regression model to examine the impact of variables, including fixed assets ratio, financial debt ratio, cash conversion cycle, sales, and industry on the gross profit of companies.

Data Collection:

The data collected were randomly picked from listed firms in the stock exchange market of Thailand (SET). The sample data consisted of 15 companies in the period of 2011-2014. Financial statements were obtained from annual reports from each company's site. The analysis used stacked data for the period 2011-2014 which resulted in 60 total observation


Variables:

Logarithm of Sales

Fixed Financial Asset Ratio

Financial Debt Ratio

Standardization of Cash Conversion Cycle

Dependent Variable:

Gross Operating Profit


Regression Analysis:

As the independent variables are fixed financial assets, natural logarithm of sales, financial debt ratio, and standardization of cash conversion cycle. Industry dummy variables were also included. The number of industries was 3, resulting in 2 industry dummy variables. The total number of observations is 60, representing stacked data for the period 2011-2014 for listed firms in the stock exchange market of Thailand. Following the regression where gross profit is regressed against the stated variables including dummy variables. 

Gross Profit = 0.396012 + 0.254062 * fixed_fa + 0.395955 * fin_debt - 0.048680 * CCC - 0.018963 * ln_sales - 0.040748 * d1 + 0.088178 * d2

The regression equation shows that there is a negative relationship between cash conversion cycle and profitability, which is consistent with the general statement that a lower cash conversion cycle will generate more profits. Moreover, fixed financial asset ratio also shows a positive correlation with gross operating profits. 

However, two results stand out as unexpected in this analysis. The negative relationship between the natural logarithm of sales and gross profit and the positive relationship between financial debt ratio and gross profit. Such unexpected results required deeper research to find specific conditions that are contributing to such correlations.


Multicollinearity Analysis:

The regression model was tested for multicollinearity. The result is as follows:

   Variable       VIF
   
fixed_fa  3.985362

fin_debt  3.054183

CCC  2.272340

ln_sales  4.527277

d1  2.368098

d2  2.150644

Variance Inflation Factor (VIF) is used to detect whether one predictor has a strong linear association with the remaining predictors. As seen above, all had a variance inflation factor below 5, indicates that multicollinearity is not a significant issue in this model.
