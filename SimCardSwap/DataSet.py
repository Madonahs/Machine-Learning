# Copyright (C) 2018 Madonah Syombua
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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