import numpy as np
import pandas as pd

data = pd.read_csv('file:///E:\project\matches.csv.csv')
print(data)

data.head(2)

data.tail()

data.shape()

data.info()

data.describe
#fetch the column
data['winner']

data[['team1','team2','winner']]
data['winner'].shape

data[['team1','team2','winner']].shape
#fetch the row
data.loc[0]

data.loc[0:5]

data.loc[0:11:2]

data.loc[[0,5,6]]

data.iloc[:,[4,5,10]]

# Masking 
mask = data["city"]== "Hyderabad"
print(mask)

data[mask]
# no.of matches in Hyderabad
data[mask].shape
# no.of matches in selected city

def get_count_city(city):
  mask = data["city"] == city
  return data[mask].shape[0]


get_count_city("Rajkot")

# condition - matches played in hyderabad after 2010, and no.of matches.
mask1 = data['city'] == 'Hyderabad'
mask2 = data['date'] > '2010-01-01'
data[mask1 & mask2]
data[mask1 & mask2].shape[0]

# Search no. of matches win by each team - Value_counts() - counts Categarical data of Series/Single Column 
data['winner'].value_counts()

#Plot with Pandas 
import matplotlib.pyplot as plt
data['winner'].value_counts().plot(kind = 'bar')
data['winner'].value_counts().head().plot(kind = 'bar')

# Represatation of batting & Fieldng
data['toss_decision'].value_counts()
data['toss_decision'].value_counts().plot(kind = 'pie')

# cal frequency of win by run
data['win_by_run'].plot(kind = 'hist')


# max no. of matches played by team

data['team1'].value_counts() 
data['team2'].value_counts()
data['team1'].value_counts() + data['team2'].value_counts()

# Sort Values - 
# # max no. of matches played by team - top 5 team

(data['team1'].value_counts() + data['team2'].value_counts()).sort_values(ascending = False)
(data['team1'].value_counts() + data['team2'].value_counts()).sort_values(ascending = False).head()

# Sort data by City
data.sort_values('city') # to make changes permanent use inplace = True

# Sort data  City in ascending order and date in descending order 
data.sort_values(['city','date'],ascending=[True,False])

# Droping Duplicates 

data.drop_duplicates(subset=["city"])

# Check for Duplicate City

print(data.duplicated())

# find Ipl Winner for each season
data.drop_duplicates('season',keep='last')




















