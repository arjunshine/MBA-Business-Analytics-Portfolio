# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 04:12:18 2019

@author: Arjun
"""
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib import pyplot 

def i_frcst(data):
 comb_df_1=data[['Date','Item','Quantity']]
 comb_df_1.Item=comb_df_1.Item.replace("MURG","CHICKEN")
 comb_df_1=comb_df_1.groupby(['Date','Item'],as_index=False).sum()
 Item_list=['CHICKEN','MUTTON','PANEER','EGG','MUSHROOM','FISH','DAL','GOBI','PRAWNS','CORN','RICE','SOUP']
 Item_df=pd.DataFrame((Item_list),columns=['Items'])
 print(Item_df)
 item_opt=int(input('Enter the corrseponding number:'))
 unique_date=comb_df_1.Date.unique()
 print('Item choosed: ',Item_df.Items[item_opt])
 c_date=[]
 c_Item=[]
 c_quan=[]
 for i in unique_date:
     for j in range(len(comb_df_1)):
         if i == comb_df_1.Date[j]:
             if Item_df.Items[item_opt] in comb_df_1.Item[j]:
                 c_date.append(comb_df_1.Date.iloc[j])
                 c_Item.append(comb_df_1.Item.iloc[j])
                 c_quan.append(comb_df_1.Quantity.iloc[j])
                  
 c1=pd.DataFrame(list(zip(c_date,c_quan)),columns =['Date', 'Quantity'])  
 c1= c1.groupby('Date')['Quantity'].sum().reset_index() 
 c1.plot(kind='line',x='Date',y='Quantity') 
 plt.suptitle('Daily', fontsize=20)
 pyplot.show()
 c2=c1.groupby('Date')['Quantity'].sum()
 c_df=c2.to_frame()
 frd=int(input("Enter  the forecast period in days: "))
 import forecast_arima_model_function as famf
 famf.lgraph(c2)
 famf.ac_plot(c_df)
 c2=famf.adf_test(c2)
 famf.my_a_arima(c2,c_df,frd) 
#########################################################


