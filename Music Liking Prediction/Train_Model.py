import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.externals import joblib

music_data=pd.read_csv('music.csv')

#creating input set
x=music_data.drop(columns=['genre'])
#creating output set
y=music_data['genre']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
#Building a model
model=DecisionTreeClassifier()
model.fit(x_train,y_train)
joblib.dump(model,'prediction.joblib')
Prediction=model.predict(x_test)
accuracy=accuracy_score(y_test,Prediction)
print(accuracy)


