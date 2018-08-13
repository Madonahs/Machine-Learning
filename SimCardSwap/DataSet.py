"""
Created on Sat Aug  4 22:32:36 2018

@author: madona syombua
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split

df = pd.read_csv("customer_data.csv")
print(df)

 
X = df.iloc[:,3:-1]

y = df.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

lr = LogisticRegression()

lr.fit(X_train, y_train)

prediction_values = lr.predict(X_test)

print(prediction_values)