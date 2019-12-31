import pandas  # acquire data and leaning
import matplotlib  # Plot/visualize
data = pandas.read_csv("power.csv")
print(data)
print(data['Solar'])
print(data['Consumption'])
print(data.describe())# give you basic stats
print(data.shape) # gives you how many rows and columns
print(data.isnull().sum()) # find missing data per colum

import matplotlib.pyplot as plt
fig, object = plt.subplots()
object.hist(data['Consumption'], color= 'orange')
plt.title("Distribution of Consuption")
plt.xlabel("Consumption GWh")
plt.ylabel("Freq.")
plt.show()


fig, object = plt.subplots()
object.hist(data['Wind'], color= 'orange')
plt.title("Distribution of Wind")
plt.xlabel("Wind GWh")
plt.ylabel("Freq.")
plt.show()


fig, object = plt.subplots()
object.scatter(data['Consumption'], data['Wind'], color= 'gray')
plt.title("Distribution of Consumption vs Wind")
plt.xlabel("Consumption GWh")
plt.ylabel("Wind GWh.")
plt.show()

fig, object = plt.subplots()
object.scatter(data['Consumption'], data['Wind+Solar'], color= 'red')
plt.title("Distribution of Consumption vs Wind+Solar")
plt.xlabel("Consumption GWh")
plt.ylabel("Wind+Solar GWh.")
plt.show()