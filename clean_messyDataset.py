import pandas as pd
import numpy as np


df= pd.read_excel('C:/Users/Mian Mohsin/Desktop/data_project/messy_dataset_100_entries.xlsx')
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.isna().sum())

#remove AGE column bcz its repeating the same values as Age and also remove Extra Column bcz its completely empty filled with redundant string
df.drop(columns=['AGE','Extra Column'], inplace=True)
# print(df.columns)

#clean column names
df.columns= (
    df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
)
# print(df.columns)

#` Convert Unknown or error values into NaN`
df.replace(['UNKNOWN', 'ERROR', ''], np.nan, inplace=True)
# print(df.isna().sum())
# print(df.info())

# convert income column to numeric
# print(df['income'].unique())
df['income'] = (
    df['income']
    .astype(str)
    .str.replace('₦', '', regex=False)
    .str.replace(',', '', regex=False)
    .str.strip()
)

df['income'] = pd.to_numeric(df['income'], errors='coerce')
# print(df['income'].unique())

#convert date column to datetime
# print(df['date_joined'].unique())
#clean suffixes from date strings
df['date_joined'] = (
    df['date_joined']
    .astype(str)
    .str.replace(r'(\d+)(st|nd|rd|th)', r'\1', regex=True)
)
df['date_joined'] = pd.to_datetime(
    df['date_joined'],
    errors='coerce',
    dayfirst=False
)
df.loc[df['date_joined'] < '2000-01-01', 'date_joined'] = pd.NaT
# print(df['date_joined'].isna().sum())

# The date_joined column was removed because the dates were written in many different formats and the column did not clearly represent one thing. Some values looked like joining dates while others looked like very old birth dates. After cleaning, most of the values became missing, so the column was not reliable and was removed.
df.drop(columns=['date_joined'], inplace=True)
cat_col=['name','gender']
for col in cat_col:
    df[col]=(
        df[col]
        .str.title()
        .str.strip()
        .fillna('Unknown')
        
    )

df['phone_number']=df['phone_number'].astype(str).str.replace(r'[^\d+]','',regex=True)
df['phone_number']=df['phone_number'].fillna('Unknown')
df['email'] = df['email'].str.lower()

# keep age column nan values as is because dropping or filling them may lead to loss of important information

df.to_excel('C:/Users/Mian Mohsin/Desktop/data_project/cleaned_messy_dataset_100_entries.xlsx', index=False)