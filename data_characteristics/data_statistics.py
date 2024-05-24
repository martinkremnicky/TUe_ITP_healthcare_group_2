import pandas as pd

data = pd.read_csv("C:/Users/hilde/Documents/Technische Universiteit Eindhoven/Int. Team Project/TUe_ITP_healthcare_group_2/data_characteristics/patient_list_latest.csv")
#print(data.head())

# calculate the number of patients
number_patients = len(data)
print("number of patients is: ", number_patients)

# the number of patients with a malignent tumor (0 is benign, 1 is malignent)
malignent_patients= data.loc[data['malignant/benign'] == 1.0]
print("number of malignent patients is: ", len(malignent_patients))

# the average age of the patients
average_age = data.loc[:,'age'].mean()
print("the average age is: ", average_age)