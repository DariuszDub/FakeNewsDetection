import pandas as pd
pd.set_option('display.max_columns', 500)
import matplotlib.pyplot as plt
import numpy as np




def get_20_80_dataset_for_analyzes():
    """Get training datset"""
    
    df = pd.read_csv('../Data/BuzzFeed/BuzzFeedNewsUser.txt',
                                  sep='\t', names=['news_no','user_no', 'user_spread_news_no_times'])
    r_df_pub_dates = pd.read_csv('r_news_order.csv',
                                  sep=',')
    f_df_pub_dates = pd.read_csv('f_news_order.csv',
                                  sep=',')
    df_t = pd.read_csv('../Data/BuzzFeed/BuzzFeedUserUser.txt',sep='\t', names=['user_no', 'follows'])
    
    df_follows_no = df_t.groupby('user_no').count().reset_index()
    
    unsort_news_punlished_by_date = pd.concat([r_df_pub_dates, f_df_pub_dates])
    sort_news_punlished_by_dat = unsort_news_punlished_by_date.sort_values(by=['publish_date'], ascending=True)
    
    news_punlished_by_date = sort_news_punlished_by_dat['news_no'].tolist()
    
    
    news_iter = 500
        
    # df.query((f'news_no == {news_punlished_by_date[:news_iter]}'), inplace = True)
    df.query((f'news_no == {news_punlished_by_date[19:91] + news_punlished_by_date[109:181]}'), inplace = True)
    #Get the number of followers
    df_no_followers = df_t.groupby('follows').count().reset_index()
    
    #Add column wit nummber of followers - replaced nan and convert into int
    df = pd.merge(df, df_no_followers, left_on='user_no', how='left', right_on='follows')
    df.drop('follows', axis=1, inplace=True)
    df.rename(columns={'user_no_x': 'user_no'}, inplace=True)
    df.rename(columns={'user_no_y': 'user_number_of_followers'}, inplace=True)
    df = df.fillna(0)
    df['user_number_of_followers'] = df['user_number_of_followers'].astype(int)
    
    #Fooloowed accounts
    df_follows_no.rename(columns={'follows': 'following_accounts_number'}, inplace=True)
    df = pd.merge(df, df_follows_no, on='user_no', how='left')
    df = df.fillna(0)
    df['following_accounts_number'] = df['following_accounts_number'].astype(int)
    
    # Label tru and fake news
    df['fake_news'] = 1
    df.loc[df['news_no'] <= 91, 'fake_news'] = 0
    
    #Count total spread(retweet) for each news
    dr = df.groupby('news_no').sum()['user_spread_news_no_times'].reset_index()
    
    #merge dataframe with number of spread newses
    df = pd.merge(df, dr, on='news_no', how='left')
    df.rename(columns={'user_spread_news_no_times_y': 'news_total_spread_no'}, inplace=True)
    
    
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
    
    
    
    print(len(df))
    df.to_csv("analyses.csv", index=False)
    print("done")
    
def get_entire_dataset_():
    """Get agregated datset for analyzes"""
    
    df = pd.read_csv('../Data/BuzzFeed/BuzzFeedNewsUser.txt',
                                  sep='\t', names=['news_no','user_no', 'user_spread_news_no_times'])
    r_df_pub_dates = pd.read_csv('r_news_order.csv',
                                  sep=',')
    f_df_pub_dates = pd.read_csv('f_news_order.csv',
                                  sep=',')
    df_t = pd.read_csv('../Data/BuzzFeed/BuzzFeedUserUser.txt',sep='\t', names=['user_no', 'follows'])
    
    df_follows_no = df_t.groupby('user_no').count().reset_index()
    

    df_no_followers = df_t.groupby('follows').count().reset_index()
    
    #Add column wit nummber of followers - replaced nan and convert into int
    df = pd.merge(df, df_no_followers, left_on='user_no', how='left', right_on='follows')
    df.drop('follows', axis=1, inplace=True)
    df.rename(columns={'user_no_x': 'user_no'}, inplace=True)
    df.rename(columns={'user_no_y': 'user_number_of_followers'}, inplace=True)
    df = df.fillna(0)
    df['user_number_of_followers'] = df['user_number_of_followers'].astype(int)
    
    #Fooloowed accounts
    df_follows_no.rename(columns={'follows': 'following_accounts_number'}, inplace=True)
    df = pd.merge(df, df_follows_no, on='user_no', how='left')
    df = df.fillna(0)
    df['following_accounts_number'] = df['following_accounts_number'].astype(int)
    
    # Label tru and fake news
    df['fake_news'] = 1
    df.loc[df['news_no'] <= 91, 'fake_news'] = 0
    
    #Count total spread(retweet) for each news
    dr = df.groupby('news_no').sum()['user_spread_news_no_times'].reset_index()
    
    #merge dataframe with number of spread newses
    df = pd.merge(df, dr, on='news_no', how='left')
    df.rename(columns={'user_spread_news_no_times_y': 'news_total_spread_no'}, inplace=True)
    
    
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
    
    
    
    print(len(df))
    df.to_csv("Entire_agregated_dataset.csv", index=False)
    print("done")

if __name__ == '__main__':
    
    get_20_80_dataset_for_analyzes()
    get_entire_dataset_()

