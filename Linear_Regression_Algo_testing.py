#!C:\Users\Aniket\Anaconda3\python.exe
#Importing the library
import cgi,sys,cgitb,json,os;
import numpy as np;
import pandas as pd;
import math;
import matplotlib.pyplot as plt;
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import statsmodels.formula.api as sm

#Importing Datasets
#def dataset():
cgitb.enable()

form = cgi.FieldStorage()
country =eval(form.getvalue('country'))
HDI = eval(form.getvalue('HDI'))
population = eval(form.getvalue('population'))
internet = eval(form.getvalue('internet'))
GDP = eval(form.getvalue('GDP'))
atheletes = eval(form.getvalue('athletes'))


dataset = pd.read_csv('GDP_2012.csv');
array1 = [0,float(HDI),float(internet),45,int(atheletes),int(population),int(GDP),0]
#array1.append(0)
#array1.append(int(HDI))
#array1.append(int(internet))
#array1.append(45)
#array1.append(int(atheletes))
#array1.append(int(population))
#array1.append(int(GDP))
#array1.append(0)
X=dataset.iloc[:,[2,3,4,5,6,7,8,9]].values
Y=dataset.iloc[:,10].values
Z = dataset.iloc[:,[5,7]].values

Testprdiction = []
Testprdiction.append(array1)
def preprocess(X,Y):
#Taking care of Missing data
    imputer = Imputer(missing_values = 'NaN',strategy = 'mean',axis=0)
    imputer = imputer.fit(X[:,[0,1]])
    X[:,[0,1]]= imputer.transform(X[:,[0,1]])
    
    
    #Taking care of categorical data
    labelencoder_X = LabelEncoder()
    #X[:,0] = labelencoder_X.fit_transform(X[:,0])
    X[:,2] = labelencoder_X.fit_transform(X[:,2])
    onehotencoder = OneHotEncoder(categorical_features = [2])
    X = onehotencoder.fit_transform(X).toarray()
    
    #Avoiding dummy variable trap
    X=X[:,1:]
    
    #dividing in training and test sets
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state = 0)
    
    
    #scaling the data
    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.fit_transform(X_test)
    
    return X_train,X_test,Y_train,Y_test

   
def model(X_train,X_test,Y_train,Y_test):
#fitting multiple linear regression in your training sets
    regressor = LinearRegression()
    #regressor = RandomForestClassifier(n_estimators=50)
    regressor.fit(X_train,Y_train)
    
    #predicting values for test set
    Y_Pred = regressor.predict(X_test)
    newY = []
    for x in Y_Pred:
        if(x<0):
            newY.append(0)
        else:
            newY.append(int(x))
    difference = []        
    for x in range(0,len(newY)):
        if(newY[x]>Y_test[x]):
            difference.append((newY[x]-Y_test[x])/newY[x])
        else:
            difference.append((Y_test[x]-newY[x])/Y_test[x])
    y=0
    for x in difference:
        y = y+x
    percentage = y/len(newY)
    accuracy = (1-percentage)*100
    return accuracy,newY

def predict(X_train,X_test,Y_train,Y_test):
    regressor = LinearRegression()
    #regressor = RandomForestClassifier(n_estimators=50)
    regressor.fit(X_train,Y_train)

#Testprdiction = sc_X.fit_transform(Testprdiction)
    prediction_test  = regressor.predict(Testprdiction)
    prediction_test =(prediction_test/1000)
    prediction_test = math.ceil(prediction_test)
    return prediction_test
#prediction_test = sc_X.fit_transform(prediction_test)

#accuracy check
def evaluate():
    xtrain,xtest,ytrain,ytest = preprocess(X,Y)
    accuracy,predictvalue = model(xtrain,xtest,ytrain,ytest)
    medalcount = predict(xtrain,xtest,ytrain,ytest)
    #print(accuracy)
    #print(medalcount)
    return medalcount

medalcount = evaluate()


try:
    response =str(medalcount) 
    
    print("Content-type:application/json\r\n\r\n")
    print (json.dumps({'status':'yes', 'response':json.dumps(response)}))
except Exception as e:
    print("Content-type:application/json\r\n\r\n")
    print( json.dumps({'status':'error', 'except':json.dumps(str(e))}))
    


#print(accuracy_score(Y_test,[int(x) for x in newY]))

#Building optimal model using backward elimination
