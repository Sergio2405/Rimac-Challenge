from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from lightgbm import LGBMClassifier

import pandas as pd 
import joblib

df = pd.read_csv("heart.csv")

numerical= df.drop(['HeartDisease'], axis=1).select_dtypes('number').columns
categorical = df.select_dtypes('object').columns

accuracy = []
model_names = []

X = df.drop('HeartDisease', axis=1)
y = df['HeartDisease']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

ohe = OneHotEncoder()
ct = make_column_transformer((ohe,categorical),remainder='passthrough')  

lgbmc = LGBMClassifier(random_state=0)

pipe = make_pipeline(ct, lgbmc)
pipe.fit(X_train, y_train)

joblib.dump(pipe, 'model.pkl') # exportando el modelo