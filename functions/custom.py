import statsmodels.api as sm
from statsmodels import regression

def linreg(x, y):
    x = sm.add_constant(x)
    model = regression.linear_model.OLS(y, x).fit()
    x = x[:, 1]

    return model.params[0], model.params[1]