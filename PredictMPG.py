import pandas
import sklearn
import matplotlib.pyplot as plt
df = pandas.read_csv('auto-mpg.csv')
print(df)
print(df.describe())
print(df.corr())

print(df.isnull().sum())
print(df.dtypes)

array = df.values # we read all data into an array

features = array[:, 0:7] # : colon -All rows ....11 is not counted here
labels = array[:, 7]

from sklearn import model_selection
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(features, labels, test_size=0.30, random_state=42)

# linear regression model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, Y_train)
print('Traning.....finished')

# ask the model to predict X_test
predictions = model.predict(X_test)
print(predictions) # model will predict sales from X_test....we hide y_test which has the mpg

# compare the predictions and y_test(mpg)
from sklearn.metrics import  r2_score
print('R squared =', r2_score(Y_test, predictions))

from sklearn.metrics import mean_squared_error
print('mean squared error = ', mean_squared_error(Y_test, predictions))
# we need to find square root

# plotting....we visualize the model performance in a scatter plot
import matplotlib.pyplot as plt
plt.style.use('seaborn')
figure,ax = plt.subplots()
ax.scatter(Y_test, predictions, color= 'green') # scatter
ax.plot(Y_test, Y_test, color= 'red') # Best fit # line
ax.set_xlabel('Y Test')
ax.set_ylabel('Model predictions')
ax.set_title('Y Test vs Model Predictions')
plt.show()


#mpg = [[8 ,307,130, 3504, 12, 70,1]]
#observation = model.predict(mpg)
#print(mpg)



