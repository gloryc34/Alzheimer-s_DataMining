import pandas as pd
pd.options.mode.chained_assignment = None

data = pd.read_csv('Alzheimer_s_Disease_and_Healthy_Aging_Data.csv', low_memory=False)
data = data.drop(columns=['Sample_Size','Response','ResponseID','StratificationCategory3','Stratification3','StratificationCategoryID3','StratificationID3','Report']) #Drops these columns

data['RowId'] = range(0, len(data)) #Adds incrementing ID to each row
data['Data_Value'] = data['Data_Value'].fillna(data['Data_Value'].median())
data['Data_Value_Alt'] = data['Data_Value_Alt'].fillna(data['Data_Value_Alt'].median())
data['Low_Confidence_Limit'] = pd.to_numeric(data['Low_Confidence_Limit'], errors='coerce')
data['Low_Confidence_Limit'] = data['Low_Confidence_Limit'].fillna(data['Low_Confidence_Limit'].median())
data['High_Confidence_Limit'] = pd.to_numeric(data['High_Confidence_Limit'], errors='coerce')
data['High_Confidence_Limit'] = data['High_Confidence_Limit'].fillna(data['High_Confidence_Limit'].median())

