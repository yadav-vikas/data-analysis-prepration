import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn 
import seaborn as sns
import glob
import re

files = glob.glob('states*.csv')

df_list = []
for file in files:
  data = pd.read_csv(file)
  df_list.append(data)
us_census = pd.concat(df_list)
print(us_census)
print(us_census.dtypes)
print(us_census.columns)
us_census.Income = pd.to_numeric(us_census.Income.replace('[\$]','',regex=True))
print(us_census.dtypes)
gender_split = us_census.GenderPop.str.split('_',expand=True)
us_census['Men'] = gender_split[0]
us_census['Women'] = gender_split[1]
us_census.Men =us_census.Men.replace('M','',regex=True)
us_census.Women = us_census.Women.replace('F','',regex=True)
us_census.Men = pd.to_numeric(us_census.Men)
us_census.Women = pd.to_numeric(us_census.Women)
us_census = us_census.drop(columns=['GenderPop'])
print(us_census)
plt.scatter(us_census.Women, us_census.Income)
plt.show() 
plt.clf()
us_census=us_census.fillna(value={'Women':us_census.TotalPop - us_census.Men,'Men':us_census.TotalPop - us_census.Women})
print(us_census.shape)
us_census = us_census.drop_duplicates()
print(us_census.duplicated())
print(us_census.shape)
plt.scatter(us_census.Women, us_census.Income)
plt.show() 
plt.clf()
print(us_census.columns)
plt.hist(us_census.Men,color='blue',alpha=0.5)
plt.hist(us_census.Women,color='red',alpha=0.2)
plt.legend(labels=['Men','Women'])
plt.title('Men VS Women in us_census data')
plt.show()
plt.clf()
plt.figure(figsize=(8,15))
plt.pie(us_census.TotalPop,labels=us_census.State,labeldistance=1.05)

plt.show()
plt.clf()
y_pos=np.arange(len(us_census.State))
#fig, ax = plt.subplots()
sns.barplot(us_census.TotalPop,us_census.State,orient='h')
#fig.autofmt_xdate()
plt.show()
