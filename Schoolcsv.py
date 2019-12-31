import pandas
import matplotlib

df = pandas.read_csv('school.csv', parse_dates=['enrolldate'])
print(df)
# check the people who didnt ans all qns where there are empties per qns
#print(df.isnull().sum())
# imputation process of dealing with missing records
# fill missing/ remove them
# Gender 9 missing 0= male 1= female coded then just fill unknown with 2
df['Gender'].fillna(2, inplace=True) # inplace makes sure its updated
df['Smoking '].fillna(3, inplace=True)
#print(df.isnull().sum()) #Gender and smoking becomes zero
#there was missing reading
median = df['Reading'].median()
df['Reading'].fillna(median,inplace=True)

#piecharts
import matplotlib.pyplot as plt
df.groupby('Gender').size().plot(kind='pie', autopct='%2.2f%%',
                                 explode=(0,0.4,0))# pull out dimantle the pie chart 0, 0,0.2... 0,0, 0.2, 0...depending on parts for gender 3 parts for smoking four parts
plt.title('Gender proportion in %')
plt.xlabel('')
plt.ylabel('')
plt.show()

