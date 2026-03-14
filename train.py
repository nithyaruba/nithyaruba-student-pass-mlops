
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import mlflow
import mlflow.sklearn
import pickle

df = pd.read_csv("dataset.csv")

X = df[["hours"]]
y = df["pass"]

model = DecisionTreeClassifier()
model.fit(X,y)

mlflow.set_experiment("student_pass_prediction")

with mlflow.start_run():
    mlflow.sklearn.log_model(model,"model")

pickle.dump(model,open("model.pkl","wb"))

print("Model trained successfully")
