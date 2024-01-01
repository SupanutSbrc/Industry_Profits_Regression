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