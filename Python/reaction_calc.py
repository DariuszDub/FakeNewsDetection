import networkx as nx
# from networkx import *
import pandas as pd
from pandas.tests.frame.test_sort_values_level_as_str import ascending
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)

import community
from networkx.algorithms.community.centrality import girvan_newman
from networkx.algorithms import centrality
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('C:/Users/Daroo/Documents/GitHub/FakeNewsNet/Data/BuzzFeed/BuzzFeedNewsUser.txt',
                              sep='\t', names=['news_no','user_no', 'user_spread_news_no_times'])
r_df_pub_dates = pd.read_csv('C:/Users/Daroo/Documents/GitHub/FakeNewsNet/Python/r_news_order.csv',
                              sep=',')
f_df_pub_dates = pd.read_csv('C:/Users/Daroo/Documents/GitHub/FakeNewsNet/Python/f_news_order.csv',
                              sep=',')
df_t = pd.read_csv('C:/Users/Daroo/Documents/GitHub/FakeNewsNet/Data/BuzzFeed/BuzzFeedUserUser.txt',sep='\t', names=['user_no', 'follows'])

"""
print(df_t.head(5))
#Generate list of spreaded newses by each user and calculate retweat response betwen user and followers 
for row in df_t.itertuples():
    user_news_collection = df.query((f'user_no == {row[1]}'), inplace=False)
    user_news_spread_list = user_news_collection['news_no'].tolist()
    
    following_user_news_collection = df.query((f'user_no == {row[2]}'), inplace=False)
    following_user_news_spread_list = following_user_news_collection['news_no'].tolist()
    
    user_number_spredes_newses = len(user_news_spread_list)
    following_number_spredes_newses = len(following_user_news_spread_list)


    #check for retweted (matching) news betwen user and following users (match)
    matching_news = set(following_user_news_spread_list).intersection(user_news_spread_list)
    number_of_matches = len(matching_news)
    if len(matching_news) >=1:
        print(row[0])#, row[1], list(matching_news), number_of_matches, user_number_spredes_newses, following_number_spredes_newses)
        df_t.at[row[0], 'number_news_matches'] = number_of_matches
        df_t.at[row[0], 'user_no_spreeds_newses'] = user_number_spredes_newses
        df_t.at[row[0], 'follows_number_spreeds_newses'] = following_number_spredes_newses
        
#         print(df_t.query('number_news_matches >= 2', inplace=False))
            

df_t.to_csv('user_no_follows_match.csv', index=False)
"""
df = pd.read_csv('user_no_follows_match.csv')
df_u = df.groupby('user_no').sum()['number_news_matches'].reset_index()
df_f = df.groupby('follows').sum()['number_news_matches'].reset_index()
print(df_u.sort_values('number_news_matches', ascending=False))
print(df_f.sort_values('number_news_matches', ascending=False))