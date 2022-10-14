# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""             LGM Internship - Lets Grow More


                  BEGINNER LEVEL TASK

            Task1 - VIP Data Science Task


             Author: Yogender Singh

                          Iris Flowers Classification ML Project """
                          
#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.manifold import TSNE                          

# Read the dataset using pandas library by read_csv method.
data = pd.read_csv('iris.csv')
data.head()
data.tail()
data.count()
data.shape

data.columns
data.value_counts()

data.isnull().sum()

actual_y=data['Species']

x=data.drop(['Id','Species'],axis=1)
x.head()


from sklearn.cluster import KMeans
      #Here inertia means Sum of squared distances of samples to their closest cluster center getting through the data observed.
      
number_of_clusters=[2,3,4,5,6,7,8,10]
inertia=[]
for i in number_of_clusters:
  kmeans=KMeans(n_clusters=i).fit(x)
  inertia.append(kmeans.inertia_)

plt.plot(number_of_clusters,inertia)
plt.xlabel('Number of Clusters',size=22)
plt.ylabel('inertia_',size=22)
plt.title('Number of Clusters vs inertia_',size=25)
plt.grid()
plt.show()

kmeans = KMeans(n_clusters = 3)
y_kmeans = kmeans.fit_predict(x)

# add these predicted y's as column to our dataframe
x['predicted_y']=y_kmeans

kmeans.cluster_centers_

y_mapping={1:'Setosa',2:'versicolour',0:'virginica'}

x['predicted_y']=x['predicted_y'].map(y_mapping)

setosa = x.loc[x.predicted_y == 'Setosa',['SepalLengthCm','SepalWidthCm']]
virginica = x.loc[x.predicted_y == 'virginica',['SepalLengthCm','SepalWidthCm']]
versicolour = x.loc[x.predicted_y == 'versicolour',['SepalLengthCm','SepalWidthCm']]

plt.scatter(setosa['SepalLengthCm'], setosa['SepalWidthCm'], s = 100, c = 'red', label = 'Setosa')
plt.scatter(virginica['SepalLengthCm'], virginica['SepalWidthCm'], s = 100, c = 'blue', label = 'Virginica')
plt.scatter(versicolour['SepalLengthCm'], versicolour['SepalWidthCm'], s = 100, c = 'green', label = 'Versicolour')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 100, c = 'yellow', label = 'Centroids')
plt.legend()

plt.xlabel('SepalLengthCm Feature',size=18)
plt.ylabel('SepalWidthCm Feature',size=18)
plt.title('Clusters with its Centroids',size=25)
plt.grid()
plt.show()

x.describe()


x.info()
x.corr()

iris=data
iris.plot(kind="scatter", x="SepalLengthCm", y= "SepalWidthCm")

                              #Checking for outliars
plt.figure(1)
plt.boxplot([iris['SepalLengthCm']])
plt.figure(2)
plt.boxplot([iris['SepalWidthCm']])
plt.show()

sns.violinplot(data=iris, x="Species", y="PetalWidthCm",palette="rocket")

sns.pairplot(iris,hue='Species');


#distribution of different species in in form of pie chart
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
l = ['Versicolor', 'Setosa', 'Virginica']
s = [50,50,50]
ax.pie(s, labels = l,autopct='%1.2f%%')
plt.show()


plt.figure(figsize=(12,8)) 
sns.heatmap(x.corr(), annot=True, cmap='Dark2_r', linewidths = 2)
plt.show()

x = data.drop(columns="Species")
y = data["Species"]
   
                        # Data Pre-processing:
                            
 X = iris[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].values
X[0:5]

y = iris['Species'].values
y[0:5]

#Split datset into train and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 3)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


                                # CLASSIFICATION MODELS:
 # from KNN model 
 
 #Create an instance of the KNN classifier with k = 3
neigh = KNeighborsClassifier(n_neighbors = 3)

#Fit the model with the training data X_train and y_train
neigh.fit(X_train,y_train)

#Use the test data X_test to predict the output, yhat_KNN
yhat_KNN = neigh.predict(X_test)

#Use the real values y_test and the predicted values yhat_KNN to find the accuracy of the model 
print("Accuracy of the KNN model: ", accuracy_score(y_test, yhat_KNN))


# from Decision Tree Classifier:
    
    #Create an instance of the decision tree classifier
dec_tree = DecisionTreeClassifier(criterion="entropy")

#Fit the model with the training data X_train and y_train
dec_tree.fit(X_train, y_train)

#Use the test data X_test to predict the output, yhat_tree
yhat_tree = dec_tree.predict(X_test)

#Use the real values y_test and the predicted values yhat_tree to find the accuracy of the model 
print("Accuracy of the Decision Tree: ", accuracy_score(y_test, yhat_tree))
      
    # from Support Vector Machine:
        
  #Create an instance of the svm classifier using the kernel function, rbf (Radial Basis Function)
svm_model = svm.SVC(kernel='rbf', gamma = 'auto')

#Fit the model with the training data X_train and y_train
svm_model.fit(X_train, y_train)

#Use the test data X_test to predict the output, yhat_svm
yhat_svm = svm_model.predict(X_test)

#Use the real values y_test and the predicted values yhat_svm to find the accuracy of the model 
print("Accuracy of the SVM Model :", accuracy_score(y_test, yhat_svm))      
        
# from Logistic Regression:
    
    #Create an instance of the Logistic Regression classification model
#using the 'liblinear' optimizer and set C, the Inverse of regularization strength to 0.01
LR = LogisticRegression(C=0.01, solver='liblinear')

#Fit the model with the training data X_train and y_train
LR.fit(X_train,y_train)

#Use the test data X_test to predict the output, yhat_LR
yhat_LR = LR.predict(X_test)

#Use the real values y_test and the predicted values yhat_LR to find the accuracy of the model 
print("Accuracy of the SVM Model :", accuracy_score(y_test, yhat_LR))

                              #Final Result Using Models are :-
                        
  results = pd.DataFrame({
    'Model': ['KNN','Decision Tree','Support Vector Machines','Logistic Regression'],
    'Score': [0.955,0.933,0.977,0.688]})

result_df = results.sort_values(by='Score', ascending=False)
result_df = result_df.set_index('Score')
result_df.head(9)      

                                         #Performance Evaluation of the models :-
                                         
                                        
ari_kmeans = adjusted_rand_score(actual_y, kmeans.labels_)

round(ari_kmeans, 2)                                        
        
        
        
        
        
        
        
        
        
        
        
        
        
        















