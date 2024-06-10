import pandas as pd
from sklearn.model_selection import train_test_split

# Read patient data
data = pd.read_csv("patient_list_latest.csv")  

# Fill nan cells
data['malignant/benign'] = data['malignant/benign'].fillna(0) 

# Split data into train, validation and test sets
X_train, X_test = train_test_split(data, test_size=0.1, random_state=42, stratify = data['malignant/benign'])
train, X_val = train_test_split(X_train, test_size=0.15, random_state=42, stratify = X_train['malignant/benign'])

train_set=pd.DataFrame(train)
val_set = pd.DataFrame(X_val)
test_set=pd.DataFrame(X_test)

# Save info
train_set.to_csv('training.csv', index=False)
val_set.to_csv('validation.csv', index = False)
test_set.to_csv('test.csv', index=False)