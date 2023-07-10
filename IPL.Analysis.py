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


data.drop_duplicates('season',keep= 'last')[['season','winner']]

#Sort by Season
data.drop_duplicates('season',keep= 'last')[['season','winner']].sort_values('season') 

# upload delivery file 
delivery = pd.read_csv('deliveries.csv')
delivery

runs = delivery.groupby('batsman')
runs

runs.get_group('V Kohli').shape

runs['batsman_runs'].sum()

# Highest run by batsman
runs['batsman_runs'].sum().sort_values(ascending = False).head()

# Top 10 Batsman 
runs['batsman_runs'].sum().sort_values(ascending = False).head(10)

mask1 = delivery['batsman_runs'] == 4
new_delivery = delivery[mask1]
new_delivery.shape


mask2 = delivery['batsman_runs'] == 6
nd_delivery = delivery[mask2]
nd_delivery.shape

nd_delivery.shape[0]

# Count No.of 6s hitted by player
nd_delivery.groupby('batsman')['batsman_runs'].count()

#top 10 batsman no. of 6s hitted 
nd_delivery.groupby('batsman')['batsman_runs'].count().sort_values(ascending = False).head(10)

#top 10 no. of 6s hitted by each batman
nd_delivery.groupby('batsman')['batsman_runs'].count().sort_values(ascending = False).head(10)

# Find the highest runs scored by V.Kohli  against bowling team 
vk = delivery[delivery['batsman'] == 'V Kohli']
vk.groupby('bowling_team')['batsman_runs'].sum
vk.groupby('bowling_team')['batsman_runs'].sum
vk.groupby('bowling_team')['batsman_runs'].sum().sort_values(ascending = False)



 #Creating function to find it for each player
def run_scorer(batsman_name):
    vk = delivery[delivery['batsman'] == batsman_name]
    return vk.groupby('bowling_team')['batsman_runs'].sum().sort_values(ascending = False).index[0]

run_scorer('MS Dhoni')

run_scorer('DA Warner')

run_scorer('G Gambhir')

# find strike rate

mask3 = delivery['over'] > 15
death_over = delivery[mask3]
death_over


# ISIN Function
# find the most destructive death over in history of ipl 
# strike rate = (no.of runs/no.of bolls)/100 
# Min batsman 200 balls in over16 - 20
death_over.groupby('batsman')['batsman_runs'].count()

All_bat = death_over.groupby('batsman')['batsman_runs'].count()
All_bat

X = All_bat>200
X

All_bat[X]

batsman_list = All_bat[X].index.tolist()
batsman_list
batsman_list

#Runs Scored by these batsman
#Balls played by these batsman

mask4 = delivery['batsman'].isin(batsman_list)
final = delivery[mask4]

runns = final.groupby('batsman')['batsman_runs'].sum()
balls = final.groupby('batsman')['batsman_runs'].count()

strike_rate = (runns/balls)*100
strike_rate


#Merge
# Find the orange cap holder for each season
matches = pd.read_csv('matches.csv')
matches

new_data = delivery.merge(matches, left_on = 'match_id', right_on = 'id')
new_data

new_data.groupby(['season','batsman'])['batsman_runs'].sum()
type(new_data.groupby(['season','batsman'])['batsman_runs'].sum())

# reset_index() - will convert 2 index Series to dataframe 
new_data.groupby(['season','batsman'])['batsman_runs'].sum().reset_index()

redcap = new_data.groupby(['season','batsman'])['batsman_runs'].sum().sort_values(ascending = False).reset_index().drop_duplicates(subset = 'season',keep = 'first')

redcap.sort_values('season')

# Season-wise Readcap holder 
redcap.sort_values('season')[['season','batsman']]

#Pivot Ipl Dataset - 6s hit by a team in which over 

mask23 = delivery['batsman_runs'] == 6
six = delivery[mask23]

six. shape

six

six.pivot_table(index = 'over', columns = 'batting_team', values = 'batsman_runs',aggfunc = 'count')

Ray = six.pivot_table(index = 'over', columns = 'batting_team', values = 'batsman_runs',aggfunc = 'count')
import seaborn as sns

sns.heatmap(Ray)




















