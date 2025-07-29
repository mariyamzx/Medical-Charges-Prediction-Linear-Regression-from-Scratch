import numpy as np
class LinearRegression:
    def __init__(self):
        self.coef_=None
        self.intercept_=None
        
    def fit(self, X_train, y_train):
        X_train=np.insert(X_train, 0,1, axis=1)
        beta_vals=np.linalg.inv(np.dot(X_train.T, X_train)).dot(X_train.T).dot(y_train)
        self.coef_=beta_vals[1:]
        self.intercept_=beta_vals[0]
        
    def predict(self, X_test):
        return self.intercept_ + np.dot(X_test,self.coef_ )