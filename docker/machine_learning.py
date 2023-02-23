# Imports
# %matplotlib inline
import pandas as pd
from sklearn.neighbors import NearestCentroid
from sklearn import tree
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsClassifier
import statistics
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns




# file path - this for linux windows you will need "//"
feature = ["permission" , "permission_number", "url_css", "check_css_for_script", "check_css_for_malicious_code", "js_check", "label"]

f_path = "/home/rivka/Desktop/chr/code/sample.csv"
df = pd.read_csv(f_path,names= feature, header=None)

X = list(zip(df["permission"],df["permission_number"],df["url_css"], df["check_css_for_script"], df["check_css_for_malicious_code"] , df["js_check"]))

y = np.stack(df["label"])
print(y)



# We split the dataset to train and test according to the required ration
# Do not change the test_size -> you can change anything else
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1765, random_state=42, stratify=y)


# We choose our model of choice and set it's hyper parameters you can change anything
clf = RandomForestClassifier(n_estimators=50)
clf.fit(X_train, y_train)
# print(sorted(Counter(y_train).items()))
# We print our results
predictions = clf.predict(X_test)
true_labels = y_test
cf_matrix = confusion_matrix(true_labels, predictions)
clf_report = classification_report(true_labels, predictions, digits=5)
heatmap = sns.heatmap(cf_matrix, annot=True, cmap='Blues', fmt='g', 
                      xticklabels=np.unique(true_labels), 
                      yticklabels=np.unique(true_labels)) 

# The heatmap is cool but this is the most important result
print(clf_report)