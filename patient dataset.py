import pandas as pd
df = pd.read_excel("C:\\Users\\User\\OneDrive\\Desktop\\Project\\cancer patient data sets.xlsx")

print(df.head())
print(df.info())
print(df.describe())

#check for missing values
print(df.isnull().sum())

# removing duplicates
df.drop_duplicates(inplace=True)

# clean column names
df.columns= df.columns.str.strip().str.lower()
print(df.columns)

import matplotlib.pyplot as plt
import seaborn as sns

#distribution of age
plt.figure(figsize=(10,6))
sns.histplot(df['age'], bins=30, kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('No.of patients')
plt.show()

# distribution of gender
plt.figure(figsize=(6,4))
sns.countplot(x='gender', data=df)
plt.title('Distribution of Gender')
plt.xlabel('Gender')
plt.ylabel('No.of patients')
plt.show()  