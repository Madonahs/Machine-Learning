<h1 align="center">Machine Learning </h1>

</p>

**This repository was created for educational purposes. It will host a number of projects as part of the process and some exercises that we created.**


## Intro

### Project A

With an upsurge in cybercrimes related to Sim Card Swap fraud in developing countries, making fraud detection is a top priority. If we are able to estimate whether someone is going to commit Sim Card Fraud we can surely try to prevent it earlier. 

## Intro

Predicting the likelihood of Sim Card Swap Fraud Occurrence.
* **Train and test the data samples**
* **Normalize and summarize the data**

### Mode
Develop

### Implementations

* **Define Problem**
* **Prepare Data**
* **Evaluate Algorithms**
* **Improve Results**
* **Present Results**

### Usage

Sim Card Swap Fraud Detection.

### Model Used

* **Logistic Regression.** Logistic regression is the appropriate regression analysis to conduct when the dependent variable is dichotomous (binary). Like all regression analyses, the logistic regression is a predictive analysis.


## Data

### Sample Dataset

There can be many factors as to why someone would want to swap his/her sim card, I will just use few. The swap will be represented by 
```1``` and 
```0``` will represent not swapped. I created this data for this exercise.

Sample Output Representation: 

Swap | Not Swapped|
|------ |------:|
|1 | 0|

* **Sample Fake Data taken from Nairobi**
Data is not given in this case so I decided to create my own, I will identify Locations here and not use the Location since we can have many customers living in the same Location.  

ID| Location                  | Age           | Subscriber Complaints   | Monthly Payments KSH |  Contacts |Swap Agent |
| ------------- | -------------         |:--------------------: | ----------------: | ---------------:| ---------------:| ---------------:|
|1|Nairobi             |30                     | 3            |1200               |20| 0|
|2|Nairobi              |18                     | 2          |60               |10 | 1|
|3|Nairobi               |60                     | 1            |180               |44| 0|
|4|Nairobi              |25                     | 2            |200               |30|0|
|5|Nairobi             |30                     | 2           |300               |10|1|
|6|Kitusuru               |45                     | 1            |900               |55|0|
|7|Nairobi              |50                     | 3            |120               |20| 0|
|8|Nairobi              |78                     | 1          |60               |10 | 1|
|9|Nairobi                |26                     | 1            |180               |44| 0|
|10|Nairobi            |23                     | 2            |200               |30|0|
|11|Nairobi             |33                     | 2            |300               |10|1|
|12|Nairobi               |45                     | 1            |1200               |55|0|
|13|Nairobi             |30                     |2             |800               |100| 0|
|14|Nairobi              |33                     | 6           |60               |90 | 1|
|15|Nairobi              |26                     | 1            |180               |44| 0|
|16|Nairobi           |23                     | 2            |2000               |30|0|
|17|Nairobi             |33                     | 2            |3000               |10|1|
|18|Nairobi            |45                     | 1            |1200               |55|0|
|19|Nairobi             |66                     |1              |50               |100| 0|
|20|Nairobi            |78                     | 1           |60               |10 | 1|
|21|Nairobi              |26                     | 1            |180               |44| 0|
|22|Nairobi            |23                     | 2           |2000               |30|0|
|23|Nairobi             |33                     | 2            |300               |10|1|
|24|Nairobi            |45                     | 1           |1200               |55|0|
|25|Nairobi           |66                     |1              |50               |100| 0|
|26|Nairobi             |78                     | 1           |60               |10 | 1|
|27|Nairobi              |26                     | 1           |180               |44| 0|
|28|Nairobi          |23                     | 2            |200               |30|0|
|29|Nairobi            |33                     | 2          |3000               |10|1|
|30|Nairobi             |45                     | 1            |1200               |55|0|


### Preview of Data
```data.describe()```

![describe](https://user-images.githubusercontent.com/11560987/43975555-afa89966-9ca3-11e8-988f-3122c79e3283.PNG)


### Data Visualization
* **Graphing the features in a pair plot** 

![swap_fraud](https://user-images.githubusercontent.com/11560987/43934745-60242a14-9c16-11e8-9fe9-97de48961f1e.png)

## Results
```0.625``` Not very bad since the data is Random.


### ROC
![accuracy](https://user-images.githubusercontent.com/11560987/43937762-3b996100-9c25-11e8-942a-77b9b3ba07f5.png)


## Contributing
Read  [Contributing](https://gist.github.com/PurpleBooth/b24679402957c63ec426)

## Machine learning algorithms:

#### Linear Algorithms:

* **Algorithm 1: Linear Regression**
* **Algorithm 2: Logistic Regression**
* **Algorithm 3: Linear Discriminant Analysis**

*Nonlinear Algorithms:

* **Algorithm 4: Classification and Regression Trees**
* **Algorithm 5: Naive Bayes**
* **Algorithm 6: K-Nearest Neighbors**
* **Algorithm 7: Learning Vector Quantization**
* **Algorithm 8: Support Vector Machines**

*Ensemble Algorithms:

* **Algorithm 9: Bagged Decision Trees and Random Forest**
* **Algorithm 10: Boosting and AdaBoost**

## License

 Copyright [2018] [Madonah Syombua]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
