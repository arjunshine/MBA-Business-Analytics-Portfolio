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

############################################################################
## ACTUAL CODE ############

mbf_df=df[['Bill_No','Quantity']]
mb_gp= mbf_df.groupby('Bill_No')['Quantity'].sum().reset_index() 
mb_gp.set_index('Bill_No', inplace = True) 

x1=pd.value_counts(mbf_df['Bill_No'].values, sort=False).to_frame()#.reset_index()
x1.columns=['Cases']
#x1.columns=['Bill_No','Quantity']

x1_ind=x1.index
#len(x1_ind)
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
    
##########################

#df_mba=mbf_df3.groupby(['Bill_No','Code'])['Quantity'].sum()
df_mba=mbf_df3[['Bill_No','Code','Quantity']]
df_mba=df_mba.groupby(['Bill_No','Code'])['Quantity'].sum().reset_index()
df_mba1=df_mba[['Bill_No','Code']]

# Item-Based Collaborative Filtering (IB-CF) #


#aprioriTable
un_b_no=list(df_mba1.Bill_No.unique())
un_code=list(df_mba1.Code.unique())
apri_df=pd.DataFrame(columns=un_code,index=un_b_no)#empty df with bill & code 

#fill up apriori table
for i in range(len(apri_df)):
    for o in range(len(df_mba1)):
        if apri_df.index[i] == df_mba1.Bill_No[o]:
            apri_df.at[apri_df.index[i],df_mba1.Code[o]]=1
            
a_df=apri_df.copy()  #.fillna(0) # fill Nan with 0
a_df1=pd.read_excel(r"C:/Users/Arjun/Documents/Trimester 5/DEMAND_ANALYSIS [ PY ]/APRIORI.xlsx",
                 sep='\t',header=0,index_col=0)
a_df1=a_df1.fillna(0)
a_df=a_df.fillna(0)

# to replace 1 with column name
a_df1=a_df1.loc[:, 'CTM':'PS'].replace(1, pd.Series(a_df1.columns, a_df1.columns))
#a_df1=a_df1.replace(0,np.nan)

############ PB PYTHON_MBA
#frequent item sets that have a support of at least 5%
m_supp=0.005
m_conf=0.5 #input("Enter the minimum required Confidence level [0<x<1] : ")
m_lift=2 #input("Enter the minimum required Lift level : ")
frequent_itemsets = apriori(a_df1, min_support=m_supp, use_colnames=True)
print(list(frequent_itemsets))

####  generate the rules 

# Confidence RUles
rules_conf=association_rules(frequent_itemsets, metric="confidence", min_threshold=0.05)
rules_conf["antecedent_len"] = rules_conf["antecedents"].apply(lambda x: len(x))
print("Available Relations:\n",rules_conf)

r_c = rules_conf[ (rules_conf['antecedent_len'] >= 2) & (rules_conf['confidence'] > 0.15) &
       (rules_conf['lift'] > 1)]
print(r_c)

# LIFT RULES
rules_lift= association_rules(frequent_itemsets, metric="lift", min_threshold=0.2)
rules_lift["antecedent_len"] = rules_lift["antecedents"].apply(lambda x: len(x))
print("Available Relations:\n",rules_lift)

 
r_l = rules_lift[ (rules_lift['antecedent_len'] >= 2) & (rules_lift['confidence'] > 0.15) &
       (rules_lift['lift'] > 1) ]

print(r_l)


#########
i_c_1=input("Enter the Code of Item 1 from the list: ")
i_c_2=input("Enter the Code of Item 2 from the list: ")

print(rules_lift[rules_lift['antecedents'] == {str(i_c_1),str(i_c_2)}])

##############################################################################
i_c_3=input("Enter the Code of Item from the list: ")
print(rules_lift[rules_lift['antecedents'] == {str(i_c_3)}])
if rules_lift['antecedents']== 'CB':
    print("YA")
    
#######################################
import pyfpgrowth
patterns = pyfpgrowth.find_frequent_patterns(a_df, 2)
rules = pyfpgrowth.generate_association_rules(patterns, 0.7)

apri_df.to_excel(r"C:/Users/Arjun/Documents/Trimester 5/DEMAND_ANALYSIS [ PY ]/APRIORI.xlsx", header=True)

fake=pd.read_excel(r"C:/Users/Arjun/Documents/Trimester 5/DEMAND_ANALYSIS [ PY ]/APRIORI.xlsx",
                 sep='\t',header=0,index_col=0)

'''
###### SAMPLE CODE ##########################




dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets_te = apriori(df, min_support=0.6, use_colnames=True)

frequent_itemsets_te

association_rules(frequent_itemsets_te, metric="confidence", min_threshold=0.7)
rules = association_rules(frequent_itemsets_te, metric="lift", min_threshold=1.2)
rules
del frequent_itemsets_te,df_te,te_ary,dataset
'''