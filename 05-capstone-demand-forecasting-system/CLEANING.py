# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 20:56:01 2019

@author: Arjun
"""
import pandas as pd
import datetime

def clean(pf):
 pf.columns=['Bill_No', 'Date', 'C', 'D','E','Time_Stamp','G','KOT','I','J','K','L','M','N','O','P','Q','R','Code','Quantity','Price','Item','W','X','Mode','Z','AA','BB']
 pf=pf.drop(['C','D','E','G','I','J','K','L','M','N','O','P','Q','R','W','X','Z','AA','BB'],axis=1)
 pf['Time_Stamp']=pf['Time_Stamp'].dt.time
 pf['Date']=pf['Date'].dt.date
 pf["Date"] = pd.to_datetime(pf["Date"]).dt.strftime('%Y-%m-%d')
 pf.Mode=pf.Mode.replace(to_replace = ['HD4','HD2','HD','HD5','HD1','HD3','EMIRA','stff','ZOMAT','SWIGG','P','P1','P2','P3','P4','P5','P6','P7','A1','A2','A3','B','5A'],value =['HOMEDELIVERY','HOMEDELIVERY','HOMEDELIVERY','HOMEDELIVERY','HOMEDELIVERY','HOMEDELIVERY','EMIRATES','STAFF','ZOMATO','SWIGGY','PARCEL','PARCEL','PARCEL','PARCEL','PARCEL','PARCEL','PARCEL','PARCEL','PARCEL','PARCEL','PARCEL','PARCEL','5'])  
 pf.sort_values(by=['Date'],inplace = True, ascending=True)
 return(pf)
