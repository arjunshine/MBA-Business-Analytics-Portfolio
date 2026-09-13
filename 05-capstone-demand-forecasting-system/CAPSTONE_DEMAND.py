# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 03:57:04 2020

@author: Arjun
"""
import os
import pandas as pd
cwd = os.getcwd()
#the directory of saved python files
os.chdir("C:\\Users\\Arjun\\Documents\\Trimester 5\\DEMAND_ANALYSIS [ PY ]")

print("*"*90)
print("\nWelcome to DFS 1.0\n")
print("*"*90)

opt=input("Have you already aggregated the data?(Y/N):")
if opt=='N':
    print("\nPlease provide the details for aggregation\n")
    lmd1=input("Enter the location of Master data files:")
    #C:\Users\Arjun\Documents\Trimester 5\TRIAL\DEMAND_ANALYSIS-DATA\MASTERDATA
    lmd2=input("Enter the location to store monthly aggregate:")
    #C:\Users\Arjun\Documents\Trimester 5\TRIAL\DEMAND_ANALYSIS-DATA\CAP_MONTHwise
    lmd3=input("Enter the location to store total aggregate:")
    #C:\Users\Arjun\Documents\Trimester 5\TRIAL\DEMAND_ANALYSIS-DATA\CAP_AGGRG
    import EXL_agg as egg
    egg.prep(lmd1,lmd2,lmd3)   


x='Y'
while(x=='Y'):
    ser=int(input("Choose the service:\n1.Layout Analysis"
                 " \n2.Individual Forecasting\n3.Combined forecasting\n"
                 "4.Order Frequency\n5.Offer Development\n")) 
    
    print("\nLOADING THE DATA\n",'-'*90)
    pfp=pd.read_excel(r"file:///C:/Users/Arjun/Documents/Trimester 5/TRIAL/DEMAND_ANALYSIS-DATA/New folder/working.xlsx",
                     sep='\t',header=0)
    if ser ==1:
        import layout as lt
        lt.lay(pfp)    
    elif ser ==2:
        import model as mdl
        mdl.fast(pfp)   
    elif ser == 3:
        import combi_forecast as cf
        cf.i_frcst(pfp)
    elif ser ==4 :
        import orderquantity as oq
        oq.most(pfp)
    elif ser==5 :
        import mba_association as mba
        opt1=input("Do you want to create a new apriori table? or work with existing one?(Y/N)\n\n"
                   "*********WARNING: TAKES 3 HOUR TO CREATE NEW ONE***************\n")
        if opt1=='N':
            a_df1=pd.read_excel(r"C:/Users/Arjun/Documents/Trimester 5/DEMAND_ANALYSIS [ PY ]/APRIORI.xlsx",
                         sep='\t',header=0,index_col=0)
            ft=mba.apr_cp(a_df1)
            m_lift=input("Enter the minimum required Lift level[0.2] : ")
            a2=mba.lift_rules(m_lift,ft)
            print(a2)
            i_c_1=input("Enter the Code of Item 1 from the list: ")
            i_c_2=input("Enter the Code of Item 2 from the list: ")
            print(a2[rules_lift['antecedents'] == {str(i_c_1),str(i_c_2)}])
            m_conf=input("Enter the minimum required Confidence level [0<x(0.05)<1] : ")
            a1=mba.conf_rules(m_conf,ft)
            print(a1)
            i_c_1=input("Enter the Code of Item 1 from the list: ")
            i_c_2=input("Enter the Code of Item 2 from the list: ")
            print(a1[rules_conf['antecedents'] == {str(i_c_1),str(i_c_2)}])
        elif opt1=='Y':
            a3=input("Are you sure(Y/N)?")
            if a3=='Y':
                b1=mba.nw_index(pfp)
                b2=mba.apri(b1)
                ft=mba.apr_cp(b2)
                m_lift=input("Enter the minimum required Lift level[0.2] : ")
                a2=mba.lift_rules(m_lift,ft)
                m_conf=input("Enter the minimum required Confidence level [0<x(0.05)<1] : ")
                a1=mba.conf_rules(m_conf,ft)
                      
    else:
        print('List index out of stock...\n J.K, enter a valid option.')
           
    x=input("Do you want to continue? (Y/N):")   
  

import layout_re as l  
l.lay(pfp,5)        