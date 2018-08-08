import networkx as nx
# from networkx import *
import pandas as pd
pd.set_option('display.max_columns', 500)
import matplotlib.pyplot as plt
import numpy as np



df = pd.read_csv('C:/Users/Daroo/Documents/GitHub/FakeNewsNet/Python/fake_news_1.csv',
                              sep=',')
"""
df = df[['user_no','user_number_of_followers','user_total_news_spread' ]]
dr = df.groupby('user_no').first()
# dr = dr.sort_values('user_number_of_followers', ascending=False)
dr = dr.sort_values('user_total_news_spread', ascending=False)
"""
# df = df.groupby('user_no').count()['user_total_probability_sharing_fake_news'].reset_index()
df = df[['user_no','user_total_probability_sharing_fake_news' ]]
dr = df.groupby('user_no').first()
df = dr['user_total_probability_sharing_fake_news'].value_counts()
print(df)

# df = df['user_total_probability_sharing_fake_news'].value_counts()
# print(df['user_total_probability_sharing_fake_news'].value_counts())
threshold = 53


ax = df.plot(kind='bar', title ="", figsize=(10, 10), legend=True, fontsize=12)
ax.axhline(y=threshold,linewidth=1, color='k', linestyle ='--')
plt.xlabel('Probability of sharing a fake news')
plt.ylabel('Counts')
plt.show()




# df.plot.hist(grid=True, bins=20, rwidth=0.9,
#                    color='#607c8e')
# plt.title('Commute Times for 1,000 Commuters')
# plt.xlabel('Counts')
# plt.ylabel('Commute Time')
# plt.grid(axis='y', alpha=0.75)
# plt.show()