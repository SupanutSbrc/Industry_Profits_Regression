An analysis employs a linear regression model to examine the importance of effectively managing the cash conversion cycle and its components to create profits for companies along with sales, fixed financial asset ratio, and financial debt ratio.

Data Collection:

The data collected were picked from listed firms in the stock exchange market of Thailand (SET). The sample data consisted of 15 companies from 2011-2014. These stocks are divided into three sectors: resource, agro (agriculture and food), and industrial, each comprising 5 stocks. Financial statements were obtained from annual reports from each company's site. The analysis used stacked data for the period 2011-2014 which resulted in 60 total observation


Variables:

Gross Operating Profit, the dependent variable used to describe profitability

  Gross Operating Profit = (Sales – COGS14) / (Total Assets – Financial Assets)

CCC is a metric that expresses the length of time, in days, that it takes for a company to convert resources into cash flows. 

  Cash Conversion Cycle = No. of Days A/R + No. of Days Inventory – No. of Days A/P

The ln sales value is used for estimating the size of a company. 

  ln sale = natural logarithm of sales

The Fixed Financial Assets Ratio is used to calculate shares and participation in other businesses. 

  Fixed Financial Assets Ratio = Fixed Financial Assets / Total Assets

The Financial Debt Ratio is used to determine the relationship between the company's participation with other firms and its profitability.

  Financial Debt Ratio = (Short Term Loans + Long Term Loans) / Total Assets

Inventory Days is the average number of days it takes a company to turn its inventory into sales

  No. of Days Inventory = Inventory / Cost of Goods Sold*365

Account Receivable Days is the average number of days it takes for a company to collect payments from its customers after a sale has been made

  No. of Days A/R = Accounts Receivables / Sales*365

Account Payable Days is the average number of days that a company takes to pay its bills and invoices

  No. of Days A/P = Accounts Payables / Cost of Goods Sold*365

The independent variables are fixed financial assets, natural logarithm of sales, financial debt ratio, and standardization of the cash conversion cycle. Industry dummy variables were also included. The number of industries was 3, resulting in 2 industry dummy variables. The total number of observations is 60, representing stacked data for the period 2011-2014 for listed firms in the stock exchange market of Thailand. Following the regression gross profit is regressed against the stated variables including dummy variables.

Ordinary least squares (OLS)

OLS is one of the most widely used techniques. It is a statistical method that is used to estimate the parameters of a linear regression model, where the linearity condition applies to the parameters, not the variables.

The main idea behind OLS is to find the line that best fits the data. Particularly, to find a line that minimizes the residuals (i.e., estimated errors). This is done by minimizing the sum of the squared differences between the predicted values and the actual values of the dependent variable.

Variance Inflation Factor (VIF)

All four models underwent a test for multicollinearity, which involves using the variance inflation factor (VIF) to assess the relationships between predictor variables in regression models. A VIF value greater than 5-10 suggests high multicollinearity, indicating a strong linear association between predictor variables. In our analysis, all coefficients in all four models exhibited VIF values within an acceptable range.

![image](https://github.com/SupanutSbrc/Industry_Profits_Regression/assets/147172225/8f4a1c71-1893-46e8-a387-d1974cf1ec19)

![image](https://github.com/SupanutSbrc/Industry_Profits_Regression/assets/147172225/030ce1f0-8b4f-4c49-9068-a4c25588cc92)



Regression: Cash Conversion Cycle (CCC)

![image](https://github.com/SupanutSbrc/Industry_Profits_Regression/assets/147172225/a48ac122-6ee5-4163-8173-ae66d3215100)


The regression equation shows that there is a negative relationship between the cash conversion cycle and profitability, which is consistent with the general statement that a lower cash conversion cycle will generate more profits. Moreover, the fixed financial asset ratio also shows a positive correlation with gross operating profits. There was also a negative relationship between the natural logarithm of sales and gross profit and a positive relationship between the financial debt ratio and gross profit.

Regression: CCC components

![image](https://github.com/SupanutSbrc/Industry_Profits_Regression/assets/147172225/ed2b949d-77fe-4bf2-a0b7-64e9a6dfe083)

![image](https://github.com/SupanutSbrc/Industry_Profits_Regression/assets/147172225/c187d745-b100-46d0-a2da-7bf00f9c1218)

![image](https://github.com/SupanutSbrc/Industry_Profits_Regression/assets/147172225/06f49fb1-d95b-4082-aed6-3672a1494d4c)


The results show that all 3 of the components of the cash conversion cycle including inventory days, account receivable days, and account payable days have a negative relationship with the profit of a company.
