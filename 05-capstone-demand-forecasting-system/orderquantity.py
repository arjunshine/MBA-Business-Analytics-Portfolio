# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 01:22:00 2019

@author: Arjun
"""

import squarify
import matplotlib.pyplot as plt
import pandas as pd
#count of items
#qunatity of corresponding item
def most(pf):
    #1.Most ordered dishes in the hotel 
    item=pf.Item.unique()
    m_s=[]
    m_c=[]
    m_n=[]
    for i in range(len(item)):
        pf1=pf[pf.Item==item[i]]
        s=sum(pf1.Quantity)
        c=pf1.Code.reset_index()
        p=pf1.Item.reset_index()
        m_s.append(s)
        m_c.append(c.Code[0])
        m_n.append(p.Item[0])
        
    m_lst=list(zip(m_c,m_n,m_s))
    m_df=pd.DataFrame(m_lst, columns=['Code','Item','Quantity'])
    m_df=m_df.sort_values(by='Quantity',ascending=False)
    mst_num=int(input("Enter the Number of Dishes to analyze from the total:"))
    m_df1=m_df.head(mst_num)
    squarify.plot(sizes=m_df1['Quantity'], label=m_df1['Code'], alpha=.8 )
    plt.suptitle('MOST_ORDERED', fontsize=20)
    plt.axis('off')
    plt.show()
    print(m_df1.to_string(index=False))
    
    #2.MODE 
    l_m1=[]
    l_m=pf['Mode'].unique()
    for i in range(len(l_m)):
        if l_m[i].isalpha()==True:
            l_m1.append(l_m[i])
            
    m_nm=int(input("How many dishes top dishes to find from different modes?:"))
    for i in range(len(l_m1)):
        pf2=pf[pf.Mode==l_m1[i]]
        pf2_it=pf2['Item'].unique()
        x_it=[]
        x_qn=[]
        x_co=[]    
        for o in range(len(pf2_it)):
            pf3=pf2[pf2.Item==pf2_it[o]].reset_index()
            x_qn.append(sum(pf3.Quantity))
            x_co.append(pf3.Code[0])
            x_it.append(pf3.Item[0])
        m_lst1=list(zip(x_co,x_it,x_qn))
        m_df2=pd.DataFrame(m_lst1,columns=['Code','Item','Quantity'])
        m_df2=m_df2.sort_values(by='Quantity',ascending=False)
        #print(l_m1[i])
        m_df2=m_df2.head(m_nm)
        m_df2.plot(kind='bar',x='Code',y='Quantity')
        plt.suptitle(l_m1[i], fontsize=20)
        plt.show()
        print(m_df2.to_string(index=False))
        
    m_nm=int(input("Dishes least bought from different modes?:"))
    for i in range(len(l_m1)):
        pf2=pf[pf.Mode==l_m1[i]]
        pf2_it=pf2['Item'].unique()
        x_it=[]
        x_qn=[]
        x_co=[]    
        for o in range(len(pf2_it)):
            pf3=pf2[pf2.Item==pf2_it[o]].reset_index()
            x_qn.append(sum(pf3.Quantity))
            x_co.append(pf3.Code[0])
            x_it.append(pf3.Item[0])
        m_lst1=list(zip(x_co,x_it,x_qn))
        m_df2=pd.DataFrame(m_lst1,columns=['Code','Item','Quantity'])
        m_df2=m_df2.sort_values(by='Quantity',ascending=True)
        #print(l_m1[i])
        m_df2=m_df2.head(m_nm)
        m_df2.plot(kind='bar',x='Code',y='Quantity')
        plt.suptitle(l_m1[i], fontsize=20)
        plt.show()
        print(m_df2.to_string(index=False))


