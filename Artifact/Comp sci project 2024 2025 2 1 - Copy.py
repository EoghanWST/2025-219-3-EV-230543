import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#projectimport pandas as pd (Data Cleaning)
import pandas as pd

df = pd.read_csv("fifa85up_data.csv")

#change name of colums to better names
df.rename(columns={'Height(in cm)': 'Height','Dribbling': 'Dribbling2', 'Value(in Euro)': 'Value', 'Wage(in Euro)': 'Wage', 'Preferred Foot': 'Foot', 'Club Position': 'Position', 'Pace Total': 'Pace', 'Shooting Total': 'Shooting', 'Passing Total': 'Passing', 'Dribbling Total': 'Dribbling', 'Defending Total': 'Defending', 'Physicality Total': 'Physicality'}, inplace=True)

#copy colums over to new file
#print(df.info())
df = df[['Full Name', 'Overall', 'Value', 'Nationality', 'Age', 'Height', 'Club Name', 'Wage', 'Position', 'Foot', 'Pace', 'Shooting', 'Passing', 'Dribbling', 'Defending', 'Physicality',]].copy()
df.to_csv("fifa_clean2.csv")

#check for missing data
#print (df.isnull().any())
#call rows with mising data
df1 = df[df.isna().any(axis=1)]

#save csv as dict
PlayerData_dict = df.to_dict()
print(PlayerData_dict)

cred = credentials.Certificate("firebaseKeyFinal.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://connecttojvacode-default-rtdb.europe-west1.firebasedatabase.app/'})
#ref = db.reference('/')#reference the root node of the database
#ref.set({"Test":"Tester"})
ref = db.reference('CleanData')#reference the root node of the database
for key,value in PlayerData_dict.items():
    ref.update({key:value})

#ref.set(testfile.csv)
