#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pymongo


# In[2]:


import pandas as pd
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db =client['rehab_facilities_db']
collection = db['facilities']
# part 1 and 2
df = pd.read_csv(r"C:\Users\22103198\Desktop\Inpatient Rehabilitation Facility.csv")

#date time to same form
df['Certification Date'] = pd.to_datetime(df['Certification Date'], format='%m/%d/%Y', errors='coerce')
df_dict = df.to_dict('records')
collection.insert_many(df_dict)
print("Data is inserted in the db")

#print(df.head())


# In[16]:


# part 3

#non_Profit = df[(df['Ownership Type']== 'Non-profit') & (df['Certification Date']>'2011-10-01')]
#print("Non profit Providers that were certified after 10-01-2011")
#print('\n')
non_prof = collection.find({
    "Ownership Type": "Non profit", 
    "Certification Date": {"$gt": pd.to_datetime("2011-10-01")}
})

print("Non-Profit providers certified after 10-01-2011:")
for provider in non_prof:
    print(provider)
print("\n")

# 


# In[17]:


#part 4

#profit_birmingham = df[(df['City/Town'] == 'BIRMINGHAM') & (df['Ownership Type'] == 'For profit')]
#print("Those providers in BIRMINGHAM and Ownership Type is For profit")
#print('\n')
#print(profit_birmingham)
birmingham_profit_providers = collection.find({
    "City/Town": "BIRMINGHAM", 
    "Ownership Type": "For profit"
})

print("Providers in BIRMINGHAM with Ownership Type = PROFIT:")
for provider in birmingham_profit_providers:
    print(provider)
print("\n")



# In[18]:


# part5

zip_code  = df[(df['ZIP Code'] >= 85000) & (df['ZIP Code'] <= 90000)]
print("Providers with ZIP codes in the range 85000-90000:")
print('\n')
print(zip_code)



# In[13]:


# part 6: Count For-Profit and Non-Profit providers
prof = len(df[df['Ownership Type'] == 'For profit'])
non_prof = len(df[df['Ownership Type'] == 'Non-profit'])

print("For-Profit providers:")
print(prof)
print("Non-Profit providers:")
print(non_prof)


# In[ ]:




