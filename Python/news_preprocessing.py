import json
import datetime
import pandas as pd

#get published date for each f_news
f_news_dates = []
r_news_dates = []
for i in range(1,92):
    f_news = dict()
    r_news = dict()
    fake_file = ('C:/Users/Daroo/Documents/GitHub/FakeNewsNet/Data/BuzzFeed/FakeNewsContent/BuzzFeed_Fake_' + 
            str(i) + "-Webpage.json")    
    real_file = ('C:/Users/Daroo/Documents/GitHub/FakeNewsNet/Data/BuzzFeed/RealNewsContent/BuzzFeed_Real_' + 
            str(i) + "-Webpage.json")
    
    with open(fake_file) as f_file:
        f_data = json.load(f_file)
        if "publish_date" in f_data and isinstance(f_data['publish_date'], dict):
            date = datetime.datetime.fromtimestamp(f_data['publish_date']['$date'] / 1e3)
            f_news['publish_date'] = date
            f_news['news_no'] = i +91
            f_news_dates.append(f_news)
        else:
            f_news['publish_date'] = "nan"
            f_news['news_no'] = i + 90
            f_news_dates.append(f_news)
    with open(real_file ) as r_file:
        r_data = json.load(r_file)
        if "publish_date" in r_data and isinstance(r_data['publish_date'], dict):
            date = datetime.datetime.fromtimestamp(r_data['publish_date']['$date'] / 1e3)
            r_news['publish_date'] = date
            r_news['news_no'] = i
            r_news_dates.append(r_news)
        else:
            r_news['publish_date'] = "nan"
            r_news['news_no'] = i
            r_news_dates.append(r_news)
            
            
df_f = pd.DataFrame(f_news_dates)
print(df_f.sort_values(by=['publish_date'],ascending=True))
df_f.sort_values(by=['publish_date'],ascending=True).to_csv('f_news_order.csv', index=False)

df_r = pd.DataFrame(r_news_dates)
print(df_r.sort_values(by=['publish_date'],ascending=True))
df_r.sort_values(by=['publish_date'],ascending=True).to_csv('r_news_order.csv', index=False)