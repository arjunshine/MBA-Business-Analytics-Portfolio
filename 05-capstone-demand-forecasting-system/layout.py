# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 01:20:19 2019

@author: Arjun
"""
import pandas as pd
import matplotlib.pyplot as plt

def lay(df):
 l=df['Mode'].tolist()
 q=df['Quantity'].tolist()
 lay=[]
 qn=[]
 q_ind=[]
 for i in range (len(l)):   
  if l[i].isnumeric()== True:
      lay.append(l[i])
      qn.append(q[i])
    
 lz={'Table':lay,'Quantity':qn}
 lay_df= pd.DataFrame(lz)
 l_tp=int(input("Choose from the given option \n1.Most Prefered Tables\n2.Least Prefered Tables\n"))
 if l_tp ==1:
     print('##################################################################')
     print('MOST PREFERED TABLES\n')
     print('##################################################################') 
     l_num=int(input("\nEnter the number of tables :"))
     pd.value_counts(lay_df['Table'].values, sort=True).head(l_num)
     v_1=pd.value_counts(lay_df['Table'].values, sort=True).head(l_num)
     v_ind=v_1.index
     l1=[]
     l2=[]
     for i in range(l_num):
         l1.append(v_1[i])
         l2.append(v_ind[i])
     v_11=pd.DataFrame(l2,columns=['Table'])
     v_11['Quantity']=l1
     v_11.plot(kind='bar',x='Table',y='Quantity')
     plt.suptitle('Fav_tables', fontsize=20)
     plt.show()
 else:
     print('##################################################################')
     print('LEAST PREFERED TABLES\n')
     print('##################################################################') 
     l_num=int(input("\nEnter the number of tables :"))
     pd.value_counts(lay_df['Table'].values, sort=True).tail(l_num)
     v_2=pd.value_counts(lay_df['Table'].values, sort=True).tail(l_num)
     v_ind2=v_2.index
     l1=[]
     l2=[]
     for i in range(l_num):
         l1.append(v_2[i])
         l2.append(v_ind2[i])
     v_12=pd.DataFrame(l2,columns=['Table'])
     v_12['Quantity']=l1
     v_12.plot(kind='bar',x='Table',y='Quantity') 
     plt.suptitle('Non-Fav_tables', fontsize=20)
     plt.show()


