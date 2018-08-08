from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

# df = pd.read_csv('itr_1.csv')
df= pd.read_csv('analyses.csv',
                              sep=',')
#Extract Target Feature
# df = shuffle(df)
df.fillna(0, inplace =True)
targetLabels = df['fake_news']

# df.drop(['source','news_total_spread_no','news_no','fake_news','user_total_fake_news_spread',
#          'user_fake_spread_probability','user_true_spread_probability','user_total_true_news_spread'],axis =1, inplace=True)
df.drop(['fake_news','news_no','user_no',"user_spread_news_no_times",'following_accounts_number',
         'user_total_real_news_spread','user_total_news_spread','user_total_fake_news_spread',
#         'user_total_probability_sharing_fake_news',
        'user_number_of_followers',
            ],axis=1, inplace=True)






X = df 
y = targetLabels
lr = LogisticRegression()
X2 = sm.add_constant(X)
est = sm.OLS(y, X2)
est2 = est.fit()
print(est2.summary())


