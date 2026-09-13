# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 01:19:32 2019

@author: Arjun
"""
import pandas as pd
import numpy as np 
from mlxtend.frequent_patterns import apriori,association_rules
from mlxtend.preprocessing import TransactionEncoder

#################################################################
#df=pfp.copy()
############################################################################
## ACTUAL CODE ############
def nw_index(df):
    mbf_df=df[['Bill_No','Quantity']]
    mb_gp= mbf_df.groupby('Bill_No')['Quantity'].sum().reset_index() 
    mb_gp.set_index('Bill_No', inplace = True)  
    x1=pd.value_counts(mbf_df['Bill_No'].values, sort=False).to_frame()#.reset_index()
    x1.columns=['Cases']
    x1_ind=x1.index
    drop_ind=[]
    for i in range(len(x1_ind)):
        if x1.Cases[x1_ind[i]]==1:# dropping bills with 1 item
            drop_ind.append(x1_ind[i])
            x1=x1.drop(x1_ind[i])            
    x1_ind=x1.index # new index
    del mbf_df,mb_gp   
    x1_1=x1.Cases
    mb={'Cases':x1_1}
    mbf_df= pd.DataFrame(mb).reset_index()
    mbf_df.columns=['Bill_No','Cases']#meta
    mbf_df2=df[['Bill_No','Item','Code','Price','Quantity']]
    mbf_df2=mbf_df2.groupby(['Bill_No','Code','Item','Price'])['Quantity'].sum()
    mbf_df2=mbf_df2.drop(index=drop_ind)
    mbf_df3=mbf_df2.reset_index()  
    df_mba=mbf_df3[['Bill_No','Code','Quantity']]
    df_mba=df_mba.groupby(['Bill_No','Code'])['Quantity'].sum().reset_index()
    df_mba1=df_mba[['Bill_No','Code']]
    return(df_mba1)
   
def apri(df_mba1):
    # Item-Based Collaborative Filtering (IB-CF) #
    #aprioriTable
    un_b_no=list(df_mba1.Bill_No.unique())
    un_code=list(df_mba1.Code.unique())
    apri_df=pd.DataFrame(columns=un_code,index=un_b_no)#empty df with bill & code 
    #fill up apriori table
    #takes 3 hours or more
    for i in range(len(apri_df)):
        for o in range(len(df_mba1)):
            if apri_df.index[i] == df_mba1.Bill_No[o]:
                apri_df.at[apri_df.index[i],df_mba1.Code[o]]=1            
    a_df=apri_df.copy() #.fillna(0) # fill Nan with 0
    return(a_df)
   
def apr_cp(a_df1):    
    a_df1=a_df1.fillna(0)
    ############ PB PYTHON_MBA
    #frequent item sets that have a support of at least 5%
    m_supp=float(input("Enter minimum support value(0.005 prefered):"))#0.005
    frequent_itemsets = apriori(a_df1, min_support=m_supp, use_colnames=True)
    print(list(frequent_itemsets))
    return(frequent_itemsets)
    ####  generate the rules 
m_conf=0.05    
def conf_rules(m_conf,frequent_itemsets):    
    # Confidence RUles
    rules_conf=association_rules(frequent_itemsets, metric="confidence", min_threshold=float(m_conf))
    rules_conf["antecedent_len"] = rules_conf["antecedents"].apply(lambda x: len(x))
    print("Available Relations:\n",rules_conf)
    a_l=input("Specify antecedent length(min 1):")
    a_c=input("Specify confidence filter parameter(min 0.15):")
    a_lt=input("Specify lift filter parameter(min 1):")
    r_c = rules_conf[ (rules_conf['antecedent_len'] >= int(a_l)) & (rules_conf['confidence'] > float(0.15)) &
           (rules_conf['lift'] > int(a_lt))]
    print("\n\n*************AVAILABLE RELATIONS*************\n\n",r_c)
    return(r_c)
    
def lift_rules(m_lift,frequent_itemsets):    
    # LIFT RULES
    rules_lift= association_rules(frequent_itemsets, metric="lift", min_threshold=float(m_lift))
    rules_lift["antecedent_len"] = rules_lift["antecedents"].apply(lambda x: len(x))
    print("Available Relations:\n",rules_lift)
    a1_l=input("Specify antecedent length(min 1):")
    a1_c=input("Specify confidence filter parameter(min 0.15):")
    a1_lt=input("Specify lift filter parameter(min 1):")
     
    r_l = rules_lift[ (rules_lift['antecedent_len'] >= int(a1_l)) & (rules_lift['confidence'] > float(a1_c)) &
           (rules_lift['lift'] >int(a1_lt)) ]
    print("\n\n*************AVAILABLE RELATIONS*************\n\n",r_l)
    return(r_l)
    
    #########
'''    
    i_c_1=input("Enter the Code of Item 1 from the list: ")
    i_c_2=input("Enter the Code of Item 2 from the list: ")

    
    print(rules_lift[rules_lift['antecedents'] == {str(i_c_1),str(i_c_2)}])
    
    ##############################################################################
    i_c_3=input("Enter the Code of Item from the list: ")
    print(rules_lift[rules_lift['antecedents'] == {str(i_c_3)}])
    if rules_lift['antecedents']== 'CB':
        print("YA")
        
   
    

frequent_itemsets=ft.copy()
m_lift=0.2
'''