from sklearn.externals import joblib

model=joblib.load('prediction.joblib')
predictions=model.predict([[21,1]])
print(predictions)

