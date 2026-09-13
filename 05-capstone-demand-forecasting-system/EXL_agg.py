# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:44:32 2019

@author: 
"""

import datetime
import xlrd
import xlwt 
import pandas as pd
from xlwt import Workbook 
import os

def prep(d1,d2,d3):
# Workbook is created
 directory = d1#r"C:\Users\Arjun\Documents\Trimester 5\TRIAL\DEMAND_ANALYSIS-DATA\MASTERDATA"
 directory_2=d2#r"C:\Users\Arjun\Documents\Trimester 5\TRIAL\DEMAND_ANALYSIS-DATA\CAP_MONTHwise"
 directory_3=d3#r"C:\Users\Arjun\Documents\Trimester 5\TRIAL\DEMAND_ANALYSIS-DATA\CAP_AGGRG"
 array = []
 array2=[]
 months= []
 months2= [] 
 sheet_names=[]
 f_rows=[]
 f_columns=[]
 sheets=[]
 sheets2=[]

 for filename in os.listdir(directory): 
     array.append(os.path.join(directory, filename))
     months.append(filename)
     print(filename)   
 num_month=len(months) 

 for x in range(num_month):   
     n_f_sf=0 #number of files inside a subfolder
     name_f=[]#array for storing file names   
     print("\n\nList of files")
     print("-"*30)
     for file in os.listdir(array[x]):
             print(file)
             name_f.append(file)#storing names of files in an array
             n_f_sf=n_f_sf+1
             zq=array[x]+'/'+ file
             sheets.append(zq)
     print("-"*30)
     print("Number of files in the folder",months[x],":",n_f_sf)
     for i in range(n_f_sf): 
         xl_workbook= xlrd.open_workbook(array[x]+'/'+name_f[i])
         xl_sheet = xl_workbook.sheet_by_index(0)
         print ('\nSheet name: %s' % xl_sheet.name)
         num_cols = xl_sheet.ncols    
         f_columns.append(num_cols)
         num_rows=xl_sheet.nrows
         f_rows.append(num_rows)
         print("Number of Rows:",f_rows[i])
         print("Number of columns:",f_columns[i])
         sheets.append(array[x]+'/'+name_f[i])

# TO MAKE THE AGGREGATE EXCEL SHEET [master to monthly]             
 for i in range(num_month):
     loc_array=[]
     namefile=[]
     for filename in os.listdir(directory+'/'+ months[i]): 
         loc_array.append(os.path.join(directory+'/'+months[i], filename))
         namefile.append(filename)
     sh2=[pd.ExcelFile(name) for name in loc_array]
     fr2=[y.parse(y.sheet_names[0], header=None,index_col=None) for y in sh2]
     comb2=pd.concat(fr2)
     outdir2=r"C:\Users\Arjun\Documents\Trimester 5\TRIAL\DEMAND_ANALYSIS-DATA\CAP_MONTHwise\\"+ months[i] +".xlsx"
     comb2.to_excel(outdir2, header=False, index=False)        
# TO MAKE THE AGGREGATE EXCEL SHEET [monthly to agg]        
 for filename in os.listdir(directory_2): 
     array2.append(os.path.join(directory_2, filename))
     months2.append(filename)
 outdir=r"C:\Users\Arjun\Documents\Trimester 5\TRIAL\DEMAND_ANALYSIS-DATA\CAP_AGGRG\\"+months[0]+'_'+months[i]+".xlsx"   
 sh1=[pd.ExcelFile(name) for name in array2]
 fr1=[y.parse(y.sheet_names[0], header=None,index_col=None) for y in sh1]
 comb1=pd.concat(fr1)
 comb1.to_excel(outdir, header=False, index=False)

#################################################################
#cleaning & saving
 p1f=pd.read_excel(outdir,sep='\t',header=None)
 import CLEANING as clean
 pd2=clean.clean(p1f)
 pd2.to_excel(r"C:\Users\Arjun\Documents\Trimester 5\TRIAL\DEMAND_ANALYSIS-DATA\New folder\working.xlsx", header=True, index=False)
 print("\nAggregation is done\n")
################################################################################