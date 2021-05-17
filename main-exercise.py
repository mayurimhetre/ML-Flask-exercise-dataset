import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix


df = sns.load_dataset('exercise')

df = df.drop(['Unnamed: 0'],axis=1)
df_temp =  pd.get_dummies(df[['diet','time']],drop_first=True)

df.drop(['diet','time'],axis=1,inplace=True)
df = pd.concat([df,df_temp],axis=1)


X = df.drop('kind',axis=1)
Y = df['kind']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(solver='liblinear')
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix
# Summary of the predictions made by the classifier
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
# Accuracy score
from sklearn.metrics import accuracy_score
print('accuracy is',accuracy_score(y_pred,y_test))


import pickle
# open a file, where you ant to store the data
file = open('logistic_regression_model_01.pkl', 'wb')

# dump information to that file
pickle.dump(classifier, file)


print(df['id'].value_counts())
data = np.array([[15,88,1,0,0]])
my_prediction = classifier.predict(data)
print(my_prediction[0])