# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 17:35:26 2018

@author: madona syombua

The data is checking , Age, Number of Complaints, Monthly Payment in Ksh
Number of contacts the user has, and Swap Agent.

I try to name the variable well for easier reading.
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


'''
Just simple test, not perfect but learning.
'''
df.describe()

df.info()

 

df['Swap Agent'].value_counts()
tmp = df.drop('Id', axis=1)
g = sns.pairplot(tmp, hue='Swap Agent', markers='+')
plt.show()

print("Predicition trial\n")

X = df.iloc[:,:-1]

y = df.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

lr = LogisticRegression()

lr.fit(X_train, y_train)

y_predict = lr.predict(X_test)
y_predict.reshape(-1,1)

'''
Using the dummy data the percentage is 62.5

'''
print(y_predict)
print(y_test)

accuracy =  metrics.accuracy_score(y_test, y_predict)
precision =  metrics.precision_score(y_test, y_predict)
recall =  metrics.recall_score(y_test, y_predict)
f1ratio =  metrics.f1_score(y_test, y_predict)

print(accuracy)

print(precision)

print(recall)
print(f1ratio)


y_score_lr = lr.fit(X_train, y_train).decision_function(X_test)
fpr_lr, tpr_lr, _ = metrics.roc_curve(y_test, y_score_lr)
roc_auc_lr = metrics.auc(fpr_lr, tpr_lr)

print("Testing accuracy\n\n")

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
The data Used, this is fake generated data just for learning
I tried topredict swap 
Id	Age 	No. of Complaints	 MP in Ksh	Contacts	Swap Agent
1	30	   0	                   1200	       20	         0
2	18  	2	                     60	       10       	1
3	60	   1	                    180	       44	         0
4	25	   2	                    200	       30       	0
5	30	   2	                    300	       10	          1
6	45	   1	                    900	       55       	0
7	50	   3	                    120	       20       	0
8	78	   1	                    60	       10       	1
9	26    	1	                   180	       44        	0
10	23	   2	                   200	       30        	0
11	33	   2	                   300          10        	1
12	45   	1	                   1200	       55       	0
13	30   	2	                    800    	    100	      0
14	33	   6	                    60	        90	      1
15	26	   1	                   180	        44	      0
16	23	   2	                  2000	        30        	0
17	33	   2	                  3000	       10       	1
18	45	   1	                 1200	          55        	0
19	66    	1	                   50       	100       	0
20	78	   1	                   60	           10	       1
21	26	   1	                   180	        44	       0
22	23    	2	                  2000	        30         0
23	33	   2	                   300	        10	        1
24	45	   1	                  1200	        55	        0
25	66	   1	                    50	        100         	0
26	78	   1	                     60	       10          	1
27	26	   1	                   180	       44           	0
28	23  	2	                   200	        30	          0
29	33  	2	                  3000	        10	           1
30	45	   1	                  1200	         50	            1
'''








