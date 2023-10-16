import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np
from scipy import stats
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor
df = pd.read_csv('value.csv')
y = df['gross_profit']
xvar = ['fixed_fa', 'fin_debt', 'CCC', 'ln_sales', 'd1', 'd2']
x = df[xvar]
scaler = StandardScaler()
x = x.assign(CCC=scaler.fit_transform(x[['CCC']]))
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)
lr = LinearRegression()
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
coefficients = lr.coef_
intercept = lr.intercept_
print("Coefficients:")
for var, coef in zip(xvar, coefficients):
    print(f"{var}: {coef:.4f}")
print(f"Intercept: {intercept:.4f}")

coefficients = lr.coef_
intercept = lr.intercept_

formula = f"Gross Profit = {intercept:.{6}f} "
for var, coef in zip(xvar, coefficients):
    formula += f"+ {coef:.{6}f} * {var} "
print("Regression Formula:")
print(formula)

# R-squared score
r2 = r2_score(y_test, y_pred)
print(f"R-squared (R2) Score: {r2:.4f}")

vif_data = pd.DataFrame()
vif_data["Variable"] = xvar
vif_data["VIF"] = [variance_inflation_factor(x.values, i) for i in range(x.shape[1])]
print("Variance Inflation Factor (VIF):")
print(vif_data)

