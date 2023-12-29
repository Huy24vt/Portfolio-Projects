#!/usr/bin/env python
# coding: utf-8
#Import packages and load data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings
import sys
if not sys.warnoptions:
    warnings.simplefilter("ignore")

data_ = pd.read_excel(r"C:\Users\ACER\Downloads\online+retail\Online Retail.xlsx")
data = data_.copy()
data.head()

# Handle missing data
data.isnull().sum()

# I intend to perform RFM segmentation. If the CustomerID is null, I won't be able to proceed with the anlysis.
data.dropna(inplace=True)

#Inspect data types
data.info()

#Now, let's proceed to review the descriptive statistics of the data
data.describe()

#I noticed some odd numbers in the data: negative quantities in Quantity column and zeros in Price column
data[data["Quantity"]<0]

#It appears that negative quantities are canceled invoices, we will exclude those entries from the data.
data = data[data["Quantity"]>0]

#And I will retain only transactions with a UnitPrice greater than 0
data = data[data["UnitPrice"]>0]

#Now, let's remove the outlier from Quantity and Price column
def outlier_threshold(dataframe,variable):
    quartile1 = dataframe[variable].quantile(0.01)
    quartile3 = dataframe[variable].quantile(0.99)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit

def replace_outlier(dataframe,variable):
    low_limit, up_limit = outlier_threshold(dataframe,variable)
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit

cols = ["Quantity", "UnitPrice"]
for col in cols:
    replace_outlier(data,col)

#And I will add some column for future use
data["Revenue"] = data["Quantity"] * data["UnitPrice"]
data["Day"] = data["InvoiceDate"].dt.day_name()
data["Year"] = data["InvoiceDate"].dt.year
data["Month"] = data["InvoiceDate"].dt.month_name()
data["Hour"] = data["InvoiceDate"].dt.hour

#Let's review the descriptive statistics of the data
data.describe()

#Everything seems okay, so we will head to EDA step
#EDA
#We will answer few questions here:
#(1) What is the overall sales?

sales_2010 = data[data["Year"]==2010].groupby("Month").sum()[["Revenue"]].reset_index()
sales_2011 = data[data["Year"]==2011].groupby("Month").sum()[["Revenue"]].reset_index()

plt.bar(sales_2010["Month"],sales_2010["Revenue"],label=("2010_sales"))
plt.bar(sales_2011["Month"],sales_2011["Revenue"],label=("2011_sales"))
plt.xticks(rotation=45)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.show()

#(2) How do sales vary on a weekly basis?
data["Last Order"] = data["InvoiceDate"]
Sales_weekly = data.resample("w",on="Last Order").size()
fig = px.line(data, x=Sales_weekly.index, y=Sales_weekly, labels={"y":"Number of Sales",
                                                               "x": "Date"})
fig.update_layout(title_text="Number of Sales Weekly",
                 title_x = 0.5, title_font=dict(size=18))
fig.show()

#(3) How do sales vary on an hourly basis?
RushHours = data.groupby("Hour").count().reset_index()
plt.plot(RushHours["Hour"],RushHours["Revenue"])
plt.grid()
plt.xlabel("Hours")
plt.ylabel("Sales")
plt.show()

#(4) Which days of the week have the highest sales performance?
DOW = data.groupby("Day").sum()["Revenue"].reset_index()
sns.barplot(data=DOW,x="Revenue",y="Day",palette="coolwarm")
plt.show()

#Now I will perform RFM Segmentation
# First I will create RFM table
from datetime import datetime
today = datetime.now()
RFM = data.groupby('CustomerID').agg({
                                    'InvoiceDate': lambda x: (today - x.max()).days,
                                    'InvoiceNo': lambda x: x.nunique(),
                                    'Revenue': lambda x: x.sum()}).reset_index()
RFM.columns = ["ID","Recency","Frequency","Monetary"]
RFM.head()

#Caculate R-F-M Score and caculate RFM Score
RFM["Recency_Score"] = pd.qcut(RFM["Recency"],5,labels=[5,4,3,2,1])
RFM['Frequency_Score'] = pd.qcut(RFM['Frequency'].rank(method ='first') ,5 , labels= [1,2,3,4,5])
RFM["Monetary_Score"] = pd.qcut(RFM["Monetary"],5,labels=[1,2,3,4,5])
RFM["RFM_Score"] = (RFM["Recency_Score"].astype(str) + RFM["Frequency_Score"].astype(str) + RFM["Monetary_Score"].astype(str))
RFM.head()

#Our Customer Segmentation
seg_map = {
r'[1-2][1-2][1-5]': 'Hibernating',
r'[1-2][3-4][1-5]': 'At risk',
r'[1-2]5[1-5]' :'Cannot lose them',
r'3[1-2][1-5]' : 'About to sleep',
r'33[1-5]' : 'Need Attention',
r'[3-4][4-5][1-5]' : 'Loyal Customers',
r'[4-5][1-3][1-5]' : 'Good Potential',
r'5[4-5][1-5]' : 'Champions',
}
RFM['Segment'] = RFM['RFM_Score'] .replace(seg_map ,regex =True)

#Bar Plot for Our segments
Segments = (RFM['Segment'].value_counts(normalize=True)* 100).reset_index(name='percentage')
Segments = Segments.round(1)
b =sns.barplot(y='index',x='percentage', data=Segments, palette = 'crest_r')
for i, v in enumerate(Segments['percentage']):
    b.text(v,i+0.20," {:.1f}".format(v)+"%", color='black', ha="left")
    b.set_ylabel('Segmentation')
    b.set_title('Customer Segmentation')

#This is our RFM table
RFM.head()

#I will export the data to a CSV file and visualize it using Power BI.
RFM.to_csv('RFM_table.csv', index=False)



