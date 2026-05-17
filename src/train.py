from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os
import time


#Load Dataset()

print("Loading Dataset")
time.sleep(2)
data = load_iris()

X = data.data
y = data.target

#Split dataset
print("Spliting data..")
time.sleep(2)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 42)

#Train model

print("Training you model..")
time.sleep(2)

model = RandomForestClassifier()

model.fit(X_train, y_train)

#prediction

print("Predicting...")
time.sleep(2)

y_pred = model.predict(X_test)

#accuracy

print("Accuracy Score predicting..")
time.sleep(2)

accuracy = accuracy_score(y_test , y_pred)

print (f"Model Accuracy - {accuracy}")


#create model folder

os.makedirs("model", exist_ok= True)

# save model
print("Saving Model..")
time.sleep(2)

joblib.dump(model , "model/model.pkl")

time.sleep(2)
print("Model Saved Successfully")