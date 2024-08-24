# -*- coding: utf-8 -*-
"""Loan Approval Prediction using Machine Learning .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cxHit4639Jif-1gLODewvw00I0r08-IY
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import svm

df = pd.read_csv('/content/Copy of loan.csv')

df.head()

df.info()

df.isnull().sum()

df['loanAmount_log'] = np.log(df['LoanAmount'])
df['loanAmount_log'].hist(bins=20)

df.isnull().sum()

df['TotalIncome'] = df['ApplicantIncome'] + df['CoapplicantIncome']
df['TotalIncome_log'] = np.log(df['TotalIncome'])
df['TotalIncome_log'].hist(bins=20)

"""'"""

df['Married'].fillna(df['Married'].mode()[0], inplace =True)
df['Self_Employed'].fillna(df['Self_Employed'].mode()[0], inplace =True)
df['Dependents'].fillna(df['Dependents'].mode()[0], inplace =True)

df.LoanAmount = df.LoanAmount.fillna(df.LoanAmount.mean())
df.loanAmount_log = df.loanAmount_log.fillna(df.loanAmount_log.mean())

df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0], inplace =True)
df['Credit_History'].fillna(df['Credit_History'].mode()[0], inplace =True)


df.isnull().sum()

x= df.iloc[:,np.r_[1:5,9:11,13:15,]].values
y= df.iloc[:,12].values

x

y

print("per of missing gender is %2f%%" %((df['Gender'].isnull().sum()/df.shape[0])*100))

print('number of people who take loan as group by gender:')
print(df['Gender'].value_counts())
sns.countplot(x='Gender', data=df, palette = 'Set1' )

print('number of people who take loan as group by marital status:')
print(df['Married'].value_counts())
sns.countplot(x='Married', data=df, palette = 'Set1' )

print('number of people who take loan as group by dependents:')
print(df['Dependents'].value_counts())
sns.countplot(x='Dependents', data=df, palette = 'Set1' )

print('number of people who take loan as group by employed:')
print(df['Self_Employed'].value_counts())
sns.countplot(x='Self_Employed', data=df, palette = 'Set1' )

print('number of people who take loan as group by Loanamount:')
print(df['LoanAmount'].value_counts())
sns.countplot(x='LoanAmount', data=df, palette = 'Set1' )

print('number of people who take loan as group by Credit_History:')
print(df['Credit_History'].value_counts())
sns.countplot(x='Credit_History', data=df, palette = 'Set1' )

from re import X
from sklearn.model_selection import train_test_split
X_train , X_test ,  y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=0)

from sklearn.preprocessing import LabelEncoder
LabelEncoder_x = LabelEncoder()

for i in range(0,5):
     X_train[:,i] = LabelEncoder_x.fit_transform(X_train[:,i])
     X_train[:,7] = LabelEncoder_x.fit_transform(X_train[:,7])

X_train

Labelencoder_y = LabelEncoder()
y_train = Labelencoder_y.fit_transform(y_train)

y_train

for i in range(0,5):
    X_test[:,i]= LabelEncoder_x.fit_transform(X_test[:,i])
    X_test[:,i] = LabelEncoder_x.fit_transform(X_test[:,7])
X_test

y_test = Labelencoder_y.fit_transform(y_test)
y_test

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.fit_transform(X_test)

"""So, standard scalar removes the mean and scales each feature variable to unit variance this opearation performed feature wise in an independent way everything dome let's see which classifier is best for prediction by seeing their accuracy"""

from sklearn.ensemble import RandomForestClassifier

rf_Clf = RandomForestClassifier()
rf_Clf.fit(X_train, y_train)

from sklearn import metrics
y_pred = rf_Clf.predict(X_test)

print('acc of random forest clf is ', metrics.accuracy_score(y_pred, y_test))
y_pred

from sklearn.naive_bayes import GaussianNB
nb_classifier = GaussianNB()
nb_classifier.fit(X_train, y_train)

y_pred = nb_classifier.predict(X_test)
print('acc of gaussianNB is %.', metrics.accuracy_score(y_pred, y_test))

y_pred

from sklearn.tree import DecisionTreeClassifier
dt_clf =  DecisionTreeClassifier()
dt_clf.fit(X_train, y_train)

y_pred = dt_clf.predict(X_test)
print('acc of DT is', metrics.accuracy_score(y_pred, y_test))

y_pred

from sklearn.neighbors import KNeighborsClassifier
kn_clf = KNeighborsClassifier()
kn_clf.fit(X_train, y_train)

y_pred = kn_clf.predict(X_test)
print('acc of KNN is', metrics.accuracy_score(y_pred, y_test))

y_pred

