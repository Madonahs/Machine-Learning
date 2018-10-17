# -*- coding: utf-8 -*-
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
Created on Thu Aug  9 17:35:26 2018

@author: madona syombua

Simply a play ground and just for practice, I am new to Machine Learning
and trying to learn new things. 
"""

import pandas as pd
import seaborn as sns
sns.set_palette('husl')
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import metrics


df = pd.read_csv("customer_data.csv")

print(df)

################################################################################
################################ df describe ###################################
################################################################################

df.describe()

df.info()

 

df['Swap Agent'].value_counts()
tmp = df.drop('Id', axis=1)
g = sns.pairplot(tmp, hue='Swap Agent', markers='+')
plt.show()

print("Predicition trial\n")

X = df.iloc[:,:-1]

y = df.iloc[:,-1]


################################################################################
################################ training the dataset ##########################
################################################################################
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

#the model is LogisticRegression 
lr = LogisticRegression()

lr.fit(X_train, y_train)

y_predict = lr.predict(X_test)
y_predict.reshape(-1,1)


#Using the dummy data the percentage is 62.5

print(y_predict)
print(y_test)

accuracy =  metrics.accuracy_score(y_test, y_predict)
precision =  metrics.precision_score(y_test, y_predict)
recall =  metrics.recall_score(y_test, y_predict)
f1ratio =  metrics.f1_score(y_test, y_predict)

#check accuracy
print(accuracy)

#check precision 
print(precision)

print(recall)
print(f1ratio)


y_score_lr = lr.fit(X_train, y_train).decision_function(X_test)
fpr_lr, tpr_lr, _ = metrics.roc_curve(y_test, y_score_lr)
roc_auc_lr = metrics.auc(fpr_lr, tpr_lr)

print("Testing accuracy\n\n")
'''
plt.figure()
plt.xlim([-0.01, 1.00])
plt.ylim([-0.01, 1.01])
plt.plot(fpr_lr, tpr_lr, lw=3, label='LogRegr ROC curve (area = {:0.2f})'.format(roc_auc_lr))
plt.xlabel('False Positive Rate', fontsize=16)
plt.ylabel('True Positive Rate', fontsize=16)
plt.title('ROC curve (1-of-10 digits classifier)', fontsize=16)
plt.legend(loc='lower right', fontsize=13)
plt.plot([0, 1], [0, 1], color='navy', lw=3, linestyle='--')
plt.axes().set_aspect('equal')
plt.show()
'''











