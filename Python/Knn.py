from sklearn import naive_bayes, model_selection
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import pandas as pd
import time
from sklearn.naive_bayes import GaussianNB
from sklearn.utils import shuffle
start_time = time.time()
pd.set_option('display.max_columns', 500)

df = pd.read_csv('analyses.csv')

#Extract Target Feature
df = shuffle(df)
df.fillna(0, inplace =True)
targetLabels = df['fake_news']

df.drop(['fake_news','news_no','user_no',"user_spread_news_no_times",'following_accounts_number',
         'user_total_real_news_spread','user_total_news_spread','user_total_fake_news_spread',
        'user_number_of_followers',
            ],axis=1, inplace=True)


print(df)


#--------------------------------------------
# Hold-out Test Set + Confusion Matrix
#--------------------------------------------
#define naive bayes model using Gaussian based information 
knn = KNeighborsClassifier()
#Split the data: 80% training : 20% test set

instances_train, instances_test, target_train, target_test = train_test_split(df, targetLabels, test_size=0.2, random_state=0)
#fit the model using just the test set
knn.fit(instances_train, target_train)
#Use the model to make predictions for the test set queries
predictions = knn.predict(instances_test)
# print(instances_test)
print("--------------------------------------------------")
# print(target_test)
''
#Output the accuracy score of the model on the test set
print("Accuracy= " + str(accuracy_score(target_test, predictions, normalize=True)))
#Output the confusion matrix on the test set
confusionMatrix = confusion_matrix(target_test, predictions)
print(confusionMatrix)
print("\n\n")
 
 
#--------------------------------------------
# Cross-validation to Compare to Models
#--------------------------------------------
#run a 10 fold cross validation on this model using the full chrum data
scores=model_selection.cross_val_score(knn, instances_train, target_train, cv=10)
#the cross validaton function returns an accuracy score for each fold
print("Dec Tree based Model:")
print("Score by fold: " + str(scores))
#we can output the mean accuracy score and standard deviation as follows:
print("Accuracy: %0.4f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
print("\n\n")

print("--- %s seconds ---" % (time.time() - start_time))