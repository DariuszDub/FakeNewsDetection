import pandas as pd
pd.set_option('display.max_columns', 500)
import random

#Read a file
df_bf_new_user = pd.read_csv('C:/Users/Daroo/Documents/GitHub/FakeNewsNet/Data/BuzzFeed/BuzzFeedNewsUser.txt',
                              sep='\t', names=['news_no','user_no', 'user_spread_news_no_times'])

df_bf_user_user = pd.read_csv('C:/Users/Daroo/Documents/GitHub/FakeNewsNet/Data/BuzzFeed/BuzzFeedUserUser.txt',
                              sep='\t', names=['user_no','follow_user_no'])
'''
#Get A 20% off from news(10% of fake_news, 10% of real_news) to create test dataset
real_news_test_sample = []
fake_news_test_sample = []
for x in range(18):
    real_news_test_sample.append(random.randint(1,90))
for x in range(18):
    fake_news_test_sample.append(random.randint(91,181))

news_test_sample = real_news_test_sample + fake_news_test_sample
#delete test
for news_no in news_test_sample:
    df_bf_new_user_test = df_bf_new_user.drop(df_bf_new_user[df_bf_new_user.news_no == news_no].index)   

print(df_bf_new_user)
'''

#Add column to hold source news
df_bf_new_user['source']="Bf"
#Get the number of followers for each user and number followed users
df_no_followers = df_bf_user_user.groupby('follow_user_no').count().reset_index()
df_follows_no = df_bf_user_user.groupby('user_no').count().reset_index()


#Add column wit nummber of followers - replaced nan and convert into int
df_bf_new_user = pd.merge(df_bf_new_user, df_no_followers, left_on='user_no', how='left', right_on='follow_user_no')
df_bf_new_user.drop('follow_user_no', axis=1, inplace=True)
df_bf_new_user.rename(columns={'user_no_x': 'user_no'}, inplace=True)
df_bf_new_user.rename(columns={'user_no_y': 'user_number_of_followers'}, inplace=True)
df_bf_new_user = df_bf_new_user.fillna(0)
df_bf_new_user['user_number_of_followers'] = df_bf_new_user['user_number_of_followers'].astype(int)

#Fooloowed accounts
df_follows_no.rename(columns={'follow_user_no': 'following_accounts_number'}, inplace=True)
df_bf_new_user = pd.merge(df_bf_new_user, df_follows_no, on='user_no', how='left')
df_bf_new_user = df_bf_new_user.fillna(0)
df_bf_new_user['following_accounts_number'] = df_bf_new_user['following_accounts_number'].astype(int)

# Label tru and fake news
df_bf_new_user['fake_news'] = 1
df_bf_new_user.loc[df_bf_new_user['news_no'] <= 91, 'fake_news'] = 0

#Count total spread(retweet) for each news
dr = df_bf_new_user.groupby('news_no').sum()['user_spread_news_no_times'].reset_index()
print(dr.sort_values('user_spread_news_no_times', ascending=False))
print(dr['user_spread_news_no_times'].sum())
#merge dataframe with number of spread newses
df = pd.merge(df_bf_new_user, dr, on='news_no', how='left')
df.rename(columns={'user_spread_news_no_times_y': 'news_total_spread_no'}, inplace=True)

'''
#create weight
df['news_weight'] = 0
df.loc[df['news_total_spread_no'] >= 100, 'news_weight'] = 1
df.loc[df['news_total_spread_no'] >= 200, 'news_weight'] = 2
df.loc[df['news_total_spread_no'] >= 300, 'news_weight'] = 3 
df.loc[df['news_total_spread_no'] >= 400, 'news_weight'] = 4
df.loc[df['news_total_spread_no'] >= 500, 'news_weight'] = 5
df.loc[df['news_total_spread_no'] >= 600, 'news_weight'] = 6 
df.loc[df['news_total_spread_no'] >= 700, 'news_weight'] = 7
df.loc[df['news_total_spread_no'] >= 800, 'news_weight'] = 8
df.loc[df['news_total_spread_no'] >= 900, 'news_weight'] = 9 
df.loc[df['news_total_spread_no'] >= 1000, 'news_weight'] = 10
df.loc[df['news_total_spread_no'] >= 1100, 'news_weight'] = 11


'''
#Calculate total fake news by user
df['fake_news_multiplyer'] = df['fake_news'] * df['user_spread_news_no_times_x']
df_new = df.groupby('user_no').sum()['fake_news_multiplyer'].reset_index()
df = pd.merge(df, df_new, on='user_no', how='left')
df.rename(columns={'user_spread_news_no_times_x': 'user_spread_news_no_times'}, inplace=True)
df.rename(columns={'fake_news_multiplyer_y': 'user_total_fake_news_spread'}, inplace=True)
df.drop('fake_news_multiplyer_x', axis=1, inplace=True)
# print(df.head(5))

#Calculate total news reatweats for each user
df_new = df.groupby('user_no').sum()['user_spread_news_no_times'].reset_index()
df = pd.merge(df, df_new, on='user_no', how='left')
df.rename(columns={'user_spread_news_no_times_x': 'user_spread_news_no_times'}, inplace=True)
df.rename(columns={'user_spread_news_no_times_y': 'user_total_news_spread'}, inplace=True)
# print(df.head(5).sort_values(by=['user_no'],ascending=True))

#Calculate true news reatweats for each user
df['user_total_real_news_spread'] = df['user_total_news_spread'] - df['user_total_fake_news_spread']
#Calculate probability of sharing a fake news
df['user_total_probability_sharing_fake_news'] =  (df['user_total_fake_news_spread'] / df['user_total_news_spread']).round(2)
df['user_total_probability_sharing_real_news'] =  (df['user_total_real_news_spread'] / df['user_total_news_spread']).round(2)
# print(df.head(5))
df.to_csv("fake_news_1.csv", index=False)

import datetime

unix_ts = 1474472520000
date = datetime.datetime.fromtimestamp(unix_ts / 1e3)
print(date)

