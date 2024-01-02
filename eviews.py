import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor

df = pd.read_csv('value.csv')
y = df['gross_profit']
xvar = ['fixed_fa', 'fin_debt', 'CCC', 'ln_sales', 'd1', 'd2']
x = df[xvar]

x = sm.add_constant(x)
#standardize ccc
scaler = StandardScaler()
x['CCC'] = scaler.fit_transform(x[['CCC']])

model = sm.OLS(y, x).fit()

print("OLS Regression Results:")
print(model.summary())

vif_data = pd.DataFrame()
vif_data["Variable"] = xvar
vif_data["VIF"] = [variance_inflation_factor(x.values, i) for i in range(1, x.shape[1])]

print("\nVariance Inflation Factor (VIF):")
print(vif_data)

#components of CCC
#number of days inventory
x1 = df[['fixed_fa', 'fin_debt', 'n. days inventory', 'ln_sales', 'd1', 'd2']]
x1 = sm.add_constant(x1)
x1['n. days inventory'] = scaler.fit_transform(x1[['n. days inventory']])
model1 = sm.OLS(y, x1).fit()
#number of days account receivable
x2 = df[['fixed_fa', 'fin_debt', 'n. days a/r', 'ln_sales', 'd1', 'd2']]
x2 = sm.add_constant(x2)
x2['n. days a/r'] = scaler.fit_transform(x2[['n. days a/r']])
model2 = sm.OLS(y, x2).fit()
#number of days account payable
x3 = df[['fixed_fa', 'fin_debt', 'n. days a/p', 'ln_sales', 'd1', 'd2']]
x3 = sm.add_constant(x3)
x3['n. days a/p'] = scaler.fit_transform(x3[['n. days a/p']])
model3 = sm.OLS(y, x3).fit()

print("Inventory Days - OLS Regression Results:")
print(model1.summary())

print("\nAccount Receivable Days - OLS Regression Results:")
print(model2.summary())

print("\nAccount Payable Days - OLS Regression Results:")
print(model3.summary())

def calculate_vif(dataframe):
    vif_data = pd.DataFrame()
    vif_data["Variable"] = dataframe.columns[1:]
    vif_data["VIF"] = [variance_inflation_factor(dataframe.values, i) for i in range(1, dataframe.shape[1])]
    return vif_data

vif_data1 = calculate_vif(x1)
print("\nVIF for Inventory Days Model:")
print(vif_data1)

vif_data2 = calculate_vif(x2)
print("\nVIF for Account Receivable Days Model:")
print(vif_data2)

vif_data3 = calculate_vif(x3)
print("\nVIF for Account Payable Days Model:")
print(vif_data3)
